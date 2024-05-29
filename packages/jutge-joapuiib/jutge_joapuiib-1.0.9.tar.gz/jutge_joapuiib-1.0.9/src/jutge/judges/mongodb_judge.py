from glob import glob
import os
import re
from colorama import Fore
import time
import sys
import traceback
from .base_judge import BaseJudge
from ..status import Status
from ..process import run_process, run_process_interactive, TimeoutError, ExitCodeError
from .. import utils
from ..models.exercise import Exercise
from pprint import pprint

class MongoDBJudge(BaseJudge):
    def __init__(self, base_dir, tests, args):
        super().__init__(base_dir, tests, args)

        # If not specified, will read from root (base_dir)
        self.package = tests.get("package", "")
        self.package = "/".join(self.package.split("."))
        self.database = tests.get("database", None)

        # Docker image
        self.image = "mongo:latest"

        # SQL docker container
        self.container = "mongodb_judge"

        self.user = "root"
        self.password = "1234"

        self.init_scripts = tests.get("init", [])
        if not isinstance(self.init_scripts, list):
            self.init_scripts = [self.init_scripts]

        self.post_scripts = tests.get("post", [])
        if not isinstance(self.post_scripts, list):
            self.post_scripts = [self.post_scripts]

        self.result = {}
        self.result["exercises"] = []

        self.light = args.light


    def stop_database(func):
        def wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except Exception as e:
                print(f"{Fore.RED}Error:{Fore.RESET}")
                print(e)
                print(traceback.format_exc())
                # self.delete_container()

        return wrapper


    def init_container(self):
        if not self.get_cointainer_id():
            self.delete_container()
            self.start_container()
        self.wait_until_container_healthy()


    def start_container(self):
        command = (f"docker run -d --name {self.container}"
                   # f" -e LANG=en_US.utf8"
                   f" -e MYSQL_ROOT_PASSWORD={self.password}"
                   " --health-cmd=\"mongosh --eval 'db.runCommand({ping: 1})' | grep 'ok' || exit 1\" --health-interval=2s"
                   f" {self.image}"
                   # " mysqld --lower_case_table_names=1"
        )
        print(command)
        out = utils.run_or_exit(run_process, command,
                out=f"Init {self.image} {self.container} container...",
                err=f"Error initializing {self.image} container").stdout

    def get_cointainer_id(self):
        command = f"docker ps -q -f name={self.container}"
        container_id = run_process(command).stdout.strip()
        return container_id


    def wait_until_container_healthy(self):
        command = (f"docker inspect -f {{{{.State.Health.Status}}}} {self.container}")

        def wait_until_healthy():
            out = run_process(command).stdout.strip()
            while not out == "healthy":
                time.sleep(2)
                out = run_process(command).stdout.strip()
                print(out[0], end="", flush=True)

        utils.run_or_exit(wait_until_healthy,
            out=f"Waiting until {self.container} is ready... ",
            err=f"Error checking {self.container} is ready.")

    def delete_container(self):
        command = f"docker ps -q -f status=exited -f name={self.container}"
        container_id = run_process(command).stdout.strip()
        if container_id:
            command = f"docker rm -f {self.container}"
            out = utils.run_or_exit(run_process, command,
                    out=f"Removing {self.image} {self.container} container...",
                    err=f"Error removing {self.image} container").stdout


    def run_init_scripts(self):
        for script in self.init_scripts:
            if isinstance(script, dict):
                if "import" in script:
                    filepath = script["import"]
                    collection = script["collection"]
                    self.copy_file(filepath)
                    self.import_data(filepath, collection)
            else:
                self.run_query(script)

    def copy_file(self, filepath):
        full_path = f"{self.base_dir}/{self.package}/{filepath}"
        command = (f"docker cp {full_path} {self.container}:{filepath}"
        )
        # print(query)
        return run_process(command)

    def run_post_scripts(self):
        self.run_queries(self.post_scripts)

    def import_data(self, filepath, collection, is_array=False, timeout=10):
        args = ""
        if is_array:
            args = "--jsonArray"
        command = (f"docker exec -i {self.container}"
                   f" mongoimport --db {self.database} --collection {collection} --file {filepath} {args}"
        )
        # print(command)
        return run_process(command, timeout=timeout)


    def run_queries(self, queries, error_msg="Error running queries:", timeout=10):
        for query in queries:
            try:
                result = self.run_query(query, timeout=timeout)
            except ExitCodeError as e:
                print(f"Error running query: {query}")
                print(f"  {Fore.RED}{error_msg}{Fore.RESET}")
                print(f"  {Fore.RED}{e}{Fore.RESET}")


    def run_query(self, query, force=False, timeout=2):
        return self.run_raw_query(query, force=force, timeout=timeout, database=self.database)

    def run_raw_query(self, query, force=False, timeout=2, database=None):
        args = "-t --default-character-set=utf8"
        if force:
            args += " -f"
        if database:
            args += f" -D {self.database}"

        query = query.replace("'", "\"")
        command = (f"docker exec -i {self.container}"
                   f" mongosh {self.database} --quiet --eval '{query}'"
        )
        # print(command)
        return run_process(command, timeout=timeout)



    def run_interactive(self):
        args = "-t --default-character-set=utf8"
        if self.database:
            args += f" -D {self.database}"

        command = (f"docker exec -it {self.container}"
                   f" mysql -u{self.user} -p{self.password} --silent {args}"
        )
        run_process_interactive(command)


    def create_database_if_not_exists(self):
        query = f"CREATE DATABASE IF NOT EXISTS {self.database};"
        self.run_raw_query(query, force=True)


    def judge(self, interactive=False):
        if len(self.exercises) > 0:
            self.init_container()

            # if self.database:
            #     self.create_database_if_not_exists();

            utils.run_or_exit(self.run_init_scripts,
                out=f"Running init scirpts...",
                err=f"Error running init scripts")

            # print(f"Interactive: {interactive}")
            for exercise in self.exercises:
                self.judge_exercise(exercise, interactive)
                self.result["exercises"].append(exercise.get_result())

            utils.run_or_exit(self.run_post_scripts,
                out=f"Running post scirpts...",
                err=f"Error running post scripts")

            return self.result


    @stop_database
    def judge_exercise(self, exercise, interactive):
        name = exercise.name

        if not name:
            print(f"{Fore.RED}Error! No s'ha especificat la clau \"name\" en algun exercici.{Fore.RESET}")
            raise Exception("No class name specified")

        dir_path = f"{self.base_dir}/{self.package}/{exercise.subpackage}"
        dir_path = re.sub(r"[/]+", "/", dir_path)
        dir_path = re.sub(r"[/]+$", "", dir_path)

        print("=" * 20)
        print(name)

        source_file = next((os.path.join(root, file)
                            for root, _, files in os.walk(dir_path)
                            for file in files if re.match(r"[_]?" + name + r".js", file)
                            ) , None)
        if not source_file:
            print(f"{Fore.RED}{name}: Not found{Fore.RESET}")
            exercise.result["found"] = False
            exercise.result["source_file"] = source_file
            print(f"{Fore.RED}Error! No script found{Fore.RESET}")
            return exercise.result

        print(source_file)
        exercise.result["found"] = True
        exercise.result["source_file"] = source_file

        # Print sources
        with open(source_file) as f:
            exercise.source = f.read().strip().replace("\t", "    ")
            self.print_source(exercise.source)
            print()
            # result = self.run_exercise(name, exercise, source, interactive)
            self.run_object(exercise, interactive=interactive, indent=1)
            utils.print_lines(f"- STATUS {exercise.name}: {exercise.status}", indent=1)
        print()
        return exercise.result


    def run_object(self, _object, indent=0, interactive=False):

        _object.set_status(Status.PERFECT)
        self.execute_object(_object, indent=indent)

        if _object.status == Status.PERFECT:
            self.compare_object(_object)

            if isinstance(_object, Exercise):
                self.print_exercise(_object)

            if _object.tests:
                for unit_test in _object.tests:
                    self.run_object(unit_test, indent=indent + 1, interactive=False)
                    status = _object.status.merge(unit_test.status)
                    self.print_unit_test(unit_test, indent=indent + 1)
                    _object.set_status(status)

        if interactive:
            self.run_interactive()

        self.run_queries(_object.clean, timeout=10, error_msg=f"Error running clean scripts in {_object.name}")

        return


    def execute_object(self, _object, indent=0):
        if not _object.source:
            _object.set_status(Status.NO_SOURCE)
            return

        self.run_queries(_object.init, timeout=10, error_msg=f"Error running init scripts in {_object.name}")

        try:
            result_query = self.run_query(_object.source, force=_object.force, timeout=10)
            _object.output = result_query.stdout.strip()
            _object.stderr = re.sub(r" at line \d+", "", result_query.stderr.strip())
        except TimeoutError:
            _object.set_status(Status.TIMEOUT)
        except ExitCodeError as e:
            _object.stderr = re.sub(r" at line \d+", "", e.stderr).strip()
            if not _object.expected_stderr:
                _object.set_status(Status.RUNTIME)
                utils.print_lines(f"{Fore.RED}{_object.stderr}{Fore.RESET}", indent=indent + 2)
                _object.result["error"] = _object.stderr

        self.run_queries(_object.post, timeout=10, error_msg=f"Error running post scripts in {_object.name}")


    def compare_object(self, _object):
        output = _object.output
        expected_output = _object.expected_output

        if _object.expected_stderr:
            output = _object.stderr
            expected_output = _object.expected_stderr

        if expected_output:
            if not output:
                _object.set_status(Status.EMPTY)
            else:
                _object.colored_output, _object.colored_expected_output, status = utils.colored_diff(output, expected_output)
                _object.set_status(status)
                unified_diff = utils.unified_diff(output, expected_output)
                if unified_diff:
                    _object.result["diff"] = unified_diff


    def print_exercise(self, exercise, indent=0):
        if exercise.status != Status.PERFECT:
            if exercise.expected_output:
                expected_output = exercise.colored_expected_output if exercise.colored_expected_output else exercise.expected_output
                utils.print_lines("- expected output:", indent=indent + 1)
                utils.print_lines(expected_output, indent=indent + 3)
            if exercise.output:
                output = exercise.colored_output if exercise.colored_output else exercise.output
                utils.print_lines("- output:", indent=indent + 1)
                utils.print_lines(output, indent=indent + 3)
            if exercise.expected_stderr:
                expected_stderr = exercise.colored_expected_output if exercise.colored_expected_output else exercise.expected_stderr
                utils.print_lines("- expected stderr:", indent=indent + 1)
                utils.print_lines(expected_stderr, indent=indent + 3)
            if exercise.stderr:
                stderr = exercise.colored_output if exercise.colored_output else f"{Fore.RED}{exercise.stderr}{Fore.RESET}"
                utils.print_lines("- stderr:", indent=indent + 1)
                utils.print_lines(stderr, indent=indent + 3)

    def print_unit_test(self, unit_test, indent=0):
        utils.print_lines(f"- test {unit_test.name}: {unit_test.status}", indent=indent)

        if unit_test.status != Status.PERFECT:
            if unit_test.input:
                utils.print_lines("- input:", indent=indent + 1)
                utils.print_lines(f"{Fore.CYAN}{unit_test.input}{Fore.RESET}", indent=indent + 3)
            elif unit_test.source:
                utils.print_lines("- source:", indent=indent + 1)
                utils.print_lines(f"{Fore.CYAN}{unit_test.source}{Fore.RESET}", indent=indent + 3)

            self.print_exercise(unit_test, indent=indent)

    def print_source(self, source_content):
        utils.line_number_print(utils.highlight(source_content, "js", self.light).strip())

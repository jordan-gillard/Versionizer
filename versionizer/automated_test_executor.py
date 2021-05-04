import os
from argparse import Namespace

from utils import print_bright_blue


class AutomatedTestExecutor:

    # def _check_for_versions(self):
    #     if not self.namespace.previous_version and not self.namespace.new_version:
    #         print("Previous version and new version are not set. Versionizer"
    #               " will run tests with the latest version of the library.")

    # @staticmethod
    # def _install_python_library(library, version=None):
    #     if version:
    #         os.system(f"pip install -q {library}=={version}")
    #     else:
    #         os.system(f"pip install -q {library}")

    @staticmethod
    def _run_tests_in_test_dir(test_location):
        print(f"pytest --quiet --color=yes {test_location}")
        os.system(f"pytest --quiet --color=yes {test_location}")

    # def _run_tests_for_version(self, version):
    #     print_bright_blue(
    #         f"Running tests with {self.namespace.library}:{version}")
    #     self._install_python_library(self.namespace.library,
    #                                  version)
    #     self._run_tests_in_test_dir(self.namespace.project_path)
    #
    # def _run_tests_for_latest_version(self):
    #     print_bright_blue(
    #         f"Running tests with latest version of {self.namespace.library}")
    #     self._install_python_library(self.namespace.library)
    #     self._run_tests_in_test_dir(self.namespace.project_path)
    @staticmethod
    def run_tests(test_location):
        print_bright_blue("Beginning test run.")
        AutomatedTestExecutor._run_tests_in_test_dir(test_location)
        # self._check_for_versions()
        # if self.namespace.previous_version:
        #     self._run_tests_for_version(self.namespace.previous_version)
        # if self.namespace.new_version:
        #     self._run_tests_for_version(self.namespace.new_version)
        # else:
        #     self._run_tests_for_latest_version()
        # # Return environment to using previous version
        # self._install_python_library(self.namespace.library,
        #                              self.namespace.previous_version)

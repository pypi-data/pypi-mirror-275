"""
Python SDK external package
"""

# Imports
import os
import sys
from dotenv import load_dotenv
from panda_server_sdk.panda_server_sdk_keys import TestingPandaPythonSDKKEYS


class TestingPandaPythonSDK(TestingPandaPythonSDKKEYS):
    """
    Class that contains methods getting data from .env file
    """

    # Load .env
    @staticmethod
    def __load_env_for_project(project_name, custom_path=None):
        """
        Loads the .env file for the specified project
        :param project_name: string of the desired project name
        :param custom_path: string of the desired path that .env file is to be loaded
        """
        if custom_path:
            path = custom_path
        else:
            path = f'\opt\{project_name}\.env'  # pylint: disable = anomalous-backslash-in-string

        # Construct the path to the .env file using the project name
        env_path = os.path.abspath(os.path.join(path))
        load_dotenv(dotenv_path=env_path)

        return env_path

    # Get Run Title from .env
    def get_title(self, project_name, custom_path=None):
        """
        Returns the TP_TITLE from the .env file for the specified project
        :param project_name: string of the desired project name
        :param custom_path: string of the desired path that .env file is to be loaded
        """
        self.__load_env_for_project(project_name, custom_path)
        return os.environ.get(self.TP_TITLE)

    # Get Github Branch from .env
    def get_branch(self, project_name, custom_path=None):
        """
        Returns the TP_BRANCH from the .env file for the specified project
        :param project_name: string of the desired project name
        :param custom_path: string of the desired path that .env file is to be loaded
        """
        self.__load_env_for_project(project_name, custom_path)
        return os.environ.get(self.TP_BRANCH)

    # Get Browser from .env
    def get_browser(self, project_name, custom_path=None):
        """
        Returns the TP_BROWSER from the .env file for the specified project
        :param project_name: string of the desired project name
        :param custom_path: string of the desired path that .env file is to be loaded
        """
        self.__load_env_for_project(project_name, custom_path)
        return os.environ.get(self.TP_BROWSER)

    # Get Reruns from .env
    def get_reruns(self, project_name, custom_path=None):
        """
        Returns the TP_RERUNS from the .env file for the specified project
        :param project_name: string of the desired project name
        :param custom_path: string of the desired path that .env file is to be loaded
        """
        self.__load_env_for_project(project_name, custom_path)
        return os.environ.get(self.TP_RERUNS)

    # Get Parallels from .env
    def get_parallels(self, project_name, custom_path=None):
        """
        Returns the TP_PARALLELS from the .env file for the specified project
        :param project_name: string of the desired project name
        :param custom_path: string of the desired path that .env file is to be loaded
        """
        self.__load_env_for_project(project_name, custom_path)
        return os.environ.get(self.TP_PARALLELS)

    # Get Cases from .env
    def get_cases(self, project_name, custom_path=None):
        """
        Returns the TP_CASES from the .env file for the specified project
        :param project_name: string of the desired project name
        :param custom_path: string of the desired path that .env file is to be loaded
        """
        self.__load_env_for_project(project_name, custom_path)
        return os.environ.get(self.TP_CASES)

    # Get Argument from .env
    def get_argument(self, project_name, custom_path=None):  # pylint: disable = inconsistent-return-statements
        """
        Returns the TP_ARGUMENTS from the .env file for the specified project
        :param project_name: string of the desired project name
        :param custom_path: string of the desired path that .env file is to be loaded
        """
        self.__load_env_for_project(project_name, custom_path)
        return os.environ.get(self.TP_ARGUMENTS)

    @staticmethod
    def get_local_arguments():
        """
        Returns all the local arguments
        """
        tp_local_arguments = {}

        for argument in sys.argv:
            if '=' in argument:
                key, value = argument.split('=', 1)
                tp_local_arguments[key] = value

        return tp_local_arguments

    def get_local_argument(self, argument):
        """
        Returns the desired local argument from local arguments
        :param argument: string of the desired local argument name
        """
        tp_local_arguments = self.get_local_arguments()
        return tp_local_arguments[argument]

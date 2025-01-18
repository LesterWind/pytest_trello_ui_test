import os
from configparser import ConfigParser


class MyConfigParser(ConfigParser):
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)


class CommonUtils:
    def __init__(self):
        pass

    @staticmethod
    def get_project_directory():
        project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return project_directory

    @staticmethod
    def load_ini(file_path):
        config = MyConfigParser()
        config.read(file_path)
        return config

    def path_setting(self, *relative_path_parts: str) -> str:
        if not relative_path_parts:
            raise ValueError("You must provide at least one relative path part")
        project_directory = self.get_project_directory()
        relative_path = os.path.join(*relative_path_parts)
        full_path = os.path.join(project_directory, relative_path)
        return full_path

    def get_domain(self):
        config_path = self.path_setting("config", "domain.ini")
        return self.load_ini(config_path)

    def get_account(self):
        accounts_path = self.path_setting("config", "accounts.ini")
        return self.load_ini(accounts_path)

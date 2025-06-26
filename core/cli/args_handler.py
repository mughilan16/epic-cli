import argparse
from config.args_config import args
from core.cli.args import Args

class ArgsHandler:
    def __init__(self, description, version): 
        self.version = version
        self.description = description
        self.parser = argparse.ArgumentParser(description=self.description); 
        self.parse_cli_args()

    def parse_cli_args(self):
        for arg in args:
            arg.add_argument(self.parser)

    def parse_args(self):
        return self.parser.parse_args()

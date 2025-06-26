from core.cli.args_handler import ArgsHandler

class App:
    def __init__(self):
        self.name = "Epic CLI"
        self.version = "0.0.1"
        self.description = "EPIC CLI is a command line interface for file collection"
        self.arg_handler = ArgsHandler(version=self.version)

    def run(self):
        self.args = self.arg_handler.parse_args()
        print("prefix : ", self.args.prefix); 
        print("job numebr : ", self.args.jobno);  
        print("upload : ", self.args.upload);

if __name__ == "__main__":
    app = App()
    app.run()

class Args:
    def __init__(self, short, long, description, type="str", required=False, default=False):
        self.short = short
        self.long = long
        self.descrtiption = description
        self.type = type
        self.required = required
        self.default = default
    
    def add_argument(self, parser):
            if self.type == "bool":
                parser.add_argument(self.short, self.long, help=self.descrtiption, action="store_true", default=self.default)
            else:
                parser.add_argument(self.short, self.long, help=self.descrtiption, required=self.required) 
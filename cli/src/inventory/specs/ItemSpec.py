import re
import sys

class ItemSpec:

    volume = 1
    version = 1
    actions = {}
    consumable = True

    def __init__(self, filename):
        self.filename = filename
        self.__set_cli_flags()

    def __set_cli_flags(self):
        flags = re.findall(
            r"((?<![a-z])-{1,2}[a-z0-9]+)(?:\s)([a-zA-Z0-9_]+)?",
            ' '.join(sys.argv[1:])
        )
        for arg, val in flags:
            arg = arg.replace("-","")
            setattr(self, arg, val)

    def use(self, **kwargs) -> None:
        print(f"You try the {self.__module__}, but it doesn't do anything.")

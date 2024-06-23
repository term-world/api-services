import os
import sys
import types
import inspect

class Look:

    def __init__(self, filename: str = ""):
        self.filename = filename
        self.__get_info()

    def __get_info(self):
        mod = types.ModuleType(self.filename)
        with open(self.filename, "r") as fh:
            source = fh.read()
        exec(source, mod.__dict__)
        cls = getattr(mod, self.filename)
        print(f"{cls(mode = 'look')}")

def cmd():
    sys.path.append(os.path.expanduser(os.getcwd()))
    Look(sys.argv[1])

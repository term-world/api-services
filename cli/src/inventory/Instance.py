class Instance:

    def __init__(self, filename: str = ""):
        self.valid = True
        self.__validate_file(filename)
        # TODO: Instead of reading file, use the code object?
        self.source = self.__read_file(filename)

    def __validate_file(self, filename: str = "") -> None:
        try:
            self.name = filename.split(".")[0]
            self.object = import_module(filename)
            getattr(obj, staus["name"])().use
        except Exception as e:
            self.valid = False

    def __read_file(self, filename: str = "") -> str:
        with open(filename, "r") as fh:
            return fh.read()

class ItemSpec:

    def __init__(self, filename: str = ""):
        self.file = filename
        self.actions = {}
        self.consumable = False
        self.volume = 1

    def use(self, **kwargs) -> None:
        print(f"You try the {self.__module__}, but it doesn't do anything.")

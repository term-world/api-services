class ItemSpec:

    volume = 1
    actions = {}
    consumable = True

    def use(self, **kwargs) -> None:
        print(f"You try the {self.__module__}, but it doesn't do anything.")

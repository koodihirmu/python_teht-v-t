class Julkaisu:
    def __init__(self, name: str) -> None:
        self.name = name
        pass

    def print(self):
        print(f"Name: {self.name}")


class Lehti(Julkaisu):
    def __init__(self, name: str, editor: str) -> None:
        super().__init__(name)
        self.editor = editor
        pass

    def print(self):
        super().print()
        print(f"Editor: {self.editor}")


class Kirja(Julkaisu):
    def __init__(self, name: str, author: str, pages: int) -> None:
        super().__init__(name)
        self.author = author
        self.pages = pages
        pass

    def print(self):
        super().print()
        print(f"Author: {self.author}\nPages: {self.pages}")

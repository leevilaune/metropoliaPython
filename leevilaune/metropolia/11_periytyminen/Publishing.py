class Publishing:
    def __init__(self,name):
        self.name = name

    def print_info(self):
        print(f"Nimi: {self.name}")

class Book(Publishing):
    def __init__(self, name, writer, pages):
        super().__init__(name)
        self.writer = writer
        self.pages = pages

    def print_info(self):
        print(f"Nimi: {self.name}, Kirjoittaja: {self.writer}, Sivumäärä: {self.pages}")

class Magazine(Publishing):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_info(self):
        print(f"Nimi: {self.name}, Päätoimittaja: {self.editor}")

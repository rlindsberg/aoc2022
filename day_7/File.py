from day_7.Folder import Folder


class File:
    def __init__(self, name: str, size: int, parent: Folder):
        self.name = name
        self.size = size
        self.parent = parent

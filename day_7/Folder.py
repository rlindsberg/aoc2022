from __future__ import annotations


class Folder:
    def __init__(self, name: str, parent: Folder):
        self.name = name
        self.parent = parent
        self.size = 0
        self.is_indexed = False

        self.children = []

    def update_file_sizes(self, size_to_add: int):
        self.size += size_to_add

        if self.name != '/':
            # roots parent is None
            self.parent.update_file_sizes(size_to_add)

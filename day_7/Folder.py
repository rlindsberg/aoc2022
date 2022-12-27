from __future__ import annotations


class Folder:
    def __init__(self, name: str, parent: Folder):
        self.name = name
        self.parent = parent
        self.size = 0

        self.children = []

from day_7.File import File
from day_7.Folder import Folder


class Finder:
    """Or you can call it File Explorer"""
    def __init__(self):
        self.parent_path = '/'
        self.current_path = '/'
        self.depth = 0

        self.dir_dict = {}
        self.index_root()

    def parse_file(self, parent_path: str, raw_file: str):
        raw_file_list = raw_file.split(' ')
        file_size = int(raw_file_list[0])
        file_name = raw_file_list[1]

        parent = self.dir_dict[parent_path]
        file = File(file_name, file_size, parent)

        return file

    def index_root(self):
        root_dir = Folder('/', None)
        self.dir_dict['/'] = root_dir

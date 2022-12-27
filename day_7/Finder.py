from day_7.File import File
from day_7.Folder import Folder


class Finder:
    """Or you can call it File Explorer"""
    def __init__(self):
        self.parent_path = '/'
        self.current_path = '/'
        self.trajectory = []

        self.folder_name_to_obj_map = {}
        self.file_name_to_obj_map = {}

        self.index_root()

    def parse_file(self, parent_path: str, raw_command: str):
        raw_file_list = raw_command.split(' ')
        file_size = int(raw_file_list[0])
        file_name = raw_file_list[1]

        parent = self.folder_name_to_obj_map[parent_path]
        file = File(file_name, file_size, parent)

        return file

    def index_root(self):
        root_dir = Folder('/', None)
        self.folder_name_to_obj_map['/'] = root_dir

    def parse_dir(self, parent_path: str, raw_command: str):
        """
        Parse raw command like "dir abc" and returns a Folder
        """
        raw_dir_list = raw_command.split(' ')
        dir_name = raw_dir_list[1]

        parent = self.folder_name_to_obj_map[parent_path]

        return Folder(dir_name, parent)

    def parse_raw_cmd_input(self, cmd_str):
        cmd_list = cmd_str.split('\n')
        cmd = cmd_list[0]
        res = cmd_list[1:]

        if cmd[:2] == 'cd':
            target_dir = cmd[3:]

            cmd_type = cmd[:2]
            argument = target_dir

            return cmd_type, argument

        elif cmd[:2] == 'ls':
            cmd_type = cmd[:2]

            return cmd_type, res
            # for item in res:
            #     # item can be file or dir
            #     if item[:3] == 'dir':
            #         # this is a dir
            #         dir_name = item[4:]
            #
            #         if dir_name not in dir_dict.keys():
            #             # index this dir
            #             temp_dir = Folder(dir_name, )

    def exec_cmd(self, cmd_str):
        # cd, arg or ls, response
        cmd_type, arg_or_res = self.parse_raw_cmd_input(cmd_str)

        if cmd_type == 'cd':
            target = arg_or_res
            if target == '/':
                # special case
                self.parent_path = '/'
                self.current_path = '/'
                self.trajectory = ['/']

            elif target == '..':
                # special case
                if len(self.trajectory) == 1:
                    print(self.trajectory)
                    print(self.parent_path)
                    assert self.parent_path == '/'
                    assert self.current_path == '/'
                    return

                self.current_path = self.parent_path
                self.parent_path = self.trajectory[-2]
                self.trajectory = self.trajectory[:-1]

            else:
                # go in a step
                self.trajectory.append(target)
                self.parent_path = self.current_path
                self.current_path = target

            print(cmd_str)
            print(f'Current path is {self.current_path}')

        elif cmd_type == 'ls':
            res = arg_or_res

            # parse all file and sub-dirs inside a dir
            for raw_command in res:
                # item can be a file or dir
                if raw_command[:3] == 'dir':
                    new_dir: Folder = self.parse_dir(parent_path=self.current_path, raw_command=raw_command)

                    if new_dir.name not in self.folder_name_to_obj_map.keys():
                        # index this dir
                        self.folder_name_to_obj_map[new_dir.name] = new_dir

                        # tell its parent that this dir exists
                        current_dir: Folder = self.folder_name_to_obj_map[self.current_path]
                        current_dir.children.append(new_dir)

                elif raw_command[:3] == '':
                    # end of the command
                    return

                else:
                    # this is a file
                    new_file: File = self.parse_file(parent_path=self.current_path, raw_command=raw_command)

                    if new_file.name not in self.file_name_to_obj_map.keys():
                        self.file_name_to_obj_map[new_file.name] = new_file

                        current_dir: Folder = self.folder_name_to_obj_map[self.current_path]
                        current_dir.update_file_sizes(new_file.size)
                        current_dir.children.append(new_file)

            print('ls')

        else:
            raise Exception('cmd is not valid')

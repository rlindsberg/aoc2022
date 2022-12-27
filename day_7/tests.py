import unittest

from day_7.Finder import Finder
from day_7.a import sum_all_sub_folder_sizes


class TestDay7(unittest.TestCase):
    def test_parse_file(self):
        file_str = '5 file2-a'

        finder = Finder()

        res = finder.parse_file('/', file_str)

        self.assertEqual(res.parent.name, '/')
        self.assertEqual(res.size, 5)
        self.assertEqual(res.name, 'file2-a')

    def test_parse_dir(self):
        dir_str = 'dir a'

        finder = Finder()

        res = finder.parse_dir('/', dir_str)

        self.assertEqual(res.parent.name, '/')
        self.assertEqual(res.name, 'a')

    def test_part_a(self):
        data = """
$ cd /
$ ls
dir a
dir b
3 file1-root
$ cd a
$ ls
5 file2-a
$ cd ..
$ cd b
$ ls
7 file3-b"""

        """
        /
            - a
                - 5kb file2-a

            - b
                - 7kb file3-b

            - 3 kb file1-root
        """
        print(data)

        finder = Finder()
        ans = sum_all_sub_folder_sizes(finder, data, at_most=100000)

        self.assertEqual(ans, 12)

    def test_part_a_2(self):
        """go back too many times, shouldn't crash"""
        data = """
$ cd /
$ cd ..
$ ls
dir a
dir b
3 file1-root
$ cd a
$ ls
5 file2-a
$ cd ..
$ cd b
$ ls
7 file3-b"""

        """
        /
            - a
                - 5kb file2-a

            - b
                - 7kb file3-b

            - 3 kb file1-root
        """
        print(data)

        finder = Finder()
        ans = sum_all_sub_folder_sizes(finder, data, at_most=100000)

        self.assertEqual(ans, 12)

    def test_part_a_example(self):
        """Use the example input from aoc"""
        data = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

        print(data)

        finder = Finder()
        ans = sum_all_sub_folder_sizes(finder, data, at_most=100000)

        self.assertEqual(ans, 95437)
        self.assertEqual(finder.folder_name_to_obj_map['/'].size, 48381165)

    def test_part_a_example_same_sub_folder_name_as_parent(self):
        """Use the first few lines of the input data, change a sub-folder's name to its parent's"""
        data = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir a
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

        print(data)

        finder = Finder()
        ans = sum_all_sub_folder_sizes(finder, data, at_most=100000)

        self.assertEqual(ans, 95437)
        self.assertEqual(finder.folder_name_to_obj_map['/'].size, 48381165)

import unittest

from day_7.a import sum_all_sub_folder_sizes


class TestDay7(unittest.TestCase):
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

        ans = sum_all_sub_folder_sizes(data, at_most=100000)

        self.assertEqual(ans, 12)

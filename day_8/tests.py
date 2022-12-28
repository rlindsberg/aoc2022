import unittest

from day_7.Finder import Finder
from day_7.a import sum_all_sub_folder_sizes
from day_8.a import count_visible_trees


class TestDay7(unittest.TestCase):

    def test_part_a(self):
        data = """30373
25512
65332
33549
35390"""

        print(data)

        ans = count_visible_trees(data)

        self.assertEqual(ans, 21)

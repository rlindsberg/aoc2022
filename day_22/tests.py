import unittest

from day_22.Map import Map
from day_22.Person import Person


class TestDay22(unittest.TestCase):
    def test_part_a_sample(self):
        data = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""

        my_map = Map(data)

        me = Person(my_map)

        instruction = data.split('\n')[-1]
        me.move_by_instruction(instruction)

        ans = me.compute_score()

        self.assertEqual(ans, 6032)

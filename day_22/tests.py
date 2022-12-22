import unittest

from day_22.Me import Me
from day_22.a import draw_map, compute_score, my_map


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

        instruction, max_x, max_y = draw_map(data)
        me = Me(my_map, max_x, max_y)
        me.move_by_instructions(instruction)

        ans = compute_score(me.position, me.facing)

        self.assertEqual(ans, 6032)

    def test_part_a_sample_2(self):
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

10R5L5R10L4R5L50LL1L2L3R2L2R50"""

        instruction, max_x, max_y = draw_map(data)
        me = Me(my_map, max_x, max_y)
        me.move_by_instructions(instruction)

        ans = compute_score(me.position, me.facing)

        self.assertEqual(ans, 12049)

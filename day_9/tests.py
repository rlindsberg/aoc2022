import unittest

from day_9.a import move_head_tail_and_compute_n_visited_pos
from day_9.knot import Knot


class TestDay9(unittest.TestCase):

    def test_part_a(self):
        data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

        print(data)

        head = Knot()
        tail = Knot()

        move_head_tail_and_compute_n_visited_pos(data, head, tail)

        self.assertEqual(head.x, 2)
        self.assertEqual(head.y, 2)

        self.assertEqual(tail.x, 1)
        self.assertEqual(tail.y, 2)

    def test_part_a_answer(self):
        """There are 13 positions the tail visited at least once."""
        data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

        print(data)

        head = Knot()
        tail = Knot()

        ans = move_head_tail_and_compute_n_visited_pos(data, head, tail)

        self.assertEqual(ans, 13)

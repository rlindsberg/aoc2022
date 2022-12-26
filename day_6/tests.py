import unittest

from day_6.a import find_start_of_packet_marker_index


class TestDay6(unittest.TestCase):
    def test_part_a(self):
        data = 'aabcd'

        ans = find_start_of_packet_marker_index(data)

        self.assertEqual(ans, 5)

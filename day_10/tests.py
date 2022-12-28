import unittest

from day_10.CPU import CPU
from day_10.a import parse_and_exec_cmd


class TestDay10(unittest.TestCase):

    def test_part_a_small(self):
        data = """noop
addx 3
addx -5
"""

        cpu = CPU()
        _ = parse_and_exec_cmd(data, cpu)

        self.assertEqual(cpu.register, -1)


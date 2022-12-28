from __future__ import annotations

from math import sqrt


class Knot:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, direction):
        # move up
        if direction == 'U':
            self.y += 1

        # right
        elif direction == 'R':
            self.x += 1

        # down
        elif direction == 'D':
            next_y = self.y - 1
            if next_y >= 0:
                self.y = next_y
            else:
                print('cannot move down')

        # left
        elif direction == 'L':
            next_x = self.x - 1
            if next_x >= 0:
                self.x = next_x
            else:
                print('cannot move left')

    def follow(self, h: Knot):
        # if distance is too far, then the tail will follow the head

        d_x = h.x - self.x
        d_y = h.y - self.y
        # case 1, diagonal
        if sqrt(d_x ** 2 + d_y ** 2) == sqrt(5):
            if d_x >= 0:
                self.move('R')
            else:
                self.move('L')

            if d_y >= 0:
                self.move('U')
            else:
                self.move('D')

        # case 2 horizontal
        if h.x - self.x == 2:
            self.move('R')
        elif h.x - self.x == -2:
            self.move('L')

        # case 3, vertical
        if h.y - self.y == 2:
            self.move('U')
        elif h.y - self.y == -2:
            self.move('D')

        d_x = h.x - self.x
        d_y = h.y - self.y
        assert sqrt(d_x ** 2 + d_y ** 2) <= sqrt(2)

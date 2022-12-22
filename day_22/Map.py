import numpy as np


class Map:
    def __init__(self, data):
        self.map_array, self.max_x, self.max_y = self.build_map(data)

    @staticmethod
    def build_map(data):
        input_list = data.split("\n")
        max_x = 0,
        max_y = 0

        # compute boundary
        for row_idx, row in enumerate(input_list):
            # reached the end
            if row == '':
                max_x = row_idx

            for column_idx, _ in enumerate(row):
                if column_idx > max_y:
                    max_y = column_idx

        assert max_x != 0
        assert max_y != 0

        my_map = np.full([max_x + 1, max_y + 1], fill_value=-1)

        for row_idx, row in enumerate(input_list):
            for column_idx, element in enumerate(row):
                if element == ' ':
                    my_map[row_idx][column_idx] = -1
                elif element == '.':
                    my_map[row_idx][column_idx] = 0
                elif element == '#':
                    my_map[row_idx][column_idx] = 1

        return my_map, max_x, my_map

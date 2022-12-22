import numpy as np


class Map:
    def __init__(self, data):
        self.map_array, self.max_x, self.max_y = self.build_map(data)

        self.get_start_end_by_row = {}
        self.get_start_end_by_column = {}
        self.compute_start_end_for_each_row()

    def compute_start_end_for_each_row(self):
        m, n = self.map_array.shape

        for row_idx in range(m):
            start, end = 0, 0

            row = self.map_array[row_idx]

            # compute the first wall or tile
            for column_idx in range(n):
                if row[column_idx] != -1:
                    # a wall or a tile
                    start = column_idx
                    break

            # compute the last wall or tile
            for column_idx in reversed(range(n)):
                if row[column_idx] != -1:
                    # a wall or a tile
                    end = column_idx
                    break

            assert start <= end

            self.get_start_end_by_row[row_idx] = (start, end)
            print('')

        for col_idx in range(n):
            start, end = None, None

            col = self.map_array[:, col_idx]

            # compute the first wall or tile
            for row_idx in range(m):
                if col[row_idx] != -1:
                    # a wall or a tile
                    start = row_idx
                    break

            # compute the last wall or tile
            for row_idx in reversed(range(m)):
                if col[row_idx] != -1:
                    # a wall or a tile
                    end = row_idx
                    break

            assert start <= end

            self.get_start_end_by_column[col_idx] = (start, end)
            print('')

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

        return my_map, max_x, max_y

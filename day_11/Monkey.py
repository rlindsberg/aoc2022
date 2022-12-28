import queue


class Monkey:
    def __init__(self, item_list, op, test_func, next_monkey_if_true, next_monkey_if_false):
        # a fifo queue, use .append() to add and .pop(0) to remove
        self.item_list = item_list
        self.op = op
        self.test_func = test_func
        self.next_monkey_if_true = next_monkey_if_true
        self.next_monkey_if_false = next_monkey_if_false

    def test(self, item_worry_level):
        new = item_worry_level
        res = eval(self.test_func)
        if res == 0:
            # true
            return self.next_monkey_if_true
        else:
            return self.next_monkey_if_false

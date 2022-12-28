import queue


class Monkey:
    def __init__(self, op, test_func, next_monkey_if_true, next_monkey_if_false):
        self.item_queue = queue.Queue()
        self.op = op
        self.test_func = test_func
        self.next_monkey_if_true = next_monkey_if_true
        self.next_monkey_if_false = next_monkey_if_false

    def test(self):
        res = eval(self.test_func)
        if res == 0:
            # true
            return self.next_monkey_if_true
        else:
            return self.next_monkey_if_false

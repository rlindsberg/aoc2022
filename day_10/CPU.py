class CPU:
    def __init__(self):
        # only one register called X
        self.register = 1
        # starts with the first cycle
        self.counter = 0
        # addx takes two cycles
        self.addx_timer = 1

        self.sum_signal_strength = 0

    def parse_and_exec_cmd(self, raw_input: str):
        # the start of a new cycle
        self.counter += 1
        print(f'Start of cycle {self.counter}')

        # now we are in the middle of a cycle
        if self.counter in [20, 60, 100, 140, 180, 220]:
            print('time to measure signal strength!')
            print(self.register)
            self.sum_signal_strength += self.counter * self.register

        if raw_input == 'noop':
            # noop has no effect
            pass
        elif raw_input == '':
            # end of cmd
            return
        else:
            # addx
            cmd_list = raw_input.split(' ')
            op = cmd_list[0]
            arg = cmd_list[1]

            if op == 'addx':
                if self.addx_timer == 0:
                    # reset timer
                    self.addx_timer = 1

                    # at the end of a cycle
                    self.register += int(arg)
                else:
                    self.addx_timer -= 1
                    self.parse_and_exec_cmd(raw_input)

        print(f'End of cycle {self.counter}')

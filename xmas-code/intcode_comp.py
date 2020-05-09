class Intcode_Computer(object):
    """This is a computer that reads in Intcode"""
    def __init__(self, program, init_input=0):
        super(Intcode_Computer, self).__init__()
        self.init_input = init_input
        self.program = program
        self.output = -1
        self.r_base = 0
        self.pos = 0

    def _parse_op(self, cmd_str):
        # take the 4 elements and return operation #
        return cmd_str

    def _step(self):
        if self.program[self.pos] == 99:
            self.pos = -1
            return

        op_code = self.program[self.pos]

        if op_code == 1:
            arg1, arg2, out = self.program[self.pos+1:self.pos+4]
            self.program[out] = self.program[arg1] + self.program[arg2]
            self.pos += 4

        elif op_code == 2:
            arg1, arg2, out = self.program[self.pos+1:self.pos+4]
            self.program[out] = self.program[arg1] * self.program[arg2]
            self.pos += 4

        elif op_code == 3:
            out = self.program[self.pos + 1]
            self.program[out] = self.init_input
            self.pos += 2

        elif op_code == 4:
            arg1 = self.program[self.pos + 1]
            self.output = self.program[arg1]
            self.pos += 2

    def run_all(self):
        while self.pos != -1:
            self._step()

        print("Done\n", self.program)

icc = Intcode_Computer([1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,2,19,6,23,1,23,5,27,1,9,27,31,1,31,10,35,2,35,9,39,1,5,39,43,2,43,9,47,1,5,47,51,2,51,13,55,1,55,10,59,1,59,10,63,2,9,63,67,1,67,5,71,2,13,71,75,1,75,10,79,1,79,6,83,2,13,83,87,1,87,6,91,1,6,91,95,1,10,95,99,2,99,6,103,1,103,5,107,2,6,107,111,1,10,111,115,1,115,5,119,2,6,119,123,1,123,5,127,2,127,6,131,1,131,5,135,1,2,135,139,1,139,13,0,99,2,0,14,0])
icc.run_all()
print(icc.program)

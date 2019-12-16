class Intcode_Computer(object):
    """docstring for Intcode_Computer"""
    def __init__(self, program, sys_input):
        super(Intcode_Computer, self).__init__()
        self.input = [*sys_input] if type(sys_input) == list else [sys_input]
        self.i = 0
        self.output = 0
        self.r_base = 0
        self.program = program

    def parse_cmd(self, cmd_str):
        cmd_arr = str(cmd_str)
        for _ in range(0,5-len(cmd_arr)):
            cmd_arr = '0' + cmd_arr

        return int(cmd_arr[-2] + cmd_arr[-1]), int(cmd_arr[-3]), int(cmd_arr[-4]), int(cmd_arr[-5])

    def m(self, mode, value, array, r_base):
        if mode == 1:
            return value
        elif mode == 2:
            return array[r_base + value]
        else: 
            return array[value]

    def r(self, mode, value, r_base):
        if mode == 2:
            return r_base + value
        else: 
            return value
        
    def run(self):
        p = self.program
        i = self.i

        op_code, a_mode, b_mode, c_mode = self.parse_cmd(p[i])
        
        while op_code != 99:     

            if op_code == 1: #add function
                p[self.r(c_mode, p[i+3], self.r_base)] = self.m(a_mode, p[i+1], p, self.r_base) + self.m(b_mode, p[i+2], p, self.r_base)            
                i += 4

            elif op_code == 2: #multi function
                p[self.r(c_mode, p[i+3], self.r_base)] = self.m(a_mode, p[i+1], p, self.r_base) * self.m(b_mode, p[i+2], p, self.r_base)            
                i += 4

            elif op_code == 3: # Take Input
                p[self.r(a_mode, p[i+1], self.r_base)] = self.input.pop()
                i += 2

            elif op_code == 4: # Send Input
                o_value = self.m(a_mode, p[i+1], p, self.r_base)
                print(o_value)
                i += 2

            elif op_code == 5: # Jump if true
                if self.m(a_mode, p[i+1], p, self.r_base) != 0:
                    i = self.m(b_mode, p[i+2], p, self.r_base)
                else: 
                    i += 3

            elif op_code == 6: # Jump if false
                if self.m(a_mode, p[i+1], p, self.r_base) == 0:
                    i = self.m(b_mode, p[i+2], p, self.r_base)
                else: 
                    i += 3

            elif op_code == 7: # less_fun
                p[self.r(c_mode, p[i+3], self.r_base)] = 1 if self.m(a_mode, p[i+1], p, self.r_base) < self.m(b_mode, p[i+2], p, self.r_base) else 0
                i += 4

            elif op_code == 8: # equal_fun
                p[self.r(c_mode, p[i+3], self.r_base)] = 1 if self.m(a_mode, p[i+1], p, self.r_base) == self.m(b_mode, p[i+2], p, self.r_base) else 0
                i += 4

            elif op_code == 9: # relative base change
                self.r_base += self.m(a_mode, p[i+1], p, self.r_base)
                i += 2

            else:
                print("Error at position: " + str(i))
                print("position value: " + str(op_code))
                return -1

            op_code, a_mode, b_mode, c_mode = self.parse_cmd(p[i])

computer = Intcode_Computer([3,8,1005,8,345,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,102,1,8,28,1006,0,94,2,106,5,10,1,1109,12,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,62,1,103,6,10,1,108,12,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,92,2,104,18,10,2,1109,2,10,2,1007,5,10,1,7,4,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,129,2,1004,15,10,2,1103,15,10,2,1009,6,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,164,2,1109,14,10,1,1107,18,10,1,1109,13,10,1,1107,11,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,1001,8,0,201,2,104,20,10,1,107,8,10,1,1007,5,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,101,0,8,236,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,257,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,279,1,107,0,10,1,107,16,10,1006,0,24,1,101,3,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,316,2,1108,15,10,2,4,11,10,101,1,9,9,1007,9,934,10,1005,10,15,99,109,667,104,0,104,1,21101,0,936995730328,1,21102,362,1,0,1105,1,466,21102,1,838210728716,1,21101,373,0,0,1105,1,466,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,1,235350789351,1,21101,0,420,0,1105,1,466,21102,29195603035,1,1,21102,1,431,0,1105,1,466,3,10,104,0,104,0,3,10,104,0,104,0,21101,0,825016079204,1,21101,0,454,0,1105,1,466,21101,837896786700,0,1,21102,1,465,0,1106,0,466,99,109,2,21201,-1,0,1,21101,0,40,2,21102,1,497,3,21101,0,487,0,1105,1,530,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,492,493,508,4,0,1001,492,1,492,108,4,492,10,1006,10,524,1101,0,0,492,109,-2,2105,1,0,0,109,4,2102,1,-1,529,1207,-3,0,10,1006,10,547,21102,1,0,-3,21201,-3,0,1,22102,1,-2,2,21101,1,0,3,21102,1,566,0,1105,1,571,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,594,2207,-4,-2,10,1006,10,594,21201,-4,0,-4,1106,0,662,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21101,613,0,0,1105,1,571,22101,0,1,-4,21101,0,1,-1,2207,-4,-2,10,1006,10,632,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,654,22101,0,-1,1,21102,654,1,0,105,1,529,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0] + ([0] * 10000), 2) 
computer.run()
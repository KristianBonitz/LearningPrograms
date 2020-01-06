import copy		

inputs = [[0, 1, 2, 3, 4], [1, 0, 2, 3, 4], [1, 2, 0, 3, 4], [1, 2, 3, 0, 4], [1, 2, 3, 4, 0], [0, 2, 1, 3, 4], [2, 0, 1, 3, 4], [2, 1, 0, 3, 4], [2, 1, 3, 0, 4], [2, 1, 3, 4, 0], [0, 2, 3, 1, 4], [2, 0, 3, 1, 4], [2, 3, 0, 1, 4], [2, 3, 1, 0, 4], [2, 3, 1, 4, 0], [0, 2, 3, 4, 1], [2, 0, 3, 4, 1], [2, 3, 0, 4, 1], [2, 3, 4, 0, 1], [2, 3, 4, 1, 0], [0, 1, 3, 2, 4], [1, 0, 3, 2, 4], [1, 3, 0, 2, 4], [1, 3, 2, 0, 4], [1, 3, 2, 4, 0], [0, 3, 1, 2, 4], [3, 0, 1, 2, 4], [3, 1, 0, 2, 4], [3, 1, 2, 0, 4], [3, 1, 2, 4, 0], [0, 3, 2, 1, 4], [3, 0, 2, 1, 4], [3, 2, 0, 1, 4], [3, 2, 1, 0, 4], [3, 2, 1, 4, 0], [0, 3, 2, 4, 1], [3, 0, 2, 4, 1], [3, 2, 0, 4, 1], [3, 2, 4, 0, 1], [3, 2, 4, 1, 0], [0, 1, 3, 4, 2], [1, 0, 3, 4, 2], [1, 3, 0, 4, 2], [1, 3, 4, 0, 2], [1, 3, 4, 2, 0], [0, 3, 1, 4, 2], [3, 0, 1, 4, 2], [3, 1, 0, 4, 2], [3, 1, 4, 0, 2], [3, 1, 4, 2, 0], [0, 3, 4, 1, 2], [3, 0, 4, 1, 2], [3, 4, 0, 1, 2], [3, 4, 1, 0, 2], [3, 4, 1, 2, 0], [0, 3, 4, 2, 1], [3, 0, 4, 2, 1], [3, 4, 0, 2, 1], [3, 4, 2, 0, 1], [3, 4, 2, 1, 0], [0, 1, 2, 4, 3], [1, 0, 2, 4, 3], [1, 2, 0, 4, 3], [1, 2, 4, 0, 3], [1, 2, 4, 3, 0], [0, 2, 1, 4, 3], [2, 0, 1, 4, 3], [2, 1, 0, 4, 3], [2, 1, 4, 0, 3], [2, 1, 4, 3, 0], [0, 2, 4, 1, 3], [2, 0, 4, 1, 3], [2, 4, 0, 1, 3], [2, 4, 1, 0, 3], [2, 4, 1, 3, 0], [0, 2, 4, 3, 1], [2, 0, 4, 3, 1], [2, 4, 0, 3, 1], [2, 4, 3, 0, 1], [2, 4, 3, 1, 0], [0, 1, 4, 2, 3], [1, 0, 4, 2, 3], [1, 4, 0, 2, 3], [1, 4, 2, 0, 3], [1, 4, 2, 3, 0], [0, 4, 1, 2, 3], [4, 0, 1, 2, 3], [4, 1, 0, 2, 3], [4, 1, 2, 0, 3], [4, 1, 2, 3, 0], [0, 4, 2, 1, 3], [4, 0, 2, 1, 3], [4, 2, 0, 1, 3], [4, 2, 1, 0, 3], [4, 2, 1, 3, 0], [0, 4, 2, 3, 1], [4, 0, 2, 3, 1], [4, 2, 0, 3, 1], [4, 2, 3, 0, 1], [4, 2, 3, 1, 0], [0, 1, 4, 3, 2], [1, 0, 4, 3, 2], [1, 4, 0, 3, 2], [1, 4, 3, 0, 2], [1, 4, 3, 2, 0], [0, 4, 1, 3, 2], [4, 0, 1, 3, 2], [4, 1, 0, 3, 2], [4, 1, 3, 0, 2], [4, 1, 3, 2, 0], [0, 4, 3, 1, 2], [4, 0, 3, 1, 2], [4, 3, 0, 1, 2], [4, 3, 1, 0, 2], [4, 3, 1, 2, 0], [0, 4, 3, 2, 1], [4, 0, 3, 2, 1], [4, 3, 0, 2, 1], [4, 3, 2, 0, 1], [4, 3, 2, 1, 0]]

p_input = 5

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
                if self.input == []:
                    return 'null'
                else:
                    p[self.r(a_mode, p[i+1], self.r_base)] = self.input.pop()
                i += 2

            elif op_code == 4: # Send Input
                self.output = self.m(a_mode, p[i+1], p, self.r_base)
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

        self.i = -1

def find_max_thruster_signal(input_list, amp_comp):
    max_output = 0
    best_settings = []

    for i in input_list:
    	out = run_amps(i, amp_comp)
    	if out >= max_output:
    		max_output = out
    		best_settings = i
    		print(i, max_output)

    return max_output, best_settings

def run_amps(phase_settings, amp_comp):
    
    amp_out = 0
    amps = []
    for i in range(0, 5):
    	amps.append(Intcode_Computer(amp_code, amp_comp[i]))

    return amp_out



amp_code = [3,8,1001,8,10,8,105,1,0,0,21,42,51,76,93,110,191,272,353,434,99999,3,9,1002,9,2,9,1001,9,3,9,1002,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,3,9,4,9,99,3,9,1002,9,4,9,101,5,9,9,1002,9,3,9,1001,9,4,9,1002,9,5,9,4,9,99,3,9,1002,9,5,9,101,3,9,9,102,5,9,9,4,9,99,3,9,1002,9,5,9,101,5,9,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99]
amp = Intcode_Computer(amp_code, [0,0])
amp.run()
print()

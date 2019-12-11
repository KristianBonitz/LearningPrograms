import copy		

inputs = [[0, 1, 2, 3, 4], [1, 0, 2, 3, 4], [1, 2, 0, 3, 4], [1, 2, 3, 0, 4], [1, 2, 3, 4, 0], [0, 2, 1, 3, 4], [2, 0, 1, 3, 4], [2, 1, 0, 3, 4], [2, 1, 3, 0, 4], [2, 1, 3, 4, 0], [0, 2, 3, 1, 4], [2, 0, 3, 1, 4], [2, 3, 0, 1, 4], [2, 3, 1, 0, 4], [2, 3, 1, 4, 0], [0, 2, 3, 4, 1], [2, 0, 3, 4, 1], [2, 3, 0, 4, 1], [2, 3, 4, 0, 1], [2, 3, 4, 1, 0], [0, 1, 3, 2, 4], [1, 0, 3, 2, 4], [1, 3, 0, 2, 4], [1, 3, 2, 0, 4], [1, 3, 2, 4, 0], [0, 3, 1, 2, 4], [3, 0, 1, 2, 4], [3, 1, 0, 2, 4], [3, 1, 2, 0, 4], [3, 1, 2, 4, 0], [0, 3, 2, 1, 4], [3, 0, 2, 1, 4], [3, 2, 0, 1, 4], [3, 2, 1, 0, 4], [3, 2, 1, 4, 0], [0, 3, 2, 4, 1], [3, 0, 2, 4, 1], [3, 2, 0, 4, 1], [3, 2, 4, 0, 1], [3, 2, 4, 1, 0], [0, 1, 3, 4, 2], [1, 0, 3, 4, 2], [1, 3, 0, 4, 2], [1, 3, 4, 0, 2], [1, 3, 4, 2, 0], [0, 3, 1, 4, 2], [3, 0, 1, 4, 2], [3, 1, 0, 4, 2], [3, 1, 4, 0, 2], [3, 1, 4, 2, 0], [0, 3, 4, 1, 2], [3, 0, 4, 1, 2], [3, 4, 0, 1, 2], [3, 4, 1, 0, 2], [3, 4, 1, 2, 0], [0, 3, 4, 2, 1], [3, 0, 4, 2, 1], [3, 4, 0, 2, 1], [3, 4, 2, 0, 1], [3, 4, 2, 1, 0], [0, 1, 2, 4, 3], [1, 0, 2, 4, 3], [1, 2, 0, 4, 3], [1, 2, 4, 0, 3], [1, 2, 4, 3, 0], [0, 2, 1, 4, 3], [2, 0, 1, 4, 3], [2, 1, 0, 4, 3], [2, 1, 4, 0, 3], [2, 1, 4, 3, 0], [0, 2, 4, 1, 3], [2, 0, 4, 1, 3], [2, 4, 0, 1, 3], [2, 4, 1, 0, 3], [2, 4, 1, 3, 0], [0, 2, 4, 3, 1], [2, 0, 4, 3, 1], [2, 4, 0, 3, 1], [2, 4, 3, 0, 1], [2, 4, 3, 1, 0], [0, 1, 4, 2, 3], [1, 0, 4, 2, 3], [1, 4, 0, 2, 3], [1, 4, 2, 0, 3], [1, 4, 2, 3, 0], [0, 4, 1, 2, 3], [4, 0, 1, 2, 3], [4, 1, 0, 2, 3], [4, 1, 2, 0, 3], [4, 1, 2, 3, 0], [0, 4, 2, 1, 3], [4, 0, 2, 1, 3], [4, 2, 0, 1, 3], [4, 2, 1, 0, 3], [4, 2, 1, 3, 0], [0, 4, 2, 3, 1], [4, 0, 2, 3, 1], [4, 2, 0, 3, 1], [4, 2, 3, 0, 1], [4, 2, 3, 1, 0], [0, 1, 4, 3, 2], [1, 0, 4, 3, 2], [1, 4, 0, 3, 2], [1, 4, 3, 0, 2], [1, 4, 3, 2, 0], [0, 4, 1, 3, 2], [4, 0, 1, 3, 2], [4, 1, 0, 3, 2], [4, 1, 3, 0, 2], [4, 1, 3, 2, 0], [0, 4, 3, 1, 2], [4, 0, 3, 1, 2], [4, 3, 0, 1, 2], [4, 3, 1, 0, 2], [4, 3, 1, 2, 0], [0, 4, 3, 2, 1], [4, 0, 3, 2, 1], [4, 3, 0, 2, 1], [4, 3, 2, 0, 1], [4, 3, 2, 1, 0]]

p_input = 5

def m(mode, value, array):
    if mode == 1:
        return value
    else: 
        return array[value]

def add_fun(a_mode, b_mode, c_mode, add1, add2, res, array):
    array[res] = m(a_mode, add1, array) + m(b_mode, add2, array)
    return array

def multi_fun(a_mode, b_mode, c_mode, add1, add2, res, array):
    array[res] = m(a_mode, add1, array) * m(b_mode, add2, array)
    return array

def less_fun(a_mode, b_mode, c_mode, add1, add2, res, array):
    if m(a_mode, add1, array) < m(b_mode, add2, array):
        array[res] = 1
    else:
        array[res] = 0
    return array

def equal_fun(a_mode, b_mode, c_mode, add1, add2, res, array):
    if m(a_mode, add1, array) == m(b_mode, add2, array):
        array[res] = 1
    else:
        array[res] = 0
    return array

def run_program(program, p_input):
    i = 0

    output = 0
    i_pos = 0

    op_code, a_mode, b_mode, c_mode = parse_cmd(program[i])
    
    while op_code != 99:     

        if op_code == 1: #add function
            program = add_fun(a_mode, b_mode, c_mode, program[i+1],program[i+2],program[i+3], program)
            i += 4

        elif op_code == 2: #multi function
            program = multi_fun(a_mode, b_mode, c_mode, program[i+1],program[i+2],program[i+3], program)
            i += 4

        elif op_code == 3: # Take Input
            program[program[i+1]] = p_input[i_pos]
            i_pos += 1
            i += 2

        elif op_code == 4: # Send Input
            o_value = m(a_mode, program[i+1], program)
            output = o_value
            i += 2

        elif op_code == 5: # Jump if true
            if m(a_mode, program[i+1], program) != 0:
                print("jump from:", i, "to: ", m(b_mode, program[i+2], program))
                i = m(b_mode, program[i+2], program)
            else: 
                i += 3

        elif op_code == 6: # Jump if false
            if m(a_mode, program[i+1], program) == 0:
                print("jump from:", i, "to: ", m(b_mode, program[i+2], program))
                i = m(b_mode, program[i+2], program)
            else: 
                i += 3

        elif op_code == 7: # less_fun
            program = less_fun(a_mode, b_mode, c_mode, program[i+1],program[i+2],program[i+3], program)
            i += 4

        elif op_code == 8: # equal_fun
            program = equal_fun(a_mode, b_mode, c_mode, program[i+1],program[i+2],program[i+3], program)
            i += 4

        else:
            print("Error at position: " + str(i))
            print("position value: " + str(op_code))
            return -1
        
        op_code, a_mode, b_mode, c_mode = parse_cmd(program[i])

def parse_cmd(cmd_str):
    cmd_arr = str(cmd_str)
    for _ in range(0,5-len(cmd_arr)):
        cmd_arr = '0' + cmd_arr

    return int(cmd_arr[-2] + cmd_arr[-1]), int(cmd_arr[-3]), int(cmd_arr[-4]), int(cmd_arr[-5])

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
    for i in range(0, 5):
    	clean = copy.copy(amp_code)
        if i == 0:
            amp_out = run_program(clean, [phase_settings[0], 0])
        else:
            amp_out = run_program(clean, [phase_settings[i], amp_out])

    return amp_out

amp_code = [3,8,1001,8,10,8,105,1,0,0,21,42,51,76,93,110,191,272,353,434,99999,3,9,1002,9,2,9,1001,9,3,9,1002,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,3,9,4,9,99,3,9,1002,9,4,9,101,5,9,9,1002,9,3,9,1001,9,4,9,1002,9,5,9,4,9,99,3,9,1002,9,5,9,101,3,9,9,102,5,9,9,4,9,99,3,9,1002,9,5,9,101,5,9,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99]

print(find_max_thruster_signal(inputs, amp_code))

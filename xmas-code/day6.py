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

    return output

def parse_cmd(cmd_str):
    cmd_arr = str(cmd_str)
    for _ in range(0,5-len(cmd_arr)):
        cmd_arr = '0' + cmd_arr
    print(''.join(cmd_arr))

    return int(cmd_arr[-2] + cmd_arr[-1]), int(cmd_arr[-3]), int(cmd_arr[-4]), int(cmd_arr[-5])

def find_max_thruster_signal(inputs, amp_comp):
    pass

def run_amps(phase_settings, amp_comp):
    
    amp_out = 0
    for i in range(0, 4):
        if i == 0:
            amp_out = run_program(amp_comp, [phase_settings[0],phase_settings[1]])
        else:
            amp_out = run_program(amp_comp, [phase_settings[i], amp_out])

    return amp_out

amp_code = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]

print(run_amps([0,1,2,3,4], amp_code))

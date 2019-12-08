test_program1 = [1,0,0,3,99]
test_program2 = [2,0,0,3,99]
test_program3 = [2,4,4,5,99,0]

mini_program = [] 
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

def run_program(program):
    i = 0
    
    op_code, a_mode, b_mode, c_mode = parse_cmd(program[i])
    
    while op_code != 99:     

        if op_code == 1: #add function
            program = add_fun(a_mode, b_mode, c_mode, program[i+1],program[i+2],program[i+3], program)
            i += 4

        elif op_code == 2: #multi function
            program = multi_fun(a_mode, b_mode, c_mode, program[i+1],program[i+2],program[i+3], program)
            i += 4

        elif op_code == 3: # Take Input
            program[program[i+1]] = p_input
            i += 2

        elif op_code == 4: # Send Input
            print("output: ", m(a_mode, program[i+1], program))
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

    return program

def parse_cmd(cmd_str):
    cmd_arr = str(cmd_str)
    for _ in range(0,5-len(cmd_arr)):
        cmd_arr = '0' + cmd_arr
    print(''.join(cmd_arr))

    return int(cmd_arr[-2] + cmd_arr[-1]), int(cmd_arr[-3]), int(cmd_arr[-4]), int(cmd_arr[-5])

def find_verb_noun():
    verb = 0
    noun = 0

print(run_program([3,225,1,225,6,6,1100,1,238,225,104,0,1002,114,46,224,1001,224,-736,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,1,166,195,224,1001,224,-137,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1001,169,83,224,1001,224,-90,224,4,224,102,8,223,223,1001,224,2,224,1,224,223,223,101,44,117,224,101,-131,224,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1101,80,17,225,1101,56,51,225,1101,78,89,225,1102,48,16,225,1101,87,78,225,1102,34,33,224,101,-1122,224,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,1101,66,53,224,101,-119,224,224,4,224,102,8,223,223,1001,224,5,224,1,223,224,223,1102,51,49,225,1101,7,15,225,2,110,106,224,1001,224,-4539,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1102,88,78,225,102,78,101,224,101,-6240,224,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1107,226,677,224,102,2,223,223,1006,224,329,101,1,223,223,1108,226,677,224,1002,223,2,223,1005,224,344,101,1,223,223,8,226,677,224,102,2,223,223,1006,224,359,1001,223,1,223,1007,226,677,224,1002,223,2,223,1005,224,374,101,1,223,223,1008,677,677,224,1002,223,2,223,1005,224,389,1001,223,1,223,1108,677,226,224,1002,223,2,223,1006,224,404,1001,223,1,223,1007,226,226,224,1002,223,2,223,1005,224,419,1001,223,1,223,1107,677,226,224,1002,223,2,223,1006,224,434,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,449,1001,223,1,223,1107,677,677,224,102,2,223,223,1005,224,464,1001,223,1,223,108,226,226,224,1002,223,2,223,1006,224,479,1001,223,1,223,1008,226,226,224,102,2,223,223,1005,224,494,101,1,223,223,108,677,226,224,102,2,223,223,1005,224,509,1001,223,1,223,8,677,226,224,1002,223,2,223,1006,224,524,101,1,223,223,7,226,677,224,1002,223,2,223,1006,224,539,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,554,1001,223,1,223,7,226,226,224,1002,223,2,223,1006,224,569,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,584,101,1,223,223,1108,677,677,224,102,2,223,223,1006,224,599,1001,223,1,223,1008,677,226,224,1002,223,2,223,1005,224,614,1001,223,1,223,8,677,677,224,1002,223,2,223,1006,224,629,1001,223,1,223,107,226,677,224,1002,223,2,223,1006,224,644,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,659,101,1,223,223,107,226,226,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226]))

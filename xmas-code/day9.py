inputs = [[0, 1, 2, 3, 4], [1, 0, 2, 3, 4], [1, 2, 0, 3, 4], [1, 2, 3, 0, 4], [1, 2, 3, 4, 0], [0, 2, 1, 3, 4], [2, 0, 1, 3, 4], [2, 1, 0, 3, 4], [2, 1, 3, 0, 4], [2, 1, 3, 4, 0], [0, 2, 3, 1, 4], [2, 0, 3, 1, 4], [2, 3, 0, 1, 4], [2, 3, 1, 0, 4], [2, 3, 1, 4, 0], [0, 2, 3, 4, 1], [2, 0, 3, 4, 1], [2, 3, 0, 4, 1], [2, 3, 4, 0, 1], [2, 3, 4, 1, 0], [0, 1, 3, 2, 4], [1, 0, 3, 2, 4], [1, 3, 0, 2, 4], [1, 3, 2, 0, 4], [1, 3, 2, 4, 0], [0, 3, 1, 2, 4], [3, 0, 1, 2, 4], [3, 1, 0, 2, 4], [3, 1, 2, 0, 4], [3, 1, 2, 4, 0], [0, 3, 2, 1, 4], [3, 0, 2, 1, 4], [3, 2, 0, 1, 4], [3, 2, 1, 0, 4], [3, 2, 1, 4, 0], [0, 3, 2, 4, 1], [3, 0, 2, 4, 1], [3, 2, 0, 4, 1], [3, 2, 4, 0, 1], [3, 2, 4, 1, 0], [0, 1, 3, 4, 2], [1, 0, 3, 4, 2], [1, 3, 0, 4, 2], [1, 3, 4, 0, 2], [1, 3, 4, 2, 0], [0, 3, 1, 4, 2], [3, 0, 1, 4, 2], [3, 1, 0, 4, 2], [3, 1, 4, 0, 2], [3, 1, 4, 2, 0], [0, 3, 4, 1, 2], [3, 0, 4, 1, 2], [3, 4, 0, 1, 2], [3, 4, 1, 0, 2], [3, 4, 1, 2, 0], [0, 3, 4, 2, 1], [3, 0, 4, 2, 1], [3, 4, 0, 2, 1], [3, 4, 2, 0, 1], [3, 4, 2, 1, 0], [0, 1, 2, 4, 3], [1, 0, 2, 4, 3], [1, 2, 0, 4, 3], [1, 2, 4, 0, 3], [1, 2, 4, 3, 0], [0, 2, 1, 4, 3], [2, 0, 1, 4, 3], [2, 1, 0, 4, 3], [2, 1, 4, 0, 3], [2, 1, 4, 3, 0], [0, 2, 4, 1, 3], [2, 0, 4, 1, 3], [2, 4, 0, 1, 3], [2, 4, 1, 0, 3], [2, 4, 1, 3, 0], [0, 2, 4, 3, 1], [2, 0, 4, 3, 1], [2, 4, 0, 3, 1], [2, 4, 3, 0, 1], [2, 4, 3, 1, 0], [0, 1, 4, 2, 3], [1, 0, 4, 2, 3], [1, 4, 0, 2, 3], [1, 4, 2, 0, 3], [1, 4, 2, 3, 0], [0, 4, 1, 2, 3], [4, 0, 1, 2, 3], [4, 1, 0, 2, 3], [4, 1, 2, 0, 3], [4, 1, 2, 3, 0], [0, 4, 2, 1, 3], [4, 0, 2, 1, 3], [4, 2, 0, 1, 3], [4, 2, 1, 0, 3], [4, 2, 1, 3, 0], [0, 4, 2, 3, 1], [4, 0, 2, 3, 1], [4, 2, 0, 3, 1], [4, 2, 3, 0, 1], [4, 2, 3, 1, 0], [0, 1, 4, 3, 2], [1, 0, 4, 3, 2], [1, 4, 0, 3, 2], [1, 4, 3, 0, 2], [1, 4, 3, 2, 0], [0, 4, 1, 3, 2], [4, 0, 1, 3, 2], [4, 1, 0, 3, 2], [4, 1, 3, 0, 2], [4, 1, 3, 2, 0], [0, 4, 3, 1, 2], [4, 0, 3, 1, 2], [4, 3, 0, 1, 2], [4, 3, 1, 0, 2], [4, 3, 1, 2, 0], [0, 4, 3, 2, 1], [4, 0, 3, 2, 1], [4, 3, 0, 2, 1], [4, 3, 2, 0, 1], [4, 3, 2, 1, 0]]

p_input = 2
relative_base = 0

def m(mode, value, array, r_base):
    if mode == 1:
        return value
    elif mode == 2:
        return array[r_base + value]
    else: 
        return array[value]

def r(mode, value, r_base):
    if mode == 2:
        return r_base + value
    else: 
        return value

def add_fun(a_mode, b_mode, c_mode, add1, add2, res, array, r_base):
    array[r(c_mode, res, r_base)] = m(a_mode, add1, array, r_base) + m(b_mode, add2, array, r_base)
    return array

def multi_fun(a_mode, b_mode, c_mode, add1, add2, res, array, r_base):
    array[r(c_mode, res, r_base)] = m(a_mode, add1, array, r_base) * m(b_mode, add2, array, r_base)
    return array

def less_fun(a_mode, b_mode, c_mode, add1, add2, res, array, r_base):
    if m(a_mode, add1, array, r_base) < m(b_mode, add2, array, r_base):
        array[r(c_mode, res, r_base)] = 1
    else:
        array[r(c_mode, res, r_base)] = 0
    return array

def equal_fun(a_mode, b_mode, c_mode, add1, add2, res, array, r_base):
    if m(a_mode, add1, array, r_base) == m(b_mode, add2, array, r_base):
        array[r(c_mode, res, r_base)] = 1
    else:
        array[r(c_mode, res, r_base)] = 0
    return array

def run_program(program, p_input):
    i = 0

    output = 0
    i_pos = 0
    r_base = 0

    op_code, a_mode, b_mode, c_mode = parse_cmd(program[i])
    
    while op_code != 99:     

        if op_code == 1: #add function
            program = add_fun(a_mode, b_mode, c_mode, program[i+1],program[i+2],program[i+3], program, r_base)
            i += 4

        elif op_code == 2: #multi function
            program = multi_fun(a_mode, b_mode, c_mode, program[i+1],program[i+2],program[i+3], program, r_base)
            i += 4

        elif op_code == 3: # Take Input
            program[r(a_mode, program[i+1], r_base)] = p_input
            i += 2

        elif op_code == 4: # Send Input
            o_value = m(a_mode, program[i+1], program, r_base)
            print(o_value)
            i += 2

        elif op_code == 5: # Jump if true
            if m(a_mode, program[i+1], program, r_base) != 0:
                #print("jump from:", i, "to: ", m(b_mode, program[i+2], program, r_base))
                i = m(b_mode, program[i+2], program, r_base)
            else: 
                i += 3

        elif op_code == 6: # Jump if false
            if m(a_mode, program[i+1], program, r_base) == 0:
                #print("jump from:", i, "to: ", m(b_mode, program[i+2], program, r_base))
                i = m(b_mode, program[i+2], program, r_base)
            else: 
                i += 3

        elif op_code == 7: # less_fun
            program = less_fun(a_mode, b_mode, c_mode, program[i+1],program[i+2],program[i+3], program, r_base)
            i += 4

        elif op_code == 8: # equal_fun
            program = equal_fun(a_mode, b_mode, c_mode, program[i+1],program[i+2],program[i+3], program, r_base)
            i += 4

        elif op_code == 9: # relative base change
            r_base += m(a_mode, program[i+1], program, r_base)
            print("base change to:", r_base)
            i += 2

        else:
            print("Error at position: " + str(i))
            print("position value: " + str(op_code))
            return -1
        
        op_code, a_mode, b_mode, c_mode = parse_cmd(program[i])

    #return program

def parse_cmd(cmd_str):
    cmd_arr = str(cmd_str)
    for _ in range(0,5-len(cmd_arr)):
        cmd_arr = '0' + cmd_arr
    #print(''.join(cmd_arr))

    return int(cmd_arr[-2] + cmd_arr[-1]), int(cmd_arr[-3]), int(cmd_arr[-4]), int(cmd_arr[-5])

code = [1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1101,3,0,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1102,1,31,1018,1102,352,1,1023,1101,0,1,1021,1101,0,33,1003,1102,1,36,1007,1102,21,1,1005,1101,359,0,1022,1101,0,787,1024,1102,1,24,1011,1101,30,0,1014,1101,22,0,1016,1101,0,0,1020,1102,1,29,1000,1101,778,0,1025,1102,23,1,1017,1102,1,28,1002,1101,38,0,1019,1102,1,27,1013,1102,1,32,1012,1101,0,37,1006,1101,444,0,1027,1102,1,20,1009,1101,0,447,1026,1101,0,39,1008,1101,35,0,1010,1102,559,1,1028,1102,26,1,1004,1102,1,25,1015,1102,1,34,1001,1101,0,554,1029,109,-3,2101,0,9,63,1008,63,34,63,1005,63,205,1001,64,1,64,1105,1,207,4,187,1002,64,2,64,109,23,21107,40,39,-7,1005,1013,227,1001,64,1,64,1106,0,229,4,213,1002,64,2,64,109,-17,1202,-2,1,63,1008,63,36,63,1005,63,249,1106,0,255,4,235,1001,64,1,64,1002,64,2,64,109,-6,1202,10,1,63,1008,63,36,63,1005,63,277,4,261,1106,0,281,1001,64,1,64,1002,64,2,64,109,-2,1208,9,26,63,1005,63,303,4,287,1001,64,1,64,1106,0,303,1002,64,2,64,109,32,1206,-7,321,4,309,1001,64,1,64,1106,0,321,1002,64,2,64,109,-29,1207,7,20,63,1005,63,337,1105,1,343,4,327,1001,64,1,64,1002,64,2,64,109,27,2105,1,-2,1001,64,1,64,1106,0,361,4,349,1002,64,2,64,109,-25,2108,39,7,63,1005,63,377,1106,0,383,4,367,1001,64,1,64,1002,64,2,64,109,1,1201,6,0,63,1008,63,36,63,1005,63,409,4,389,1001,64,1,64,1105,1,409,1002,64,2,64,109,1,2102,1,1,63,1008,63,33,63,1005,63,435,4,415,1001,64,1,64,1105,1,435,1002,64,2,64,109,28,2106,0,-3,1106,0,453,4,441,1001,64,1,64,1002,64,2,64,109,-13,21101,41,0,1,1008,1018,44,63,1005,63,477,1001,64,1,64,1106,0,479,4,459,1002,64,2,64,109,4,21108,42,42,-2,1005,1019,501,4,485,1001,64,1,64,1106,0,501,1002,64,2,64,109,-21,2101,0,2,63,1008,63,28,63,1005,63,523,4,507,1105,1,527,1001,64,1,64,1002,64,2,64,109,26,1205,-5,545,4,533,1001,64,1,64,1105,1,545,1002,64,2,64,109,3,2106,0,-1,4,551,1106,0,563,1001,64,1,64,1002,64,2,64,109,-33,1201,4,0,63,1008,63,28,63,1005,63,583,1105,1,589,4,569,1001,64,1,64,1002,64,2,64,109,11,2107,27,-3,63,1005,63,609,1001,64,1,64,1106,0,611,4,595,1002,64,2,64,109,8,21102,43,1,3,1008,1018,43,63,1005,63,637,4,617,1001,64,1,64,1105,1,637,1002,64,2,64,109,-5,21108,44,41,0,1005,1010,653,1105,1,659,4,643,1001,64,1,64,1002,64,2,64,109,-13,2108,21,8,63,1005,63,681,4,665,1001,64,1,64,1106,0,681,1002,64,2,64,109,6,1207,0,34,63,1005,63,703,4,687,1001,64,1,64,1105,1,703,1002,64,2,64,109,7,1208,-7,35,63,1005,63,723,1001,64,1,64,1106,0,725,4,709,1002,64,2,64,109,-13,2102,1,7,63,1008,63,23,63,1005,63,745,1105,1,751,4,731,1001,64,1,64,1002,64,2,64,109,13,1205,10,767,1001,64,1,64,1105,1,769,4,757,1002,64,2,64,109,14,2105,1,0,4,775,1001,64,1,64,1106,0,787,1002,64,2,64,109,-20,21107,45,46,7,1005,1011,809,4,793,1001,64,1,64,1105,1,809,1002,64,2,64,109,-3,2107,25,3,63,1005,63,827,4,815,1106,0,831,1001,64,1,64,1002,64,2,64,109,13,1206,7,847,1001,64,1,64,1106,0,849,4,837,1002,64,2,64,109,-11,21101,46,0,7,1008,1010,46,63,1005,63,871,4,855,1106,0,875,1001,64,1,64,1002,64,2,64,109,15,21102,47,1,-4,1008,1014,48,63,1005,63,895,1106,0,901,4,881,1001,64,1,64,4,64,99,21102,27,1,1,21101,0,915,0,1106,0,922,21201,1,63208,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21102,1,942,0,1106,0,922,21202,1,1,-1,21201,-2,-3,1,21101,957,0,0,1105,1,922,22201,1,-1,-2,1106,0,968,21201,-2,0,-2,109,-3,2106,0,0] + ([0] * 10000)

run_program(code, p_input)

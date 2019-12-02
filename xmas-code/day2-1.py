test_program1 = [1,0,0,3,99]
test_program2 = [2,0,0,3,99]
test_program3 = [2,4,4,5,99,0]

mini_program = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,2,19,6,23,1,23,5,27,1,9,27,31,1,31,10,35,2,35,9,39,1,5,39,43,2,43,9,47,1,5,47,51,2,51,13,55,1,55,10,59,1,59,10,63,2,9,63,67,1,67,5,71,2,13,71,75,1,75,10,79,1,79,6,83,2,13,83,87,1,87,6,91,1,6,91,95,1,10,95,99,2,99,6,103,1,103,5,107,2,6,107,111,1,10,111,115,1,115,5,119,2,6,119,123,1,123,5,127,2,127,6,131,1,131,5,135,1,2,135,139,1,139,13,0,99,2,0,14,0]

def add_fun(add1, add2, res, array):
    array[res] = array[add1] + array[add2]
    return array

def multi_fun(add1, add2, res, array):
    array[res] = array[add1] * array[add2]
    return array

def run_program(program):
    i = 0

    while program[i] != 99:     
        if program[i] == 1: #add function
            program = add_fun(program[i+1],program[i+2],program[i+3], program)
        elif program[i] == 2: #multi function
            program = multi_fun(program[i+1],program[i+2],program[i+3], program)
        else:
            print("Error at position: " + str(i))
            print("position value: " + str(program[i]))
            return -1
        i += 4

    return program

print(run_program(mini_program))
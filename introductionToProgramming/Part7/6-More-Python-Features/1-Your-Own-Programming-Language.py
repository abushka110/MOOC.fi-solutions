# solution
def run(program: list):
    output_result = []
    # dict to store variables value
    variables_dict = {}
    jump_point = ""
    for command_full in program:
        allowed_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # function to change variable value
        if "MOV" in command_full:
            # check if the value to assign is number or other variable
            if command_full[6:].isdigit():
                variables_dict[command_full[4]] = int(command_full[6:])
            elif command_full[6:] in variables_dict:
                variables_dict[command_full[4]] = variables_dict[command_full[6:]]
        # function to add two numbers
        elif "ADD" in command_full:
            if command_full[6] in allowed_characters:
                variables_dict[command_full[4]] += variables_dict[command_full[6]]
            else:
                variables_dict[command_full[4]] += int(command_full[6:])
        # function to subtraction two numbers
        elif "SUB" in command_full:
            if command_full[6] in allowed_characters:
                variables_dict[command_full[4]] -= variables_dict[command_full[6]]
            else:
                variables_dict[command_full[4]] -= int(command_full[6:])
        # function to multiplicate two numbers
        elif "MUL" in command_full:
            if command_full[6] in allowed_characters:
                variables_dict[command_full[4]] *= variables_dict[command_full[6]]
            else:
                variables_dict[command_full[4]] *= int(command_full[6:])
        # function to print variable value
        elif "PRINT" in command_full:
            if command_full[6] in variables_dict:
                output_result.append(variables_dict[command_full[6:]])
            else:
                output_result.append(0)
        elif "END" in command_full:
            break

    return output_result

# test
if __name__ == "__main__":
    # test 1 - expected output [1, 2, 3]
    print("Test 1")
    program1 = []
    program1.append("MOV A 1")
    program1.append("MOV B 2")
    program1.append("PRINT A")
    program1.append("PRINT B")
    program1.append("ADD A B")
    program1.append("PRINT A")
    program1.append("END")
    result = run(program1)
    print(result)
    
    # test 2 - expected output [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
    print("Test 2")
    program2 = []
    program2.append("MOV A 1")
    program2.append("MOV B 10")
    program2.append("begin:")
    program2.append("IF A >= B JUMP quit")
    program2.append("PRINT A")
    program2.append("PRINT B")
    program2.append("ADD A 1")
    program2.append("SUB B 1")
    program2.append("JUMP begin")
    program2.append("quit:")
    program2.append("END")
    result = run(program2)
    print(result)

    # test 3
    print("TEST 3")
    program3 = ['MOV A 5', 'PRINT A']
    result = run(program3)
    print(result)

    # test 4
    print("TEST 4")
    program4 = ['MOV A 10', 'PRINT A', 'MOV B A', 'SUB B 8', 'PRINT B', 'SUB A B', 'PRINT A'] 
    result = run(program4)
    print(result)
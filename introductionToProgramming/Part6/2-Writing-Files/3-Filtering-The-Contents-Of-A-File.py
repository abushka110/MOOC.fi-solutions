# solution
def filter_solutions():
    # open all files
    with open("solutions.csv") as file, open("correct.csv", "w") as correct_file, open("incorrect.csv", "w") as incorrect_file:
        for line in file:
            # split into pieces
            pieces = line.split(";")
            calculation = pieces[1]
            result = pieces[2]
            # eval function calculate string expression
            if eval(calculation) == int(result):
                correct_file.write(line)
            else:
                incorrect_file.write(line)

# model solution
# def filter_solutions():
#     # Open all lines
#     with open("solutions.csv") as source, open("correct.csv", "w") as correct_file, open("incorrect.csv", "w") as incorrect_file:
#         for row in source:
#             # Split into pieces
#             pieces = row.split(";")
 
#             calculation = pieces[1]
#             result = pieces[2]
 
#             # Addition or subtraction?
#             if "+" in calculation:
#                 operands = calculation.split("+")
#                 # correct is True or False based on whether the calculation was correct or not
#                 correct = int(operands[0]) + int(operands[1]) == int(result)
#             else:
#                 operands = calculation.split("-")
#                 # correct is True or False based on whether the calculation was correct or not
#                 correct = int(operands[0]) - int(operands[1]) == int(result)
 
#             # Write to file
#             if correct:
#                 correct_file.write(row)
#             else:
#                 incorrect_file.write(row)

filter_solutions()
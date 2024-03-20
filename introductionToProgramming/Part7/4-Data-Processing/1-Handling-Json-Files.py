# # solution 1
# import json

# def print_persons(filename: str):
#     with open(filename) as students_info_file:
#         data = students_info_file.read()
    
#     students = json.loads(data)
#     for student in students:
#         student_name = student["name"]
#         student_age = student["age"]
#         print(f"{student_name} {student_age} years (", end="")
#         index = 1
#         for hobby in student["hobbies"]:
#             if index == len(student["hobbies"]):
#                 print(f"{hobby}", end = "")
#             else:
#                 print(f"{hobby}, ", end = "")
#                 index += 1
#         print(")")

# model solution
import json

def print_persons(filename: str):
    with open(filename) as students_info_file:
        data = students_info_file.read()
    
    students = json.loads(data)
    for student in students:
        student_name = student["name"]
        student_age = student["age"]
        student_hobbies = ", ".join(student['hobbies'])
        print(f"{student_name} {student_age} years ({student_hobbies})")

# test
if __name__ == "__main__":
    print_persons("students.json")


# Peter Pythons 27 years (coding, knitting)
# Jean Javanese 24 years (coding, rock climbing, reading)
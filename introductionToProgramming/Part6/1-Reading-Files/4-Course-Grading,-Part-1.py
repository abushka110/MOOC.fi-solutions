# solution
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

students = {}    
with open(student_info) as students_file:
    for line in students_file:
        items = line.split(";")
        if items[0] == "id":
            continue
        students[items[0]] = f"{items[1]} {items[2].strip()}"

exercises = {}
with open(exercise_data) as exercises_file:
    for line in exercises_file:
        items = line.split(";")
        if items[0] == "id":
            continue
        esum = 0
        for i in range(1, len(items)):
            esum += int(items[i])
        exercises[items[0]] = esum

for id, name in students.items():
    print(name, exercises[id])

# solution
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
students = {}
    
with open(student_info) as students_file:
    for line in students_file:
        items = line.split(";")
        if items[0] == "id":
            continue
        full_name = items[1] + " " + items[2].strip()
        students[items[0]] = full_name

grades = {}
with open(exercise_data) as exercises_file:
    for line in exercises_file:
        items = line.split(";")
        if items[0] == "id":
            continue
        sum = 0
        for i in range(1, len(items)):
            sum += int(items[i])
        grades[items[0]] = sum

for id, name in students.items():
    print(name, grades[id])

# solution
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")

students = {}
with open(student_info) as students_file:
    for line in students_file:
        items = line.split(";")
        if items[0] == "id":
            continue
        students[items[0]] = f"{items[1]} {items[2].strip()}"

exercise_point = {}
with open(exercise_data) as exercises_file:
    for line in exercises_file:
        items = line.split(";")
        if items[0] == "id":
            continue
        sum = 0
        for i in range(1, len(items)):
            sum += int(items[i])
        exercise_point[items[0]] = int(sum // 4)

grades_points = {}
with open(exam_points) as exam_file:
    for line in exam_file:        
        items = line.split(";")
        if items[0] == "id":
            continue
        grade_sum = 0
        for i in range(1, len(items)):
            grade_sum += int(items[i])
        grades_points[items[0]] = grade_sum

total_points = {}
for id, name in students.items():
    point = 0
    points_sum = exercise_point[id] + grades_points[id]
    limits = [15, 18, 21, 24, 28]
    while point < 5 and points_sum >= limits[point]:
        point += 1
    total_points[id] = point

for id, name in students.items():
    print(name, total_points[id])

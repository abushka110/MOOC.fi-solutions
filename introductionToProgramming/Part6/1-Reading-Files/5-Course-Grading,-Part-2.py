# solution
# if False:
#     # this is never executed
#     student_info = input("Student information: ")
#     exercise_data = input("Exercises completed: ")
#     exam_points = input("Exam points: ")
# else:
#     # hard-coded input
#     student_info = "students1.csv"
#     exercise_data = "exercises1.csv"
#     exam_points = "exam_points1.csv"

student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")

students = {}
    
with open(student_info) as students_file:
    for line in students_file:
        items = line.split(";")
        if items[0] == "id":
            continue
        full_name = items[1] + " " + items[2].strip()
        students[items[0]] = full_name

exercise_point = {}
with open(exercise_data) as exercises_file:
    for line in exercises_file:
        items = line.split(";")
        if items[0] == "id":
            continue
        sum = 0
        for i in range(1, len(items)):
            sum += int(items[i])
        exercise_point[items[0]] = int(sum / 40 * 10)

grades_points = {}
with open(exam_points) as exam_file:
    for line in exam_file:
        line = line.replace("\n", "")
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
    if points_sum <= 14:
        point = 0
    elif 14 < points_sum <= 17:
        point = 1
    elif 17 < points_sum <= 20:
        point = 2
    elif 20 < points_sum <= 23:
        point = 3
    elif 23 < points_sum <= 27:
        point = 4
    elif points_sum > 27:
        point = 5
    total_points[id] = point

for id, name in students.items():
    print(name, total_points[id])

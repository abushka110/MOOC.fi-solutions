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
exercise_count = {}
with open(exercise_data) as exercises_file:
    for line in exercises_file:
        items = line.split(";")
        if items[0] == "id":
            continue
        sum = 0
        for i in range(1, len(items)):
            sum += int(items[i])
        exercise_count[items[0]] = int(sum)
        exercise_point[items[0]] = int(sum / 40 * 10)

exam_points_list = {}
with open(exam_points) as exam_file:
    for line in exam_file:
        line = line.replace("\n", "")
        items = line.split(";")
        if items[0] == "id":
            continue
        grade_sum = 0
        for i in range(1, len(items)):
            grade_sum += int(items[i])
        exam_points_list[items[0]] = grade_sum

grade_points = {}
total_points = {}
for id, name in students.items():
    point = 0
    points_sum = exercise_point[id] + exam_points_list[id]
    total_points[id] = points_sum
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
    grade_points[id] = point

print("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade")
for id, name in students.items():
    print(f"{name:30}{exercise_count[id]:<10}{exercise_point[id]:<10}{exam_points_list[id]:<10}{total_points[id]:<10}{grade_points[id]:<10}")

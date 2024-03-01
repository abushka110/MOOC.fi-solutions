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
    limits = [15, 18, 21, 24, 28]
    while point < 5 and points_sum >= limits[point]:
        point += 1
    grade_points[id] = point

print("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade")
for id, name in students.items():
    print(f"{name:30}{exercise_count[id]:<10}{exercise_point[id]:<10}{exam_points_list[id]:<10}{total_points[id]:<10}{grade_points[id]:<10}")

# solution
# read file names
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")
course_info = input("Course information: ")

# create dictionary for students name with id for key
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

with open("results.txt", "w") as results_txt, open("results.csv", "w") as results_csv, open(course_info) as course_info_file:
    course_name_write = ""
    study_credits_write = ""
    for line in course_info_file:
        line = line.replace("\n", "")
        if course_name_write == "":
            line =line.replace("name: ", "")
            course_name_write = line
        else:
            line = line.replace("study credits: ", "")
            study_credits_write = line
    results_txt.write(f"{course_name_write}, {study_credits_write} credits\n")
    for id, name in students.items():
        results_txt.write("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade")
        write_str = f"{name:30}{exercise_count[id]:<10}{exercise_point[id]:<10}{exam_points_list[id]:<10}{total_points[id]:<10}{grade_points[id]:<10}"
        results_txt.write(write_str + "\n")
        results_csv.write(f"{id};{name};{grade_points[id]:<10}\n")
print("Results written to files results.txt and results.csv")
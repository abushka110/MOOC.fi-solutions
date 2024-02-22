# solution
# add student to database
def add_student(database: dict, name: str):
    database[name] = ""

# Print information about a student, including completed courses and average grade.
def print_student(database, name):
    if name in database:
        print(f"{name}:")
        if database[name] == "":
            print(" no completed courses")
        else:
            print(f" {len(database[name])} completed courses:")
            average = 0
            for course in database[name]:
                average += course[1]
                print(f"  {course[0]} {course[1]}")
            average = average / len(database[name])
            print(f" average grade {average:.1f}")
    else:
        print(f"{name}: no such person in the database")

# add course that student completed
def add_course(database, name, course):
    # check if student already has the course
    current_course = ()
    for course_in_database in database[name]:
        if course_in_database[0] == course[0]:
            current_course = course_in_database[:]
    # add course if it doesn't exist already
    if current_course == () and course[1] != 0:
        if database[name] == "":
            database[name] = [course]
        else:
            database[name].append(course)
    # add course if it already exists but the new grade is higher
    if current_course:
        if current_course[1] < course[1]:
            database[name].remove(current_course)
            database[name].append(course)

# summary function
# Print a summary of the database, including the number of students,
# the student with the most completed courses,
# and the student with the best average grade.
def summary(database):
    # count students
    students_count = len(database)
    print(f"students {students_count}")
    
    # find which student has the most completed courses
    most_courses = 0
    most_courses_student = ""
    for name in database:
        if most_courses < len(database[name]):
            most_courses = len(database[name])
            most_courses_student = name
    print(f"most courses completed {most_courses} {most_courses_student}")

    # calculate the best average grade
    best_ave_grade = 0
    best_ave_grade_student = ""
    for name in database:
        temp_average_grade = 0
        for course in database[name]:
            temp_average_grade += course[1]
        temp_average_grade /= len(database[name])
        if best_ave_grade < temp_average_grade:
            best_ave_grade = temp_average_grade
            best_ave_grade_student = name
    print(f"best average grade {best_ave_grade} {best_ave_grade_student}")

# test
if __name__ == "__main__":
    # test 1
    # students = {}
    # add_student(students, "Peter")
    # add_course(students, "Peter", ("Introduction to Programming", 3))
    # add_course(students, "Peter", ("Advanced Course in Programming", 2))
    # add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    # add_course(students, "Peter", ("Introduction to Programming", 2))
    # print_student(students, "Peter")

    # test 2
    # students = {}
    # add_student(students, "Peter")
    # add_course(students, "Peter", ("Software Development Methods", 5))
    # add_course(students, "Peter", ("Software Development Methods", 1))
    # print_student(students, "Peter")

    # test 3
    # students = {}
    # add_student(students, "Peter")
    # add_course(students, "Peter", ("Software Development Methods", 1))
    # add_course(students, "Peter", ("Software Development Methods", 5))
    # print_student(students, "Peter")

    # test 4
    # students = {}
    # add_student(students, "Peter")
    # add_student(students, "Eliza")
    # add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    # add_course(students, "Peter", ("Introduction to Programming", 1))
    # add_course(students, "Peter", ("Advanced Course in Programming", 1))
    # add_course(students, "Eliza", ("Introduction to Programming", 5))
    # add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    # summary(students)

    # test 5
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    summary(students)
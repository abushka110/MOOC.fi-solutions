# solution
# function that ask points and exercices
def askPoint():
    exam_Exercices = input("Exam points and exercices completed: ")
    
    # lists for points
    exam_Points = []
    exercices_Points = []

    # keep asking untill user input is nothing (press "Enter")
    while exam_Exercices != "":
        exam_Points.append(int(exam_Exercices[:2]))
        exercices_Points.append(int(exam_Exercices[3:]))
        exam_Exercices = input("Exam points and exercices completed: ")

    total_points = points_total(exam_Points, exercices_Points)
    grades_list = points_to_grades(total_points)
    print("Statistics:")
    print(f"Points average: {points_average(total_points)}")
    print(f"Pass percentage: {pass_percentage(grades_list)}")

    print("Grade distribution: ")
    for i in reversed(range(6)):
        print(f"  {i}:", "*" * grades_list.count(i))

# 
def points_total(exam_points: list, exercices_points: list):
    # convert exercices points to granted points
    granted_points = []
    for item in exercices_points:
        item = item / 10
        granted_points.append(int(item))

    # add exam points to granted points
    exam_plus_granted = []
    for item1, item2 in zip(exam_points, granted_points):
        if item1 < 10:
            exam_plus_granted.append(0)
        else:
            exam_plus_granted.append(item1 + item2)
    
    return exam_plus_granted

# function to convert points to grades
def points_to_grades(exam_plus_granted: list):
    grades = []
    for x in range(len(exam_plus_granted)):
        if exam_plus_granted[x] >= 28:
            grades.append(5)
        elif exam_plus_granted[x] >= 24:
            grades.append(4)
        elif exam_plus_granted[x] >= 21:
            grades.append(3)
        elif exam_plus_granted[x] >= 18:
            grades.append(2)
        elif exam_plus_granted[x] >= 15:
            grades.append(1)
        else:
            grades.append(0)  
    return grades

def points_average(grades):
    return sum(grades) / len(grades) 

def pass_percentage(grades: list):
    temp = len(grades) - grades.count(0)
    return temp * 100 / len(grades)

# test
askPoint()
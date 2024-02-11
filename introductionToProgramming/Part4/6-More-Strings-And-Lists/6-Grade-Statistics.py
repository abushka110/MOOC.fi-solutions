# solution
# function that ask points and exercises
# points and exercises are added to lists
# stop when user input is nothing (press "Enter")
# then print out statistics
def askPoint():
    examExercisesInput = input("Exam points and exercises completed: ")

    examExercisesList = []
    while examExercisesInput != "":
        examExercisesList.append(examExercisesInput)
        examExercisesInput = input("Exam points and exercises completed: ")

    pointsList = []
    exercisesList = []
    for pointsExercises in examExercisesList:
        pointsList.append(int(pointsExercises[:2]))
        exercisesList.append(int(pointsExercises[3:]))

    print("Statistics:")

    # function that calculate GrantedPoints
    grantedPointsList = []
    for item in exercisesList:
        item = item / 10
        grantedPointsList.append(int(item))
    # grantedPointsList = exerciseGrantedPoints(exercisesList)

    # function that calculate grade
    # grade = exam points + exercise points
    pointsPlusExercisesPointsList = []
    for item1, item2 in zip(pointsList, grantedPointsList):
        pointsPlusExercisesPointsList.append(item1 + item2)

    resultList = []
    for x in range(len(pointsPlusExercisesPointsList)):
        if pointsPlusExercisesPointsList[x] >= 0 and pointsPlusExercisesPointsList[x] <= 14 or pointsList[x] < 10:
            resultList.append(0)
        elif pointsPlusExercisesPointsList[x] >= 15 and pointsPlusExercisesPointsList[x] <= 17:
            resultList.append(1)
        elif pointsPlusExercisesPointsList[x] >= 18 and pointsPlusExercisesPointsList[x] <= 20:
            resultList.append(2)
        elif pointsPlusExercisesPointsList[x] >= 21 and pointsPlusExercisesPointsList[x] <= 23:
            resultList.append(3)
        elif pointsPlusExercisesPointsList[x] >= 24 and pointsPlusExercisesPointsList[x] <= 27:
            resultList.append(4)
        elif pointsPlusExercisesPointsList[x] >= 28 and pointsPlusExercisesPointsList[x] <= 30:
            resultList.append(5)
    # 

    # function for statistics
    # passedGrades = []
    # for grade in grades:
    #     if grade >= 10:
    #         passedGrades.append(grade)
    temp = len(resultList) - resultList.count(0)
    passPercentage = temp * 100 / len(resultList)
    averagePoints = sum(pointsPlusExercisesPointsList) / len(pointsPlusExercisesPointsList)
    print(f"Points average: {averagePoints}")
    print(f"Pass percentage: {passPercentage}")
    print("Grade distribution:")
    for i in reversed(range(6)):
        print(f"  {i}:", "*" * resultList.count(i))
    # stats(resultList)

# test
askPoint()
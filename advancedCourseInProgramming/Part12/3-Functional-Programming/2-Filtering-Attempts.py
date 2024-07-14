class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

# solution
def accepted(attempts: list):
    return list(filter(lambda attempt: attempt.grade > 0, attempts))

def attempts_with_grade(attempts: list, grade: int):
    return list(filter(lambda attempt: attempt.grade == grade, attempts))

def passed_students(attempts: list, course: str):
    attempts_passed = list(filter(lambda attempt: attempt.course_name == course and attempt.grade > 0, attempts))
    return sorted(list(map(lambda attempt: attempt.student_name, attempts_passed)))

# test
if __name__ == "__main__":
    print("TEST 1")
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 0)
    for attempt in accepted([s1, s2, s3]):
        print(attempt)
    # expected output:
    # Peter Python, grade for the course Introduction to Programming 3
    # Olivia C. Objective grade for the course Introduction to Programming 5

    print()

    print("TEST 2")
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Introduction to AI", 3)
    s4 = CourseAttempt("Olivia C. Objective", "Data Structures and Algorithms", 3)
    for attempt in attempts_with_grade([s1, s2, s3, s4], 3):
        print(attempt)
    # expected output:
    # Peter Python, grade for the course Introduction to Programming 3
    # Peter Python, grade for the course Introduction to AI 3
    # Olivia C. Objective, grade for the course Data Structures and Algorithms 3

    print()

    print("TEST 3")
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to AI", 5)
    s3 = CourseAttempt("Peter Python", "Introduction to AI", 0)
    s4 = CourseAttempt("Jack Java", "Introduction to AI", 3)
    for attempt in passed_students([s1, s2, s3, s4], "Introduction to AI"):
        print(attempt)
    # expected output:
    # Jack Java
    # Olivia C. Objective
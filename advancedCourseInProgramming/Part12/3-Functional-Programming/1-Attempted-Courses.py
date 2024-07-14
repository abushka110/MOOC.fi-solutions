class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

# solution
def names_of_students(attempts: list):
    return list(map(lambda t: t.student_name, attempts))

def course_names(attempts: list):
    # Use map to extract course names from each CourseAttempt object
    course_names = map(lambda attempt: attempt.course_name, attempts)
    # Convert to set to remove duplicates, then back to list and sort
    return sorted(set(course_names))

# test
if __name__ == "__main__":
    # test 1
    print("TEST 1")
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)
    for name in names_of_students([s1, s2, s3]):
        print(name)
    # expected output:
    # Peter Python
    # Olivia C. Objective
    # Peter Python
    print()

    # test 2
    print("TEST 2")
    for name in course_names([s1, s2, s3]):
        print(name)
    # expected output:
    # Advanced Course in Programming
    # Introduction to Programming
    print()
import datetime

def final_points():
    start_times = {}
    task_grade_dict = {}
    
    with open("start_times.csv") as start_file, open("submissions.csv") as submissions_file:
        for line in start_file:
            name, start_time = line.strip().split(";")
            start_times[name] = datetime.datetime.strptime(start_time, "%H:%M")
        
        for line in submissions_file:
            name, task, points, submission_time = line.strip().split(";")
            submission_time = datetime.datetime.strptime(submission_time, "%H:%M")
            
            if name not in task_grade_dict:
                task_grade_dict[name] = {}
            
            if submission_time < start_times[name] + datetime.timedelta(hours=3):
                if task not in task_grade_dict[name] or int(points) > int(task_grade_dict[name][task]):
                    task_grade_dict[name][task] = points
        
    # Calculating total points for each participant
    final_dict = {}
    for name, tasks in task_grade_dict.items():
        student_grade = 0
        for task_num, grade in tasks.items():
            student_grade += int(grade)
        final_dict[name] = student_grade

    return final_dict

# Test the function
if __name__ == "__main__":
    print(final_points())

# solution
import datetime

def cheaters():
    start_times = {}
    cheaters = []
    with open("start_times.csv") as start_file, open("submissions.csv") as submissions_file:
        for line in start_file:
            name, start_time = line.strip().split(";")
            start_times[name] = datetime.datetime.strptime(start_time, "%H:%M")
        for line in submissions_file:
            name, task, points, submission_time = line.strip().split(";")
            submission_time = datetime.datetime.strptime(submission_time, "%H:%M")
            if (submission_time - start_times[name]).total_seconds() > 3 * 60 * 60 and name not in cheaters:
                cheaters.append(name)
    return cheaters

# test
if __name__ == "__main__":
    print(cheaters())

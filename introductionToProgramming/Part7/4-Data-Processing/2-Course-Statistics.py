# solution
import urllib.request
import json

def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = json.load(my_request)
    active_courses = []
    for course in data:
        if course["enabled"] == True:
            active_courses.append((course['fullName'], course['name'], course['year'], sum(course['exercises'])))
    return active_courses

def retrieve_course(course_name: str):
    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = json.load(my_request)

    info = {
        'weeks': len(data),
        'students': 0,
        'hours': 0,
        'hours_average': 0,
        'exercises': 0,
        'exercises_average': 0
    }
    
    for week in data.values():
        info['students'] = max(info['students'], week['students'])
        info['hours'] += week['hour_total']
        info['hours_average'] = info['hours'] // info['students']
        info['exercises'] += week['exercise_total']
        info['exercises_average'] = info['exercises'] // info['students']

    return info

# test
if __name__ == "__main__":
    # retrieve_all()
    print(retrieve_course("docker2019"))
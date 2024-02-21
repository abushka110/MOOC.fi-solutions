# solution
# def oldest_person(people: list):
#     oldest = people[0][0]
#     oldest_year = people[0][1]
#     for person in people:
#         if oldest_year > person[1]:
#             oldest = person[0]
#             oldest_year = person[1]
#     return oldest

# solution 1 - better
def oldest_person(people: list):
    oldest = people[0]
    for person in people:
        if person[1] < oldest[1]:
            oldest = person
    return oldest[0]

# test
if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]
    print(oldest_person(people)) # Mary
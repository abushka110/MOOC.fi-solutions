# solution
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self) -> None:
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        return len(self.persons) == 0
    
    def print_contents(self):
        persons_height = 0
        for person in self.persons:
            persons_height += person.height
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {persons_height} cm")
        for person in self.persons:
            print(f"{person.name} ({person.height} cm)")

# test
if __name__ == "__main__":
    room = Room()
    print("Is the room empty?", room.is_empty())
    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Ally", 166))
    room.add(Person("Nina", 162))
    room.add(Person("Dorothy", 155))
    print("Is the room empty?", room.is_empty())
    room.print_contents()
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
        if person not in self.persons:
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

    def shortest(self):
        if not self.persons:
            return None
        else:
            shortest_person = self.persons[0]  # Fix index error
            for person in self.persons:
                if person.height < shortest_person.height:
                    shortest_person = person
            return shortest_person

    def remove_shortest(self):
        if not self.persons:  # If the room is empty
            return None
        else:
            shortest_person = self.shortest()
            self.persons.remove(shortest_person)
            return shortest_person

            
# test
# if __name__ == "__main__":
    # test 1
    # room = Room()
    # print("Is the room empty?", room.is_empty())
    # room.add(Person("Lea", 183))
    # room.add(Person("Kenya", 172))
    # room.add(Person("Ally", 166))
    # room.add(Person("Nina", 162))
    # room.add(Person("Dorothy", 155))
    # print("Is the room empty?", room.is_empty())
    # room.print_contents()
    # expected output:
    # Is the room empty? True
    # Is the room empty? False
    # There are 5 persons in the room, and their combined height is 838 cm
    # Lea (183 cm)
    # Kenya (172 cm)
    # Ally (166 cm)
    # Nina (162 cm)
    # Dorothy (155 cm)


    # test 2
    # room = Room()
    # print("Is the room empty?", room.is_empty())
    # print("Shortest:", room.shortest())
    # room.add(Person("Lea", 183))
    # room.add(Person("Kenya", 172))
    # room.add(Person("Nina", 162))
    # room.add(Person("Ally", 166))
    # print()
    # print("Is the room empty?", room.is_empty())
    # print("Shortest:", room.shortest())
    # print()
    # room.print_contents()
    # expected output:
    # Is the room empty? True
    # Shortest: None

    # Is the room empty? False
    # Shortest: Nina

    # There are 4 persons in the room, and their combined height is 683 cm
    # Lea (183 cm)
    # Kenya (172 cm)
    # Nina (162 cm)
    # Ally (166 cm)


    # test 3
    # room = Room()
    # room.add(Person("Lea", 183))
    # room.add(Person("Kenya", 172))
    # room.add(Person("Nina", 162))
    # room.add(Person("Ally", 166))
    # room.print_contents()
    # print()
    # removed = room.remove_shortest()
    # print(f"Removed from room: {removed.name}")
    # print()
    # room.print_contents()
    # There are 4 persons in the room, and their combined height is 683 cm
    # Lea (183 cm)
    # Kenya (172 cm)
    # Nina (162 cm)
    # Ally (166 cm)

    # Removed from room: Nina

    # There are 3 persons in the room, and their combined height is 521 cm
    # Lea (183 cm)
    # Kenya (172 cm)
    # Ally (166 cm)


    # test 4
    
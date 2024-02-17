# solution
def add(phonebook_dict):
    name = input("name: ")
    number = input("number: ")
    if name in phonebook_dict:
        phonebook_dict[name].append(number)
    else:
        phonebook_dict[name] = [number]
    print("ok!")

def search(phonebook_dict):
    name = input("name: ")
    if name in phonebook_dict:
        for item in phonebook_dict[name]:
            print(item)
    else:
        print("no number")

def phone_book():
    phonebook_dict = {}
    command_no = int(input("command (1 search, 2 add, 3 quit): "))
    while command_no != 3:
        if command_no == 1:
            search(phonebook_dict)
        elif command_no == 2:
            add(phonebook_dict)
        command_no = int(input("command (1 search, 2 add, 3 quit): "))
    print("quitting...")
        
# test
phone_book()
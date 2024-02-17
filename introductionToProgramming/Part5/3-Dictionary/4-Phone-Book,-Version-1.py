# solution
def add(phonebook_dict):
    name = input("name: ")
    phonebook_dict[name] = input("number: ")
    print("ok!")

def search(phonebook_dict):
    name = input("name: ")
    if name in phonebook_dict:
        print(phonebook_dict[name])
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
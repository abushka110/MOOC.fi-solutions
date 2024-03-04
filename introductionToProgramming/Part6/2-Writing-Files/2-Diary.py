# solution
print("1 - add an entry, 2 - read entries, 0 - quit")
fun_action = int(input("Function: "))
while fun_action != 0:
    if fun_action == 1:
        diary_entry = input("Diary entry: ")
        with open("diary.txt", "a") as add_file:
            add_file.write(f"{diary_entry}\n")
        print("Diary saved")
    elif fun_action == 2:
        print("Entries:")
        with open("diary.txt") as read_file:
            for line in read_file:
                line = line.replace("\n", "")
                print(line)
    print("1 - add an entry, 2 - read entries, 0 - quit")
    fun_action = int(input("Function: "))
print("Bye now!")

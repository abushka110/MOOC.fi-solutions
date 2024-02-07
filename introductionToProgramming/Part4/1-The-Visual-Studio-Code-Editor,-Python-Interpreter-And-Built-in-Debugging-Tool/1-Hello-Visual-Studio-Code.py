editor = input("Editor: ")
string = "Visual Studio Code"
while editor.lower() != string.lower():
    if editor.lower() == "word" or editor.lower() == "notepad":
        print("awful")
    else:
        print("not good")
    editor = input("Editor: ")

print("an excellent choice!")
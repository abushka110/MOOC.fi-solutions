# solution
def read_input(phrase: str, num_1: int, num_2: int):
    alert_message = f"You must type in an integer between {num_1} and {num_2}"
    while True:
        try:
            number = int(input("Please type in a number: "))
            if num_1 <= number <= num_2:
                return number
            else:
                print(alert_message)
        except ValueError:
            print(alert_message)

# test
if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)
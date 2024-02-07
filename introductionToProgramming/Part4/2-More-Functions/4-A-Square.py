# Copy here code of line function from previous exercise
def line(size, symbols):
    if len(symbols) > 0:
        print(symbols[0] * size)
    else:
        print("*" * size)

def square(size, character):
    # You should call function line here with proper parameters
    index = size
    while index != 0:
        line(size, character)
        index -= 1
        

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")
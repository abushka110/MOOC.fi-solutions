# Copy here code of line function from previous exercise
def line(size, symbols):
    if len(symbols) > 0:
        print(symbols[0] * size)
    else:
        print("*" * size)

def triangle(size):
    # You should call function line here with proper parameters
    index = 1
    while index <= size:
        line(index, "#")
        index += 1
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)

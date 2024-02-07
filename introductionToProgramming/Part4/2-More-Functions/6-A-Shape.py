# Copy here code of line function from previous exercise and use it in your solution
def line(size, symbols):
    if len(symbols) > 0:
        print(symbols[0] * size)
    else:
        print("*" * size)

# shape
def shape(size, symbol, size1, symbol1):
    index = 1
    while index <= size:
        line(index, symbol)
        index += 1
    index = 0
    while index < size1:
        line(size, symbol1)
        index += 1
        

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "X", 3, "*")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")
def line(size, symbols):
    if len(symbols) > 0:
        print(symbols[0] * size)
    else:
        print("*" * size)

if __name__ == "__main__":
    line(5, "")
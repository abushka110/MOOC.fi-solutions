# solution 1
# def print_many_times(text, times):
#     print(f"{text}\n" * times)

# solution 2
def print_many_times(text, times):
    while times != 0:
        print(text)
        times -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print_many_times("python", 5)
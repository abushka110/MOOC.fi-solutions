# solution
def lengths(lists: list) -> list:
    return [len(each_list) for each_list in lists]

# test
if __name__ == "__main__":
    lists = [[1,2,3,4,5], [324, -1, 31, 7],[]]
    print(lengths(lists))

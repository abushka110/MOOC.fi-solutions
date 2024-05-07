# solution
class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        most_common = None
        most_common_count = 0
        for item in my_list:
            if my_list.count(item) > most_common_count:
                most_common = item
                most_common_count = my_list.count(item)
        return most_common
    
    @classmethod
    def doubles(cls, my_list: list):
        doub = []
        for item in my_list:
            if my_list.count(item) >= 2 and item not in doub:
                doub.append(item)
        return len(doub)

# test
if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
# solution
# a function
def execute_many_times(my_function, n: int):
    # call function in given range times
    for i in range(n):
        my_function()

# b function
def check_list(check_function, my_list: list):
    # check every value in list
    for item in my_list:
        # check if called function return True or False
        if check_function(item) == False:
        # can be checked with keyword not
        # if not check_function(item):
            return False
    # return true if all tests was True
    return True

# test
if __name__ == "__main__":
    # test 1
    print("testcase 1")
    def function_to_call():
        print("passed")
    execute_many_times(function_to_call, 3)
    print()

    # test 2
    # Define function
    print("testcase 2")
    def test_function():
        print('Hello from test function!')
    # Function, that takes another function as a parameter
    def execute_function(my_function):
        # Calling function given as a parameter inside the function execute_function
        my_function()
    # Now, inside the execute_function, function test_function is called
    execute_function(test_function) # Prints out 'Hello from test function!'
    print()
    # test_function is defined above
    execute_many_times(test_function, 3) # Prints out 'Hello from test function!' 3 times
    print()
    execute_many_times(test_function, 5) # Prints out 'Hello from test function!' 5 times
    print()

    # test 3
    print("testcase 3")
    def greater_than_zero(number: int):
        return number > 0

    def is_palindrome(string: str):
        return string == string[::-1]

    print(check_list(greater_than_zero, [1,2,3])) # True
    print(check_list(greater_than_zero, [1,2,0])) # False
    print(check_list(is_palindrome, ['abba', 'neveroddoreven'])) # True
    print(check_list(is_palindrome, ['abba', 'python'])) # False


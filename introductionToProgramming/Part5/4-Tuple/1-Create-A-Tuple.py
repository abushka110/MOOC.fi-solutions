# solution
def create_tuple(x: int, y: int, z: int):
    numbers = [x, y, z]
    imm_numbers = (min(numbers), max(numbers), sum(numbers))
    return imm_numbers

# solution 1
# def create_tuple(x: int, y: int, z: int):
#     """ The function returns a tuple formed from the parameters (smallest, greatest, sum) """
#     smallest = min([x, y, z])
#     greatest = max([x, y, z])
#     sum = x + y + z # sum([x, y, z]) also works
 
#     return (smallest, greatest, sum)

# test
if __name__ == "__main__":
    print(create_tuple(5, 3, -1)) # (-1, 5, 7)
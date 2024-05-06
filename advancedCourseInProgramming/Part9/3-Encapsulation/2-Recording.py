# solution
class Recording:
    def __init__(self, length: int):
        if length >= 0:
            self.__length = length
        else:
            raise ValueError("Negative length is not possible")
    
    # A getter method
    @property
    def length(self):
        return self.__length

    # A setter method
    @length.setter
    def length(self, length_new):
        if length_new >= 0:
            self.__length = length_new
        else:
            raise ValueError("Negative length is not possible")

# test
if __name__ == "__main__":
    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)
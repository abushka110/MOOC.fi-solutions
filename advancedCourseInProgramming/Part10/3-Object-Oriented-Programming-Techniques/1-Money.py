# solution
class Money:
    def __init__(self, euros: int, cents: int):
        self.euros = euros
        self.cents = cents

    def __str__(self):
        if self.cents < 10:
            return f"{self.euros}.0{self.cents} eur"
        else:
            return f"{self.euros}.{self.cents} eur"
        
    def __eq__(self, another):
        if (self.euros + self.cents / 100) == (another.euros + another.cents / 100):
            return True
        else:
            return False
    
    def __lt__(self, another):
        if (self.euros + self.cents / 100) < (another.euros + another.cents / 100):
            return True
        else:
            return False 
        
    def __gt__(self, another):
        if (self.euros + self.cents / 100) > (another.euros + another.cents / 100):
            return True
        else:
            return False 
        
    def __ne__(self, another):
        if (self.euros + self.cents / 100) != (another.euros + another.cents / 100):
            return True
        else:
            return False 

# test
if __name__ == "__main__":
    # test 1
    e1 = Money(4, 10)
    e2 = Money(2, 5)
    e3 = Money(4, 10)
    print(e1)
    print(e2)
    print(e3)
    print(e1 == e2)
    print(e1 == e3)
    # expected output:
    # 4.10 eur
    # 2.05 eur
    # 4.10 eur
    # False
    # True

    # test 2
    e1 = Money(4, 10)
    e2 = Money(2, 5)
    print(e1 != e2)
    print(e1 < e2)
    print(e1 > e2)
    # expected output:
    # True
    # False
    # True
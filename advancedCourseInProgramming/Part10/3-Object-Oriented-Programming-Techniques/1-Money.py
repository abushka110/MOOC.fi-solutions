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

# test
if __name__ == "__main__":
    pass  # Add your test code here

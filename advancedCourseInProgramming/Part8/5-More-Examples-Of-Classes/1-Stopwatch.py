# solution
# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
    
    def tick(self):
        if self.seconds == 59 and self.minutes == 59:
            self.seconds = 0
            self.minutes = 0
        else:
            if self.seconds == 59:
                self.seconds = 0
                self.minutes += 1
            else:
                self.seconds += 1
            
    
    def __str__(self):
        return f"{self.minutes:02d}:{self.seconds:02d}"

# test
if __name__ == "__main__":
    # watch = Stopwatch()
    # for i in range(3600):
    #     print(watch)
    #     watch.tick()
    clock = Stopwatch()                
    clock.tick()     
    print(clock)           
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

# 00:00
# 00:01
# 00:02
# ... many more lines printed out
# 00:59
# 01:00
# 01:01
# ... many, many more lines printed out
# 59:58
# 59:59
# 00:00
# 00:01
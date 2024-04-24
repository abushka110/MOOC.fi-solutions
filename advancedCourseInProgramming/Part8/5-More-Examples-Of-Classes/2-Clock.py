# solution
# Write your solution here:
class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def tick(self):
        if self.hours == 23 and self.seconds == 59 and self.minutes == 59:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        else:
            if self.seconds == 59 and self.minutes == 59:
                self.hours += 1
                self.minutes = 0
                self.seconds = 0
            else:
                if self.seconds == 59:
                    self.minutes += 1
                    self.seconds = 0
                else:
                    self.seconds += 1

    def set(self, hours_set, minutes_set):
        self.hours = hours_set
        self.minutes = minutes_set
        self.seconds = 0
            
    
    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

# test
if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    
    def __lt__(self, other):
    
        if self.hours == other.hours:
            return self.minutes < other.minutes
        return self.hours < other.hours



t1 = Time(10, 30)
t2 = Time(12, 15)
print(t1 < t2)  
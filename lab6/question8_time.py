class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __eq__(self, other):
        return (self.hours == other.hours and
                self.minutes == other.minutes and
                self.seconds == other.seconds)

# Test the Time class
if __name__ == "__main__":
    t1 = Time(10, 30, 45)
    t2 = Time(10, 30, 45)
    t3 = Time(11, 15, 20)
    print(t1 == t2)  # True
    print(t1 == t3)  # False

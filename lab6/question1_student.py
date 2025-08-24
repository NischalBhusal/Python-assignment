class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_info(self):
        print(f"Name: {self.name}, Roll Number: {self.roll_number}, Marks: {self.marks}")

# Test the Student class
if __name__ == "__main__":
    student = Student("Ram Bahadur", 101, 95)
    student.display_info()

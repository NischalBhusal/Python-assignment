import json

# Question 2: Student Class with Multiple Objects
# Create a class Student with attributes name and marks, create three objects and display details

class Student:
    # Class variable to keep track of total students
    total_students = 0
    
    def __init__(self, name, marks):
        """
        Constructor to initialize Student object with name and marks
        Args:
            name (str): The name of the student
            marks (list or float): The marks of the student (can be single mark or list of marks)
        """
        self.name = name
        
        # Handle both single mark and list of marks
        if isinstance(marks, (int, float)):
            self.marks = [marks]  # Convert single mark to list
        elif isinstance(marks, list):
            self.marks = marks
        else:
            self.marks = []
            print(f" Warning: Invalid marks format for {name}. Setting empty marks.")
        
        # Increment total students count
        Student.total_students += 1
        self.student_id = Student.total_students
        
        print(f" Student created: {self.name} (ID: {self.student_id})")
    
    def show_details(self):
        """
        Method to display student's name and marks details
        """
        print("\n‍ STUDENT DETAILS")
        print("-" * 35)
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        
        if self.marks:
            print(f"Marks: {self.marks}")
            print(f"Total Marks: {sum(self.marks)}")
            print(f"Average Mark: {sum(self.marks) / len(self.marks):.2f}")
            print(f"Highest Mark: {max(self.marks)}")
            print(f"Lowest Mark: {min(self.marks)}")
            
            # Grade calculation based on average
            average = sum(self.marks) / len(self.marks)
            grade = self.calculate_grade(average)
            print(f"Grade: {grade}")
        else:
            print("Marks: No marks recorded")
        
        print("-" * 35)
    
    def calculate_grade(self, average):
        """
        Calculate grade based on average marks
        Args:
            average (float): Average marks
        Returns:
            str: Grade letter
        """
        if average >= 90:
            return "A+ (Excellent)"
        elif average >= 80:
            return "A (Very Good)"
        elif average >= 70:
            return "B+ (Good)"
        elif average >= 60:
            return "B (Above Average)"
        elif average >= 50:
            return "C (Average)"
        elif average >= 40:
            return "D (Below Average)"
        else:
            return "F (Fail)"
    
    def add_mark(self, mark):
        """
        Add a new mark to the student's record
        Args:
            mark (float): The mark to add
        """
        if 0 <= mark <= 100:
            self.marks.append(mark)
            print(f" Mark {mark} added for {self.name}")
        else:
            print(f" Invalid mark: {mark}. Mark should be between 0 and 100.")
    
    def update_name(self, new_name):
        """
        Update student's name
        Args:
            new_name (str): New name for the student
        """
        old_name = self.name
        self.name = new_name.strip()
        print(f" Name updated: {old_name} → {self.name}")
    
    def get_total_marks(self):
        """
        Get total marks of the student
        Returns:
            float: Total marks
        """
        return sum(self.marks) if self.marks else 0
    
    def get_average_marks(self):
        """
        Get average marks of the student
        Returns:
            float: Average marks
        """
        return sum(self.marks) / len(self.marks) if self.marks else 0
    
    def is_passing(self, passing_grade=40):
        """
        Check if student is passing
        Args:
            passing_grade (float): Minimum passing grade
        Returns:
            bool: True if passing, False otherwise
        """
        return self.get_average_marks() >= passing_grade
    
    def __str__(self):
        """
        String representation of the Student object
        """
        avg = self.get_average_marks()
        return f"Student({self.name}, Avg: {avg:.1f}, Marks: {len(self.marks)})"
    
    @classmethod
    def get_total_students(cls):
        """
        Class method to get total number of students
        Returns:
            int: Total number of students created
        """
        return cls.total_students
    
    @classmethod
    def create_student_from_input(cls):
        """
        Class method to create student from user input
        Returns:
            Student: New student object
        """
        try:
            name = input("Enter student name: ").strip()
            marks_input = input("Enter marks (space-separated for multiple): ").strip()
            
            if marks_input:
                marks = [float(x) for x in marks_input.split()]
            else:
                marks = []
            
            return cls(name, marks)
        except ValueError:
            print(" Invalid marks format. Creating student with no marks.")
            return cls(name, [])

# Simplified output formatting
def beautify_output():
    print("=" * 40)
    print("STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)

# Save student data to a JSON file
def save_students_to_file(students, filename="students_data.json"):
    """Save student data to a JSON file."""
    data = [
        {
            "id": student.student_id,
            "name": student.name,
            "marks": student.marks,
            "total_marks": student.get_total_marks(),
            "average_marks": student.get_average_marks(),
            "grade": student.calculate_grade(student.get_average_marks())
        }
        for student in students
    ]
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# Load student data from a JSON file
def load_students_from_file(filename="students_data.json"):
    """Load student data from a JSON file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            return [Student(d["name"], d["marks"]) for d in data]
    except FileNotFoundError:
        return []

# Main demonstration
if __name__ == "__main__":
    beautify_output()

    # Load existing students or start fresh
    students = load_students_from_file()

    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            marks = list(map(int, input("Enter marks (space-separated): ").split()))
            new_student = Student(name, marks)
            students.append(new_student)
            save_students_to_file(students)
        elif choice == "2":
            if not students:
                print("No students available.")
            else:
                for student in students:
                    print(f"{student.name}: Total={student.get_total_marks()}, Avg={student.get_average_marks():.2f}")
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

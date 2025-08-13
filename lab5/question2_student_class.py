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

# Demonstration and Testing
if __name__ == "__main__":
    print("=" * 50)
    print("QUESTION 2: STUDENT CLASS DEMONSTRATION")
    print("=" * 50)
    
    # 1. Create three Student objects as required
    print("\n1. Creating three Student objects:")
    
    # Student 1 - Single subject
    student1 = Student("Alice Johnson", 85)
    
    # Student 2 - Multiple subjects
    student2 = Student("Bob Smith", [78, 82, 90, 75, 88])
    
    # Student 3 - Multiple subjects with different performance
    student3 = Student("Charlie Brown", [92, 95, 88, 91, 94])
    
    # 2. Display details of all three students using show_details() method
    print("\n2. Displaying details of all three students:")
    student1.show_details()
    student2.show_details()
    student3.show_details()
    
    # 3. Additional demonstrations
    print("\n3. Additional Student Operations:")
    
    # Add more marks to student1
    print("Adding more marks to Alice:")
    student1.add_mark(90)
    student1.add_mark(87)
    student1.add_mark(92)
    student1.show_details()
    
    # Update student name
    print("\nUpdating student name:")
    student2.update_name("Robert Smith")
    student2.show_details()
    
    # 4. Class-level operations
    print(f"\n4. Class Statistics:")
    print(f"Total students created: {Student.get_total_students()}")
    
    # 5. Student comparison
    print("\n5. Student Performance Comparison:")
    students = [student1, student2, student3]
    
    print(" Performance Summary:")
    print(f"{'Name':<15} {'Total':<8} {'Average':<8} {'Grade':<15} {'Status'}")
    print("-" * 60)
    
    for student in students:
        total = student.get_total_marks()
        average = student.get_average_marks()
        grade = student.calculate_grade(average)
        status = "PASS" if student.is_passing() else "FAIL"
        print(f"{student.name:<15} {total:<8.1f} {average:<8.1f} {grade:<15} {status}")
    
    # Find top performer
    top_student = max(students, key=lambda s: s.get_average_marks())
    print(f"\n Top Performer: {top_student.name} (Average: {top_student.get_average_marks():.1f})")
    
    # Find student with most subjects
    most_subjects = max(students, key=lambda s: len(s.marks))
    print(f" Most Subjects: {most_subjects.name} ({len(most_subjects.marks)} subjects)")
    
    # Class average
    class_average = sum(s.get_average_marks() for s in students) / len(students)
    print(f" Class Average: {class_average:.2f}")
    
    # 6. Interactive student creation
    print("\n6. Interactive Student Creation:")
    try:
        create_more = input("Would you like to create another student? (y/n): ").lower()
        if create_more == 'y':
            new_student = Student.create_student_from_input()
            new_student.show_details()
            
            # Add to comparison
            students.append(new_student)
            print(f"\nUpdated class size: {len(students)} students")
            print(f"New class average: {sum(s.get_average_marks() for s in students) / len(students):.2f}")
            
    except KeyboardInterrupt:
        print("\n\nStudent creation cancelled.")
    
    # 7. String representations
    print("\n7. Student Objects Summary:")
    for i, student in enumerate(students, 1):
        print(f"{i}. {student}")
    
    # 8. Passing/Failing analysis
    print("\n8. Academic Performance Analysis:")
    passing_students = [s for s in students if s.is_passing()]
    failing_students = [s for s in students if not s.is_passing()]
    
    print(f" Passing Students: {len(passing_students)}")
    for student in passing_students:
        print(f"   - {student.name} (Avg: {student.get_average_marks():.1f})")
    
    if failing_students:
        print(f" Failing Students: {len(failing_students)}")
        for student in failing_students:
            print(f"   - {student.name} (Avg: {student.get_average_marks():.1f})")
    else:
        print(" All students are passing!")
    
    print("\n" + "=" * 50)
    print("STUDENT CLASS DEMONSTRATION COMPLETED!")
    print("Key Concepts: Multiple Objects, Class Variables, Methods, Comparison")
    print("=" * 50)

students = []

while True:
    print("\n===== Student Report Card Management System =====")
    print("1. Add new student record")
    print("2. View report of all students")
    print("3. Display class topper(s)")
    print("4. Search student by roll number")
    print("5. Display students who failed in one or more subjects")
    print("6. Update marks of a student")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        try:
            m1 = int(input("Enter marks in Subject 1: "))
            m2 = int(input("Enter marks in Subject 2: "))
            m3 = int(input("Enter marks in Subject 3: "))
            student = {
                'name': name,
                'roll': roll,
                'marks': [m1, m2, m3]
            }
            students.append(student)
            print("Student record added successfully.")
        except ValueError:
            print("Invalid marks entered. Please use integers.")

    elif choice == '2':
        if not students:
            print("No records to show.")
        else:
            print("\n---- All Student Reports ----")
            for s in students:
                avg = sum(s['marks']) / len(s['marks'])
                print(f"Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}, Average: {avg:.2f}")

    elif choice == '3':
        if not students:
            print("No students to evaluate.")
        else:
            max_avg = 0
            toppers = []
            for s in students:
                avg = sum(s['marks']) / len(s['marks'])
                if avg > max_avg:
                    max_avg = avg
                    toppers = [s]
                elif avg == max_avg:
                    toppers.append(s)
            print(f"\nTopper(s) with average {max_avg:.2f}:")
            for s in toppers:
                print(f"Name: {s['name']}, Roll: {s['roll']}")

    elif choice == '4':
        roll = input("Enter roll number to search: ")
        found = False
        for s in students:
            if s['roll'] == roll:
                print(f"\nStudent Found - Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == '5':
        print("\nStudents who failed (marks < 40 in any subject):")
        found = False
        for s in students:
            if any(mark < 40 for mark in s['marks']):
                print(f"Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}")
                found = True
        if not found:
            print("No students failed in any subject.")

    elif choice == '6':
        roll = input("Enter roll number to update marks: ")
        updated = False
        for s in students:
            if s['roll'] == roll:
                try:
                    print("Enter new marks:")
                    m1 = int(input("Subject 1: "))
                    m2 = int(input("Subject 2: "))
                    m3 = int(input("Subject 3: "))
                    s['marks'] = [m1, m2, m3]
                    print("Marks updated successfully.")
                    updated = True
                    break
                except ValueError:
                    print("Invalid marks entered.")
        if not updated:
            print("Student not found.")

    elif choice == '7':
        print("Exiting system. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 7.")
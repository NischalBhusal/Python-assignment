students = {
    "Ram": [78, 85, 90],
    "Hari": [88, 76, 92],
    "Sita": [95, 89, 93]
}

while True:
    print("\nChoose an option:")
    print("a. Display average marks")
    print("b. Find topper")
    print("c. Update marks")
    print("d. Exit")
    choice = input("Enter your choice (a/b/c/d): ").lower()

    if choice == 'a':
        print("\nAverage marks of each student:")
        for name in students:
            marks = students[name]
            avg = sum(marks) / len(marks)
            print(f"{name}: {avg:.2f}")

    elif choice == 'b':
        topper = ""
        top_avg = 0
        for name in students:
            marks = students[name]
            avg = sum(marks) / len(marks)
            if avg > top_avg:
                top_avg = avg
                topper = name
        print(f"\nTopper: {topper} with average marks {top_avg:.2f}")

    elif choice == 'c':
        name = input("Enter student name to update: ")
        if name in students:
            try:
                print("Enter new marks for 3 subjects:")
                m1 = int(input("Subject 1: "))
                m2 = int(input("Subject 2: "))
                m3 = int(input("Subject 3: "))
                students[name] = [m1, m2, m3]
                print(f"Updated marks for {name}")
            except ValueError:
                print("Invalid input. Please enter integer marks.")
        else:
            print("Student not found.")

    elif choice == 'd':
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")
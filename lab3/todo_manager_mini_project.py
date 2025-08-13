# Simplified To-Do Manager with Interactive Functionality

def add_task(task_list, task_name):
    """Add a new task to the task list."""
    task_list.append({"name": task_name, "completed": False})

def list_tasks(task_list):
    """List all tasks with their status."""
    if not task_list:
        print("No tasks available.")
        return
    for i, task in enumerate(task_list, 1):
        status = "[Completed]" if task["completed"] else "[Pending]"
        print(f"{i}. {task['name']} {status}")

def complete_task(task_list, task_index):
    """Mark a task as completed by its index."""
    if 0 <= task_index < len(task_list):
        task_list[task_index]["completed"] = True
    else:
        print("Invalid task index.")

def main():
    """Main function to run the To-Do Manager."""
    tasks = []
    while True:
        print("\nTo-Do Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            add_task(tasks, task_name)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            try:
                task_index = int(input("Enter task number to complete: ")) - 1
                complete_task(tasks, task_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Exiting To-Do Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

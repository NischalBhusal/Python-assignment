print("=" * 60)
print("MINI PROJECT: SIMPLE TO-DO MANAGER")
print("Using Functional Programming with Lambda, Filter, and Map")
print("=" * 60)

def add_task(task_list, task_name):
    """
    Add a new task to the task list
    Each task is a dictionary: {"name": str, "completed": bool}
    """
    new_task = {"name": task_name, "completed": False}
    return task_list + [new_task]  # Return new list (functional approach)

def list_pending(task_list):
    """
    Use lambda and filter() to list only incomplete tasks
    """
    return list(filter(lambda task: not task["completed"], task_list))

def complete_all(task_list):
    """
    Use map() to mark all tasks as completed
    """
    return list(map(lambda task: {"name": task["name"], "completed": True}, task_list))

def complete_task(task_list, task_name):
    """
    Mark a specific task as completed
    """
    return list(map(
        lambda task: {"name": task["name"], "completed": True} 
        if task["name"].lower() == task_name.lower() 
        else task, 
        task_list
    ))

def search_tasks(task_list, keyword):
    """
    Search tasks containing a keyword using filter() and lambda
    """
    return list(filter(
        lambda task: keyword.lower() in task["name"].lower(), 
        task_list
    ))

def display_tasks(task_list, title="Current Tasks"):
    """
    Display all tasks in a formatted way
    """
    print(f"\n{title}:")
    print("-" * 30)
    if not task_list:
        print("  No tasks found.")
        return
    
    for i, task in enumerate(task_list, 1):
        status = "" if task["completed"] else ""
        print(f"  {i}. {status} {task['name']}")

def get_completed_tasks(task_list):
    """
    Get all completed tasks using filter and lambda
    """
    return list(filter(lambda task: task["completed"], task_list))

def count_tasks(task_list):
    """
    Count total, completed, and pending tasks
    """
    total = len(task_list)
    completed = len(get_completed_tasks(task_list))
    pending = len(list_pending(task_list))
    
    return {
        "total": total,
        "completed": completed,
        "pending": pending
    }

def remove_completed_tasks(task_list):
    """
    Remove all completed tasks using filter
    """
    return list(filter(lambda task: not task["completed"], task_list))

# Sample Workflow Demonstration
print("\n1. CREATING INITIAL TASKS")
print("-" * 30)

# Initialize empty task list
tasks = []

# Add tasks as shown in the sample workflow
tasks = add_task(tasks, "Buy groceries")
tasks = add_task(tasks, "Finish assignment")
tasks = add_task(tasks, "Call friend")
tasks = add_task(tasks, "Clean room")
tasks = add_task(tasks, "Study Python")

display_tasks(tasks, "Initial Tasks")

print("\n2. LISTING PENDING TASKS")
print("-" * 30)

# List incomplete tasks
pending_tasks = list_pending(tasks)
display_tasks(pending_tasks, "Pending Tasks")

print("\n3. COMPLETING SPECIFIC TASKS")
print("-" * 35)

# Complete specific tasks
tasks = complete_task(tasks, "Buy groceries")
tasks = complete_task(tasks, "Call friend")

display_tasks(tasks, "After Completing Some Tasks")

print("\n4. SEARCHING TASKS")
print("-" * 20)

# Search tasks with keyword "call"
search_result = search_tasks(tasks, "call")
print(f"Search Result for 'call': {[task['name'] for task in search_result]}")

# Search for other keywords
study_tasks = search_tasks(tasks, "study")
print(f"Search Result for 'study': {[task['name'] for task in study_tasks]}")

assignment_tasks = search_tasks(tasks, "assignment")
print(f"Search Result for 'assignment': {[task['name'] for task in assignment_tasks]}")

print("\n5. TASK STATISTICS")
print("-" * 20)

stats = count_tasks(tasks)
print(f"Total tasks: {stats['total']}")
print(f"Completed tasks: {stats['completed']}")
print(f"Pending tasks: {stats['pending']}")

print("\n6. MARK ALL REMAINING AS COMPLETED")
print("-" * 35)

# Mark all tasks as complete
all_completed_tasks = complete_all(tasks)
display_tasks(all_completed_tasks, "All Tasks Completed")

print("\n7. ADVANCED OPERATIONS")
print("-" * 25)

# Add more tasks for demonstration
demo_tasks = []
demo_tasks = add_task(demo_tasks, "Read a book")
demo_tasks = add_task(demo_tasks, "Exercise for 30 minutes")
demo_tasks = add_task(demo_tasks, "Write journal entry")
demo_tasks = add_task(demo_tasks, "Learn new recipe")

# Complete some tasks
demo_tasks = complete_task(demo_tasks, "Read a book")
demo_tasks = complete_task(demo_tasks, "Exercise for 30 minutes")

display_tasks(demo_tasks, "Demo Tasks")

# Show only completed tasks
completed_only = get_completed_tasks(demo_tasks)
display_tasks(completed_only, "Completed Tasks Only")

# Remove completed tasks
active_tasks = remove_completed_tasks(demo_tasks)
display_tasks(active_tasks, "Active Tasks (Completed Removed)")

print("\n8. FUNCTIONAL PROGRAMMING FEATURES DEMONSTRATED")
print("-" * 50)

print(" Lambda functions used for:")
print("  - Filtering incomplete tasks")
print("  - Filtering completed tasks")
print("  - Searching tasks by keyword")
print("  - Marking tasks as completed")

print("\n Filter() used for:")
print("  - Getting pending tasks")
print("  - Getting completed tasks")
print("  - Searching tasks")
print("  - Removing completed tasks")

print("\n Map() used for:")
print("  - Marking all tasks as completed")
print("  - Updating specific task status")

print("\n" + "=" * 60)
print("TO-DO MANAGER PROJECT COMPLETED SUCCESSFULLY!")
print("All functional programming concepts demonstrated.")
print("=" * 60)
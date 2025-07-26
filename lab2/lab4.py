stack = []
queue = []

while True:
    choice = input("\nDo you want to implement stack(1), queue(2), or quit(q)? ")
    if choice == "1":
        schoice = input("Do you want to push(1), pop(2), or back(b)? ")
        if schoice == "1":
            push = input("Enter the element that you want to push onto the stack: ")
            stack.append(push)
            print("Stack after push:", stack)
        elif schoice == "2":
            if len(stack) > 0:
                popped = stack.pop()
                print("Popped element:", popped)
                print("Stack after pop:", stack)
            else:
                print("Your stack has no elements so you cannot pop")
        elif schoice.lower() == "b":
            continue
        else:
            print("Invalid choice for stack operation.")
            
    elif choice == "2":
        qchoice = input("Do you want to enqueue(1), dequeue(2), or back(b)? ")
        if qchoice == "1":
            enqueue = input("Enter the element that you want to enqueue onto the queue: ")
            queue.append(enqueue)
            print("Queue after enqueue:", queue)
        elif qchoice == "2":
            if len(queue) > 0:
                dequeued = queue.pop(0)
                print("Dequeued element:", dequeued)
                print("Queue after dequeue:", queue)
            else:
                print("Your queue has no elements so you cannot dequeue")
        elif qchoice.lower() == "b":
            continue
        else:
            print("Invalid choice for queue operation.")
            
    elif choice.lower() == "q":
        break
        
    else:
        print("Invalid choice. Please enter 1 for stack, 2 for queue, or q to quit.")
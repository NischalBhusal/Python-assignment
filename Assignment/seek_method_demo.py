# Question 2: Demonstrate the seek() method in file handling
def demonstrate_seek_method():
    print("=== Demonstrating seek() Method ===")
    sample_text = "Hello World! This is a demonstration of seek() method."
    with open('demo_file.txt', 'w') as file:
        file.write(sample_text)
    with open('demo_file.txt', 'r') as file:
        print("Read first 5 chars:", file.read(5))
        print("Current position:", file.tell())
        file.seek(0)
        print("After seek(0), read 5 chars:", file.read(5))
        file.seek(6)
        print("After seek(6), read next 5 chars:", file.read(5))

if __name__ == "__main__":
    demonstrate_seek_method()

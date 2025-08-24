class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Test the Dog class
if __name__ == "__main__":
    dog = Dog()
    dog.speak()

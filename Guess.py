import random
min = int(input("Enter lower range: "))
max = int(input("Enter upper range: "))

number = random.randint(min, max)

while True:
    guess = int(input(f"Guess the number between {min} and {max}: "))
    if guess == number:
        print("You guessed right!")
        break
    else:
        print("Wrong guess!")
        choice = input("Do you want to try again? (y/n): ").lower()
        if choice != 'y':
            print(f"The correct number was {number}. Goodbye!")
            break
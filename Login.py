users = { "Nischal": "nischal123","Piyush": "piyush123","Saurabh": "saurabh123","Ankit": "ankit123","Priyanshu": "priyanshu123" }
attempts = 5
while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == password:
        print(f"Welcome, {username}!")
        break
    else:
        attempts -= 1
        print(f"Incorrect username or password. Attempts left: {attempts}")
else:
    print("Your attempts expired")
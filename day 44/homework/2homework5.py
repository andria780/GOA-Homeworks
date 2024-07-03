correct_password = "password123"

password_correct = False

while not password_correct:

    password = input("Enter the password: ")

    if password == correct_password:
        print("Correct password entered. Access granted.")
        password_correct = True
    else:
        print("Incorrect password. Please try again.")

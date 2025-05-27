MINIMUM_LENGTH = 8
password = input("Enter password: ")
while len(password) < MINIMUM_LENGTH:
    print("Invalid password")
    password = input("Enter password: ")
print("*" * len(password))
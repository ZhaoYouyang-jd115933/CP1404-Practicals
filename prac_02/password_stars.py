MINIMUM_LENGTH = 8
def main():
    password = get_valid_password()
    print("*" * len(password))

def get_valid_password():
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Invalid password")
        password = input("Enter password: ")
    return password
main()
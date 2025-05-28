"""
MINIMUM_LENGTH = 8
function main()
    password = get_valid_password()
    print_asterisks(password)

function get_valid_password()
    get password
    while length of password less than MINIMUM_LENGTH
          display "Invalid password"
          get password
    return password

function print_asterisks(password)
    display "*" * length of password
"""
MINIMUM_LENGTH = 8
def main():
    """Get valid password and print asterisks"""
    password = get_valid_password()
    print_asterisks(password)

def get_valid_password():
    """Get valid password"""
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Invalid password")
        password = input("Enter password: ")
    return password

def print_asterisks(password):
    """Print asterisks based on length of password"""
    print("*" * len(password))
main()
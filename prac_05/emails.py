def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        choice = input(f"Is your name {user_name}? (Y/n)")
        if choice == "Y" or choice == "":
            user_name = email_to_name[email]
        else:
            real_name = input("Name: ")
            email_to_name[email] = real_name
        email = input("Email: ")

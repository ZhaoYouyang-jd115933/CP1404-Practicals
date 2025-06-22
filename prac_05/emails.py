def main():
    """Collect emails and names in a dictionary and print the results."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        user_name = extract_name_from_email(email)
        choice = input(f"Is your name {user_name}? (Y/n)").upper()
        if choice == "Y" or choice == "":
            name = user_name
        else:
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    print()
    for email in email_to_name:
        print(f"{email_to_name[email]} ({email})")

def extract_name_from_email(email):
    """Extract a name from the email"""
    name = email.split('@')[0]
    name_parts = name.split('.')
    name_parts = [part.title() for part in name_parts]
    name = ' '.join(name_parts)
    return name

main()
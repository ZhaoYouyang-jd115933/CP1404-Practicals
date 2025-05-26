"""
get name
display menu
get choice
while choice not equal to "Q"
     if choice equal to "H"
         display "Hello" name
     else if choice equal to "G"
         display "Goodbye" name
     else
         display "Invalid choice"
     display menu
     get choice
display "Finished."
"""
name = input("Enter name: ")
MENU = "(H)ello\n(G)oodbye\n(Q)uit"
print(MENU)
choice = input(">>> ")
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ")
print("Finished.")
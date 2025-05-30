"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion

MENU = "C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"
display menu
get choice
while choice not equal to "Q"
     if choice equal to "C"
         get Celsius
         Fahrenheit = Celsius * 9.0 / 5 + 32
         display Fahrenheit
     else if choice equal to "F"
         get Fahrenheit
         Celsius = 5 / 9 * (Fahrenheit - 32)
         display Celsius
     else
         display "Invalid option"
     display menu
     get choice
display "Thank you."
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        # TODO: Write this section to convert F to C and display the result
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")
        # Remove the "pass" statement when you are done. It's a placeholder.
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
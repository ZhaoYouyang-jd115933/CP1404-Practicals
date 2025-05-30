"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion

MENU = "C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"

function main()
    display menu
    get choice
    while choice not equal to "Q"
         if choice equal to "C"
             get Celsius
             Fahrenheit = convert_Celsius_to_Fahrenheit(Celsius)
             display Fahrenheit
         else if choice equal to "F"
             get Fahrenheit
             Celsius = convert_Fahrenheit_to_Celsius(Fahrenheit)
             display Celsius
         else
             display "Invalid option"
         display menu
         get choice
    display "Thank you."

function convert_Celsius_to_Fahrenheit(Celsius)
    return Celsius * 9.0 / 5 + 32

function convert_Fahrenheit_to_Celsius(Fahrenheit)
    return 5 / 9 * (Fahrenheit - 32)
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    """Convert temperature according to user's choice"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit"""
    return celsius * 9.0 / 5 + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius"""
    return 5 / 9 * (fahrenheit - 32)
main()
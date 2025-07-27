from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
def main():
    """Display a menu to allow users to choose available taxis, drive taxis and show the total bill."""
    print("Let's drive!")
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi(fanciness=2, name="Limo", fuel=100),
        SilverServiceTaxi(fanciness=4, name="Hummer", fuel=200)
    ]
    total_bill = 0
    current_taxi = None

    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            total_bill = handle_drive(current_taxi, total_bill)
        else:
            print("Invalid option")

        print(MENU)
        choice = input(">>> ").lower()

def choose_taxi(taxis):
    """Display the list of taxis and let the user choose one."""
    print("Taxis available:")
    display_taxis(taxis)

    try:
        selected_choice = int(input("Choose taxi: "))
        if 0 <= selected_choice < len(taxis):
            selected_taxi = taxis[selected_choice]
            selected_taxi.start_fare()
            return selected_taxi
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid input")
    return None

def display_taxis(taxis):
    """Display all taxis in the list with their index and status."""
    for i in range(len(taxis)):
        print(f"{i} - {taxis[i]}")

main()
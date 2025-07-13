import csv
from prac_07.guitar import Guitar

def main():
    add_guitars()

def add_guitars():
    """Put all new guitars in a list based on the user input"""
    new_guitars = []
    name = input("Name: ")
    while name != "":
        year = input("Year: ")
        cost = input("Cost: ")
        new_guitars.append([name, year, cost])
        print(f"{name} ({year}) : {cost} added.")
        save_new_guitars(new_guitars)
        name = input("Name: ")

def save_new_guitars(new_guitars):
    """Add the input new guitars in csv file"""
    with open("guitars.csv", "a", newline="") as out_file:
        writer = csv.writer(out_file)
        writer.writerows(new_guitars)

main()
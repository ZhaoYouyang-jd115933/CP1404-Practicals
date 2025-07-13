import csv
from prac_07.guitar import Guitar

def main():
    add_guitars()
    guitars = read_file()

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
    return new_guitars

def save_new_guitars(new_guitars):
    """Add the input new guitars in csv file"""
    with open("guitars.csv", "a", newline="") as out_file:
        writer = csv.writer(out_file)
        writer.writerows(new_guitars)

def read_file():
    """Read guitars from guitars.csv and return a list of Guitar objects"""
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(",")
        guitar = Guitar(parts[0], int(parts[1]), parts[2])
        guitars.append(guitar)
    in_file.close()
    return guitars
main()
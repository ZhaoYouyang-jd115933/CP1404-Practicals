"""
Word Occurrences
Estimate: 30 minutes
Actual:   35 minutes
"""
from prac_06.guitar import Guitar
guitars = []
print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year}) : ${cost:.2f} added.")
    print()
    name = input("Name: ")
    print()
    print("... snip ...")
    print()
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
print("These are my guitars:")
for number, guitar in enumerate(guitars, 1):
    vintage_string = "(vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {number}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

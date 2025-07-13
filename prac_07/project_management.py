
import datetime
from operator import attrgetter
from prac_07.project import Project

MIN_NUMBER = 0
MAX_NUMBER = 100
MAX_PRIORITY = 10
CHOICES = ["Y", "N"]
MENU = (
    "- (L)oad projects\n"
    "- (S)ave projects\n"
    "- (D)isplay projects\n"
    "- (F)ilter projects by date\n"
    "- (A)dd new project\n"
    "- (U)pdate project\n"
    "- (Q)uit")

def main():
    """Main program loop for Project Management."""
    print("Welcome to Pythonic Project Management")
    file_name = "projects.txt"
    projects = load_projects(file_name)
    print(f"Loaded {len(projects)} projects from {file_name}")
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "L":
            new_file_name = input("Filename: ")
            projects = load_projects(new_file_name)
            print(f"{len(projects)} projects loaded from {new_file_name}")
        elif choice == "S":
            save_name = input("Filename: ")
            save_projects(projects, save_name)
            print("Projects saved.")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filtered_projects = check_date(projects)
            for project in filtered_projects:
                print(project)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        print(MENU)
        choice = input(">>> ").upper()

def load_projects(file_name):
    """Load projects from file into a list of Project objects."""
    projects = []
    with open(file_name, "r") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            parts = line.strip().split("\t")
            record = Project(parts[0],parts[1],int(parts[2]),float(parts[3]),int(parts[4]))
            projects.append(record)
    return projects

def save_projects(projects, filename):
    """Save list of Project objects to file in tab-separated format."""
    with open(filename, "w") as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(Project.change_string(project) + "\n")

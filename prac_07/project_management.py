"""
Project Management
Estimate: 4 hours
Actual:   6 hours
"""

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

    save_choice = input(f"Would you like to save to {file_name}? ")
    if save_choice == "Y":
        save_projects(projects, file_name)
        print("Projects saved.")
    print("Thank you for using custom-built project management software.")

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

def category_project(projects):
    """Classify projects into complete and incomplete."""
    complete_project = []
    incomplete_project = []
    for project in projects:
        if project.is_complete():
            complete_project.append(project)
        else:
            incomplete_project.append(project)
    return complete_project, incomplete_project

def print_projects(title, projects):
    """Print a list of projects with a title, sorted by priority."""
    print(f"{title}:")
    for project in sorted(projects, key=attrgetter("priority")):
        print(f"  {project}")

def display_projects(projects):
    """Display incomplete and completed projects, sorted by priority."""
    complete_projects, incomplete_projects = category_project(projects)
    print_projects("Incomplete projects", incomplete_projects)
    print_projects("Completed projects", complete_projects)

def update_project(projects):
    """Allow user to select a project and update its completion and priority."""
    for index, project in enumerate(projects):
        print(f"{index} {project}")
    update_choice = get_valid_number("Project choice", len(projects) - 1)
    selected_project = projects[update_choice]
    print(selected_project)

    new_percentage = get_valid_number_allow_empty("New Percentage", MAX_NUMBER)
    if new_percentage is not None:
        selected_project.completion_percentage = new_percentage

    new_priority = get_valid_number_allow_empty("New Priority", MAX_PRIORITY)
    if new_priority is not None:
        selected_project.priority = new_priority

def get_valid_number(prompt, max_number):
    """Prompt for integer in valid range."""
    message = input(f"{prompt}: ")
    while not message.isdigit() or int(message) < MIN_NUMBER or int(message) > max_number:
        print(f"Invalid input; enter a number between {MIN_NUMBER} and {max_number}")
        message = input(f"{prompt}: ")
    return int(message)

def get_valid_number_allow_empty(prompt, max_number):
    """Allow user to skip by pressing Enter, or enter a valid number"""
    message = input(f"{prompt}: ").strip()
    if message == "":
        return None
    while not message.isdigit() or int(message) < MIN_NUMBER or int(message) > max_number:
        print(f"Invalid input; enter a number between {MIN_NUMBER} and {max_number}")
        message = input(f"{prompt}: ").strip()
        if message == "":
            return None
    return int(message)

def check_date(projects):
    """Filter projects starting on or after user-entered date."""
    filtered_projects = []
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    input_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    for project in projects:
        if project.date >= input_date:
            filtered_projects.append(project)
    return filtered_projects

def add_new_project(projects):
    """Add a new project to the current list (not saved yet)."""
    print("Let's add a new project")
    name = input("Name: ")
    date = input("Start date (dd/mm/yy): ")
    priority = get_valid_number("Priority", MAX_PRIORITY)
    cost = float(input("Cost estimate: $"))
    completion_percentage = get_valid_number("Percent complete", MAX_NUMBER)
    project = Project(name, date, priority, cost, completion_percentage)
    projects.append(project)

main()
"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    """Print all the data in a nested list and print subject details"""
    data = load_data()
    print(data)
    display_subject_details(data)

def load_data():
    """Read each line of data from the file and return all the data in a list"""
    subject_data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject_data.append(parts)
    input_file.close()
    return subject_data

def display_subject_details(subject_data):
    """Display subject details"""
    for data in subject_data:
        code, teacher, number_of_students = data
        print(f"{code} is taught by {teacher} and has {number_of_students} students")

main()
FILENAME = "wimbledon.csv"

def main():
    records = load_data()
def load_data():
    """Convert data in file into a list of lists"""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()[1:]
        for line in lines:
            data_parts = line.strip().split(", ")
            records.append(data_parts)
    return records





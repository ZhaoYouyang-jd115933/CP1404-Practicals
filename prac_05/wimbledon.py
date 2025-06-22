FILENAME = "wimbledon.csv"

def main():
    records = load_data()
    champions_to_count = count_champions(records)
    print(champions_to_count)

def load_data():
    """Convert data in file into a list of lists"""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()[1:]
        for line in lines:
            data_parts = line.strip().split(", ")
            records.append(data_parts)
    return records

def count_champions(records):
    """Extract champion name and count how many times they have won."""
    champions_to_count = {}
    for data_parts in records:
        champion = data_parts[2]
        if champion in champions_to_count:
            champions_to_count[champion] += 1
        else:
            champions_to_count[champion] = 1
    return champions_to_count

main()




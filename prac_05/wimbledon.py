FILENAME = "wimbledon.csv"

def main():
    """Print the number of wins of champions and print countries of all the champions in alphabetical order"""
    records = load_data()
    champions_to_count = count_champions(records)
    countries = get_countries(records)
    print("Wimbledon Champions:")
    for champion in champions_to_count:
        print(f"{champion} {champions_to_count[champion]}")

    sorted_countries = sorted(countries)
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted_countries))

def load_data():
    """Convert data in file into a list of lists"""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()[1:]
        for line in lines:
            data_parts = line.strip().split(",")
            records.append(data_parts)
    return records

def count_champions(records):
    """Extract champion name and count how many times they have won."""
    champions = extract_champion_and_country(records, 2)
    champions_to_count = {}
    for champion in champions:
        if champion in champions_to_count:
            champions_to_count[champion] += 1
        else:
            champions_to_count[champion] = 1
    return champions_to_count

def get_countries(records):
    """Get countries of all champions in a set"""
    countries_list = (extract_champion_and_country(records, 1))
    countries = set(countries_list)
    return countries

def extract_champion_and_country(records, index):
    """Extract champion and country from records and store each value in a separate list"""
    items = []
    for data_parts in records:
        items.append(data_parts[index])
    return items
main()




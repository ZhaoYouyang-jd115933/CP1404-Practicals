import random
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBER_OF_EACH_LINE = 6

number_of_quick_picks = int(input("How many quick picks? "))
for number in range(number_of_quick_picks):
    numbers = []
    while len(numbers) < NUMBER_OF_EACH_LINE:
        random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if random_number not in numbers:
            numbers.append(random_number)
    numbers.sort()
    print(" ".join(f"{number:2}" for number in numbers))

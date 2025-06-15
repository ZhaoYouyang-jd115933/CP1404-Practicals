NUMBER_OF_INPUTS = 5
numbers = []
for number in range(NUMBER_OF_INPUTS):
    enter_number = int(input("Number: "))
    numbers.append(enter_number)
average_number = sum(numbers) / len(numbers)
print(f"The first number is {numbers[0]}")
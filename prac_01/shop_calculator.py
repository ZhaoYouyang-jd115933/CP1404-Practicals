"""
DISCOUNT_RATE = 0.9
total_price = 0
get number_of_items
while number_of_items <= 0
    display "Invalid number of items!"
    get number_of_items
repeat number for number_of_items times
    get each_item_price
    total_price = total_price + each_item_price
if total_price > 100
    total_price = total_price * DISCOUNT_RATE
display number_of_items, total_price
"""
DISCOUNT_RATE = 0.9
total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for number in range(number_of_items):
    each_item_price = float(input("Price of item: "))
    total_price = total_price + each_item_price
if total_price > 100:
    total_price = total_price * DISCOUNT_RATE
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
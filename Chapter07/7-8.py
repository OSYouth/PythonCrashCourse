sandwich_orders = ['beef', 'tuna', 'durian']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich")
    finished_sandwiches.append(sandwich)

print("\nThese sandwiched had been made: ")
for sandwich in finished_sandwiches:
    print(sandwich)
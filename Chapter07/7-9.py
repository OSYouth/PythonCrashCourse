sandwich_orders = ['pastrami', 'beef', 'tuna', 'pastrami', 'durian', 'pastrami']
finished_sandwiches = []

print("The pastrami sandwich sold out! ")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich")
    finished_sandwiches.append(sandwich)

if 'pastrami' not in finished_sandwiches:
    print("\nThese sandwiched had been made: ")
    for sandwich in finished_sandwiches:
        print(sandwich)
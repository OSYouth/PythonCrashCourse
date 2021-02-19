def make_sandwich(*toppings):
    print("\nAdding these in sandwich: ")
    for topping in toppings:
        print("- " + topping)

make_sandwich("beef")
make_sandwich("beef", 'tomatto')
make_sandwich("beef", 'pegen', 'buzhidaojiaosha')
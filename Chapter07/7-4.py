prompt = "\nPlease enter some pizza toppings: "
prompt += "\nEnter 'quit' to end the program. "

while True:
    toppings = input(prompt)

    if toppings == 'quit':
        break

    print("We will adding " + toppings.title() + " in pizza!")
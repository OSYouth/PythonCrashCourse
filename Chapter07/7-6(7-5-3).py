prompt = "\nPlease enter your age! "
prompt += "\nYou could enter 'quit' if you want to end this program: "

while True:
    age = input(prompt)

    if age == 'quit':
        break
    else:
        age = int(age)

        if age < 3:
            price = 0
        elif age <= 12:
            price = 10
        else:
            price = 15

        print("\nThe price is " + str(price) + " dollars.")
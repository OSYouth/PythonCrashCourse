import json

filename = 'favorite_numbers.json'

try:
    with open(filename) as f_obj:
        number = json.load(f_obj)
except FileNotFoundError:
    number = input("Please input your favorite number: ")
else:
    print("I know your favorite number! It's " + number)
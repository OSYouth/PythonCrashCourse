import json

filename = 'favorite_numbers.json'
with open(filename) as f_obj:
    number = json.load( f_obj)

print("I know your favorite number! It's " + number)
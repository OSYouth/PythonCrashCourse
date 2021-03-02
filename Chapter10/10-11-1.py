import json

number = input("Please input your favorite number: ")

filename = 'favorite_numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)
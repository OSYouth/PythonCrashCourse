favorite_number = {
    'LC' : [7, 8],
    'YYQ' : [9, 10, 11],
    'LFK' : [8, 9, 10],
    'GJ' : [5, 6],
    'CMS' : [6],
}

for name, numbers in favorite_number.items():
    print(name.title() + "'s favorite number(s) is/are ")
    for number in numbers:
        print("\t" + str(number))
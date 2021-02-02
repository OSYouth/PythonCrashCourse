people = {
    'yyq': {
        'first_name': 'Yeqing',
        'last_name': 'YIN',
        'age': 25,
        'city': 'Changsha',
    },

    'cms': {
        'first_name': 'mengshan',
        'last_name': 'chen',
        'age': 29,
        'city': 'dongguan',
    },

    'hyf': {
        'first_name': 'yifeng',
        'last_name': 'huang',
        'age': 29,
        'city': 'Changsha',
    }
}

for name, info in people.items():
    print("Username: " + name)
    print("\tFull Name: " + info['last_name'].title() + " " + info['first_name'].title())
    print("\tAge: " + str(info['age']))
    print("\tCity: " + info['city'].title())
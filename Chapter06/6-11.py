cities = {
    'beijing': {
        'country': 'china',
        'population': 1111,
        'fact': 'large city, capital',
    },
    'newyork': {
        'country': 'america',
        'population': 999,
        'fact': 'trade center',
    },
    'paris': {
        'country': 'french',
        'population': 333,
        'fact': 'capital city',
    },
}

for name, info in cities.items():
    print(name.title() + " is in " + info['country'].title() + ".")
    print("\tPopolation: " + str(info['population']))
    print("\tFact: " + info['fact'])
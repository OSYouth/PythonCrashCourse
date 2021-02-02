pets = {
    'wangcai': {
        'type': 'dog',
        'host': 'LW'
    },
    'kitty': {
        'type': 'cat',
        'host': 'XL'
    }
}

for name, info in pets.items():
    print(name.title() + " is " + info['type'] +
          ", which belongs to " + info['host'] + ".")
favorite_places = {
    'lc': ['haerbin', 'aerbeisi'],
    'yyq': ['japan'],
    'hyf': ['home', 'loudi']
}

for name, places in favorite_places.items():
    print(name.title() + "'s favorite place(s) is /are ")
    for place in places:
        print("\t" + place.title())
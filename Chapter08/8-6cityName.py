def city_country(city, country):
    message = city + ", " + country
    return message.title()

line = city_country('santiagp', 'chile')
print(line)
line = city_country('beijing', 'china')
print(line)
line = city_country('shanghai', 'china')
print(line)

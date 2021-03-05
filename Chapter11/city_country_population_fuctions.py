def get_city_country_population(city, country, population=''):
    if population:
        ccp = city.title() + ', ' + country.title() + ' - population ' + population
    else:
        ccp = city.title() + ', ' + country.title()
    return ccp
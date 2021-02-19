def make_car(company, type, **car_info):
    info = {}
    info['compamy'] = company
    info['type'] = type
    for key, value in car_info.items():
        info[key] = value
    return  info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
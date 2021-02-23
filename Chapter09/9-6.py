class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name.title() + " is a(n) " + self.cuisine_type + " restaurant.")

    def open_restaurant(self):
        print("The restaurant is opening.")

    def set_number_served(self, person):
        self.number_served = person

    def increment_number_served(self, number):
        self.number_served += number

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['strawbeery', 'pear', 'banana']

    def display_ice_cream(self):
        print("There are these ice cream provided in " + self.restaurant_name + ":")
        for flavor in self.flavors:
            print("- " + flavor)

test = IceCreamStand("Häagen-Dazs", "desert")
test.display_ice_cream()
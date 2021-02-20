class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title() + " is a(n) " + self.cuisine_type + " restaurant.")

    def open_restaurant(self):
        print("The restaurant is opening.")

pc = Restaurant("xiaojiangnan", "Chinese food")
print(pc.restaurant_name)
print(pc.cuisine_type)
pc.describe_restaurant()
pc.open_restaurant()
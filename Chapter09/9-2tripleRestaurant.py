class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title() + " is a(n) " + self.cuisine_type + " restaurant.")

    def open_restaurant(self):
        print("The restaurant is opening.")

qjn = Restaurant("qiaojiangnan", "Chinese food")
xng = Restaurant("xiaonanguo", "Chinese food")
ydc = Restaurant("yinducai", "Indian food")

qjn.describe_restaurant()
xng.describe_restaurant()
ydc.describe_restaurant()

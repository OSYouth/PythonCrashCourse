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

pc = Restaurant("xiaojiangnan", "Chinese food")
print("There are " + str(pc.number_served) + " people have been served in " + pc.restaurant_name)

pc.number_served = 7
print("There are " + str(pc.number_served) + " people have been served in " + pc.restaurant_name)

pc.set_number_served(88)
print("There are " + str(pc.number_served) + " people have been served in " + pc.restaurant_name)

pc.increment_number_served(13)
print("There are " + str(pc.number_served) + " people have been served in " + pc.restaurant_name)

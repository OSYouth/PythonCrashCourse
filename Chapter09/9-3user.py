class User():

    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name

    def describe_user(self):
        print(self.fname.title() + self.lname.title())

    def greet_user(self):
        print("Welcome you login in!")

lc = User("chi", "li")
yyq = User("yeqing", "yin")

lc.describe_user()
lc.greet_user()

yyq.describe_user()
yyq.greet_user()
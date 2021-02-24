class User():

    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(self.fname.title() + self.lname.title())

    def greet_user(self):
        print("Welcome you login in!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
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

class Privileges():
    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        print("The admin's privileges including below: ")
        for privilege in self.privileges:
            print("- " + privilege)

class Admin(User):
    def __init__(self, first_name, last_name):
        # super(Admin, self).__init__(first_name, last_name)
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

lc = Admin("chi", "li")

lc.privileges.show_privileges()

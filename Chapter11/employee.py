class Employee():

    def __init__(self, fname, lname, annual_salary):
        self.first_name = fname
        self.last_name = lname
        self.annual_salary = annual_salary

    def give_raise(self, raise_salary=5000):
        self.annual_salary = self.annual_salary + raise_salary
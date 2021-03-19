import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('Chi', 'LI', 10000)

    def test_give_default_raise(self):
        new_salary = self.employee.annual_salary + 5000
        self.employee.give_raise()
        self.assertEqual(new_salary, self.employee.annual_salary)

    def test_give_custom_raise(self):
        new_salary = self.employee.annual_salary + 8000
        self.employee.give_raise(8000)
        self.assertEqual(new_salary, self.employee.annual_salary)

unittest.main()
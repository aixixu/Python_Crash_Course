import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        firstname = 'Cohen'
        lastname = 'xu'
        salary = 4000
        self.employee = Employee(firstname,lastname,salary)
        self.result1 = 9000
        self.result2 = 5000
        
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.result1, self.employee.salary)
    
    def test_give_custom_raise(self):
        self.employee.give_raise(1000)
        self.assertEqual(self.result2, self.employee.salary)

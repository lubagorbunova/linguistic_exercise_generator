import unittest
from src.exercise import TextProcessor


class EmployeeBaseTests(unittest.TestCase):

    def test_create_employee_ideal(self):
        instance = TextProcessor('кошка спит на диване!')
        self.assertEqual(instance.get_raw_text())
        self.assertEqual(instance.get_raw_text())

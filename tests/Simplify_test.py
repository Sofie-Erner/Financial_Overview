import unittest
import numpy as np
import os
import sys

path = os.path.abspath(os.getcwd()) # path to directory of script
sys.path.append("../")

import src
from src.Get_expense_categories import GetExpenseCategory
from src.Simplify_statement import SimplifyStatement

class SimplifyTest(unittest.TestCase):
    """
    SimplifyTest class to test the simplification of bank statements.
    The expenses will be categorised.
    """
    def test_function(self):
        pass

class ExpenseCategoriesTest(unittest.TestCase):
    """
    ExpenseCategoriesTest class to test the import of expense categories
    """
    def setUp(self):
        """ Test result of function and list of keys to compare to """
        self.keys_expected = ['entertaintment', 'personal', 'unknown', 'travel', 'groceries', 'eating_out', 'shopping', 'bills']
        self.dict_result = GetExpenseCategory("Test_expenses_categories.csv")

    def test_GetExpenseCategory_dict(self):
        """ Test output is a dictionary """
        self.assertIs(type(self.dict_result),dict)

    def test_GetExpenseCategory_keys(self):
        """ Test output keys matches """
        self.assertListEqual(list(self.dict_result.keys()),self.keys_expected)

    def test_GetExpenseCategory_output(self):
        """ Test output first column"""
        self.assertListEqual(list(self.dict_result["entertaintment"]),['netflix'])

if __name__ == "__main__":
    unittest.main()

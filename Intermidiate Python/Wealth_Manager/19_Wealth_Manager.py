import unittest
from test_class import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.balance = BankAccount(100)

    def tearDown(self):
        self.balance = None

    def test_initial_balance(self):
        self.assertEqual(self.balance.balance, 100)
        self.assertNotEqual(self.balance.balance, 0)
        self.assertNotEqual(self.balance.balance, -100)

    def test_deposit_positive_amount(self):
        self.balance.deposit(50)
        self.assertEqual(self.balance.balance, 150)
        with self.assertRaises(ValueError):
            self.balance.deposit(0)

if __name__ == '__main__':
    unittest.main()
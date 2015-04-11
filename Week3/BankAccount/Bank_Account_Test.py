import unittest
from bankaccount import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.my_account = BankAccount("Ivo", 100000, "$")

    def test_init(self):
        self.assertEqual(self.my_account.name, "Ivo")
        self.assertEqual(self.my_account._balance, 100000)
        self.assertEqual(self.my_account.currency, "$")

    def test_str(self):
        needed_result = "Bank account for Ivo with balance of 100000$"
        self.assertEqual(str(self.my_account), needed_result)

    def test_deposit(self):
        self.my_account.deposit(100)
        self.assertEqual(self.my_account._balance, 100100)
        with self.assertRaises(ValueError):
            self.my_account.deposit(-20)

        self.assertEqual(self.my_account._balance, 100100)

    def test_transfer_to_different_currency(self):
        your_account = BankAccount("Rado", 10, "&")

        with self.assertRaises(ValueError):
            self.my_account.transfer_to(your_account, 200)
        self.assertEqual(self.my_account._balance, 100000)
        self.assertEqual(your_account._balance, 10)

    def test_transfer_to_more_money_that_we_have(self):
        your_account = BankAccount("Rado", 10, "$")

        self.assertTrue(your_account.transfer_to(self.my_account, 300))
        self.assertEqual(self.my_account._balance, 100300)
        self.assertEqual(your_account._balance, -290)

    def test_transfer_to(self):
        your_account = BankAccount("Rado", 10, "$")
        result = self.my_account.transfer_to(your_account, 300)
        self.assertTrue(result)
        self.assertEqual(your_account._balance, 310)
        self.assertEqual(self.my_account._balance, 100000 - 300)



if __name__ == "__main__":
    unittest.main()

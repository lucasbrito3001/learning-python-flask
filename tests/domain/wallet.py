import unittest

from api.domain.wallet import Wallet
from api.exception.wallet import InvalidValueError

class TestWalletAddBalance(unittest.TestCase):
    def test_raise_invalid_value_error_when_its_negative(self):
        with self.assertRaises(InvalidValueError):
            wallet = Wallet(None)
            wallet.add_balance(float(-100))

    def test_raise_invalid_value_error_when_its_equals_zero(self):
        with self.assertRaises(InvalidValueError):
            wallet = Wallet(None)
            wallet.add_balance(float(0))

    def test_raise_invalid_value_error_when_its_not_a_number(self):
        with self.assertRaises(InvalidValueError):
            wallet = Wallet(None)
            wallet.add_balance("invalid_value")

    def test_add_balance_successfully(self):
        wallet = Wallet(None)
        wallet.add_balance(float(100))
        
        self.assertEqual(wallet._balance, 100)
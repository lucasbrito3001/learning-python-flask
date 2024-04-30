class InvalidValueError(Exception):
    def __init__(self):          
        self.message = 'Invalid value, must be a number greater than zero.'
        self.errors = []

class WalletNotFoundError(Exception):
    def __init__(self):
        self.message = 'Wallet not found.'
        self.errors = []

class InsufficientBalanceError(Exception):
    def __init__(self):
        self.message = 'Insufficient balance to perform this transaction.'
        self.errors = []

class MissingValueError(Exception):
    def __init__(self):
        self.message = 'Missing the value in the request body.'
        self.errors = []
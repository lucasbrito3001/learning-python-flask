import uuid

from api.exception.wallet import InsufficientBalanceError, InvalidValueError

class Wallet(object):
    def __init__(self, initial_balance: float):
        self._balance = initial_balance or float(0)
        self._uuid = str(uuid.uuid4())

    def __str__(self):
        return f"Id: {self._uuid} | Balance: {self._balance}"


    def add_balance(self, value: float) -> None:
        if type(value) is not float or value <= 0:
            raise InvalidValueError()
        
        self._balance += value
    
    def withdraw(self, value: float) -> None:
        if type(value) is not float or value <= 0:
            raise InvalidValueError()
        
        if value > self._balance:
            raise InsufficientBalanceError()
        
        self._balance -= value
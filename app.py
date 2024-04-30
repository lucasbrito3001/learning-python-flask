from uuid import UUID
from flask import Flask, request

from api.domain.wallet import Wallet
from api.exception.wallet import InvalidValueError, MissingValueError, WalletNotFoundError, InsufficientBalanceError
from api.repository.wallet import WalletRepository

app = Flask(__name__)
walletRepository = WalletRepository()

@app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get("/healthy")
def health_check():
    return { "status": "healthy" }

@app.post("/create-wallet")
def create_wallet():
    try:
        wallet = Wallet(None)

        walletRepository.add(wallet)
        
        return { "status": True, "data": { "id": wallet._uuid } }, 201
    except:
        return { "status": False, "error": { "message": "Internal error" } }, 500
    
@app.put("/add-balance/<wallet_id>")
def add_balance(wallet_id):
    try:
        body = request.get_json()
        
        value_to_add = body.get("value")
        
        if value_to_add is None:
            raise MissingValueError()

        wallet = walletRepository.get(str(wallet_id))
        
        if wallet is None:
            raise WalletNotFoundError()
            
        wallet.add_balance(float(value_to_add))

        walletRepository.update(wallet)

        return { "status": True, "data": { "balance": wallet._balance } }, 200
    except (WalletNotFoundError, InvalidValueError, MissingValueError) as error:
        return { "status": False, "error": { "message": error.message, "errors": error.errors } }, 400
    except:
        return { "status": False, "error": { "message": "Internal error" } }, 500
    
@app.put("/withdraw/<wallet_id>")
def withdraw(wallet_id):
    try:
        body = request.json

        if body["value"] is None:
            raise MissingValueError()

        wallet = walletRepository.get(str(wallet_id))
        wallet.withdraw(body["value"])

        walletRepository.update(wallet)

        return { "status": True, "data": { "balance": wallet._balance } }, 200
    except (InvalidValueError, WalletNotFoundError, InsufficientBalanceError, MissingValueError) as error:
        return { "status": False, "error": { "message": error.message, "errors": error.errors } }, 400
    except:
        return { "status": False, "error": { "message": "Internal error" } }, 500
    
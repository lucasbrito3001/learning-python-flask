from uuid import UUID
from api.domain.wallet import Wallet


class WalletRepository:
    def __init__(self):
        self.wallets = dict()

    def get(self, walletId: UUID) -> Wallet | None:
        return self.wallets.get(walletId)
    
    def add(self, wallet: Wallet) -> None:
        self.wallets[wallet._uuid] = wallet

    def update(self, wallet: Wallet) -> None:
        self.wallets[wallet._uuid] = wallet
    
    def remove(self, walletId: UUID) -> None:
        del self.wallets[walletId]
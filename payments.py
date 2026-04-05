from base import BasePayment

class CreditCard(BasePayment):
    def __init__(self,card_number: str):
        self.card_number = card_number

    def __str__(self):
        return self.card_number


    def pay(self,amount: float) -> bool:
       print(f"${amount} paid using credit card {self.card_number}")
       return True


class CryptoPayment(BasePayment):
    def __init__(self,wallet_address: str):
        self.wallet_address = wallet_address

    def pay(self,amount: float ) -> bool:
        print(f"{amount} paid using crypto {self.wallet_address}")
        return True

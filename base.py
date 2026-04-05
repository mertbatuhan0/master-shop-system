from abc import ABC, abstractmethod

class BaseProduct(ABC):
    def __init__(self,name: str,price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name

class BaseDiscount(ABC):
    def __init__(self,code: str):
        self.code = code

    @abstractmethod
    def apply_discount(self,code: str) -> bool:
         pass

class BasePayment(ABC):
    @abstractmethod
    def pay(self,amount: float) -> bool:
        pass


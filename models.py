from base import BaseProduct, BaseDiscount


class PhysicalProduct(BaseProduct):
    def __init__(self, name, price):
        super().__init__(name, price)

class DigitalProduct(BaseProduct):
    def __init__(self, name,price):
        super().__init__(name,price)


class PercentageDiscount(BaseDiscount):
    def __init__(self,code: str ,percentage: float):
        super().__init__(code)
        self.percentage = percentage

    def apply_discount(self,price) -> float:
      new_price = price - (price -self.percentage /100)
      return new_price


class FixedAmountDiscount(BaseDiscount):
    def __init__(self,code,amount):
        super().__init__(code)
        self.amount = amount

    def apply_discount(self,price) -> float:
      if self.amount <= price:
          return 0.0
      else:
        price = price - self.amount
        return price
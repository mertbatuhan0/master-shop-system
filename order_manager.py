
class Order:
    def __init__(self):
        self.products = []

    def add_product(self,product):
         self.products.append(product)
         print(f"{product.name} added to order")

    def calculate_total_price(self) -> float:
        total_price = 0
        for h in self.products:
            total_price += h.price
        return total_price


    def process_checkout(self,payment,discount=None):
        current_price = self.calculate_total_price()
        if discount:
            current_price -= discount.apply_discount(current_price)

        if payment.pay(current_price):
            print(f"Credit Card (No: {payment}) is used for payment.")









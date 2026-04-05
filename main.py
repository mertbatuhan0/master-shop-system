from models import PhysicalProduct, DigitalProduct, PercentageDiscount
from payments import CreditCard
from order_manager import Order

def main():
    iphone = PhysicalProduct("iPhone 17", 50000.0)
    ebook = DigitalProduct("Python Programming", 250.0)

    promo = PercentageDiscount("SAVE10", 10)
    my_card = CreditCard("1234-5678-9012-3456")

    shop_order = Order()

    shop_order.add_product(iphone)
    shop_order.add_product(ebook)

    shop_order.process_checkout(my_card, promo)

if __name__ == "__main__":
    main()
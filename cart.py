class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)

    def total_cart_value(self):
        return sum(p.price for p in self.cart_items)

    def display_cart(self):
        print("Cart Contents:")
        for item in self.cart_items:
            item.display_info()
            
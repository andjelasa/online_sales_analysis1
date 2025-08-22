from product import Product
from product_manager import ProductManager
from cart import Cart 

pm = ProductManager()
pm.add_product(Product("Laptop", 1000, 3))
pm.add_product(Product("Phone", 500, 5))
pm.add_product(Product("Tablet", 700, 2))

pm.view_all_products()
print(f"Total Inventory Value: ${pm.total_value()}")

cart = Cart()
cart.add_to_cart(pm.products[0])
cart.add_to_cart(pm.products[1])
cart.add_to_cart(pm.products[2])

cart.display_cart()
print(f"Total Cart Value: ${cart.total_cart_value()}")

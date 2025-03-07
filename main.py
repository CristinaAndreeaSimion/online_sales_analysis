
from product import Product
from product_manager import ProductManager

if __name__ == "__main__":
    manager = ProductManager()
    
    product1 = Product("Laptop", 1500, 10)
    product2 = Product("Mouse", 50, 100)
    product3 = Product("Keyboard", 80, 50)
    
    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)
    
    print("All Products:")
    manager.display_products()
    print(f"Total Inventory Value: {manager.total_inventory_value()}")
    
    cart = Cart()
    cart.add_to_cart(product1)
    cart.add_to_cart(product2)
    cart.add_to_cart(product3)
    
    print("\nCart Items:")
    cart.display_cart()
    print(f"Total Cart Value: {cart.total_cart_value()}")


    
    
    
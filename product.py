# Define a Python class named 'Product'.
class Product:
    # Constructor method that initializes a 'Product' object with provided attributes.
    def __init__(self, product_id, name, price, quantity):
        """
        Args :
              Product_Id, name, price, quantity
        """  
        # Store the 'product_id' attribute for this product instance.
        self.product_id = product_id
        # Store the 'name' attribute for this product instance.
        self.name = name
        # Store the 'price' attribute for this product instance.
        self.price = price
        # Store the 'quantity' attribute for this product instance.
        self.quantity = quantity

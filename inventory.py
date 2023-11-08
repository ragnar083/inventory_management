# Import the 'pandas' library as 'pd' for data manipulation.
import pandas as pd

# Import the 'product' module which has  the 'Product' class.
import product

# Define a Python class named 'InventoryManagementSystem'.
class InventoryManagementSystem:
    # Constructor method that initializes the inventory and file name attributes, and loads the inventory from a file.
    def __init__(self, file_name='inventory.csv'):
        # Initialize an empty dictionary to store product information.
        self.inventory = {}
        # Store the file name for inventory data.
        self.file_name = file_name
        # Load inventory data from the file 
        self.load_inventory()

    # Method to add a new product to the inventory.
    def add_product(self, product_id, name, price, quantity):
        # Check if the product ID already exists in the inventory.
        if product_id in self.inventory:
            print("Product with this ID already exists.")
        else:
            # Create a new 'Product' object and add it to the inventory dictionary.
            self.inventory[product_id] = product.Product(product_id, name, price, quantity)
            # Save the updated inventory to the file.
            self.save_inventory()
            print("Product added successfully.")

    # Method to update product details based on product ID and a field (name, price, or quantity).
    def update_product(self, product_id, field, new_value):
        # Check if the product ID exists in the inventory.
        if product_id in self.inventory:
            # Get the product object from the inventory.
            product_obj = self.inventory[product_id]
            # Check if the specified field exists as an attribute in the 'Product' class.
            if hasattr(product_obj, field):
                # Update the specified field with the new value.
                setattr(product_obj, field, new_value)
                # Save the updated inventory to the file.
                self.save_inventory()
                print("Product updated successfully.")
            else:
                print("Invalid field name.")
        else:
            print("Product not found.")

    # Method to delete a product from the inventory based on the product ID.
    def delete_product(self, product_id):
        # Check if the product ID exists in the inventory.
        if product_id in self.inventory:
            # Remove the product from the inventory.
            del self.inventory[product_id]
            # Save the updated inventory to the file.
            self.save_inventory()
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    # Method to display the details of available products in the inventory.
    def display_products(self):
        # looping through the loaded data for displaying
        for product_id, product in self.inventory.items():
            print(f"Product ID: {product_id}, Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")
            print(20*"-")

    # Method to load inventory data from a CSV file.
    def load_inventory(self):
        try:
            # Attempt to read data from the specified CSV file.
            data = pd.read_csv(self.file_name)
            # Iterate through the data and create 'Product' objects for each entry, storing them in the inventory.
            for index, row in data.iterrows():
                self.inventory[row['product_id']] = product.Product(row['product_id'], row['name'], row['price'], row['quantity'])
        except FileNotFoundError:
            # Handle the case where no inventory data file is found.
            print("No inventory data found. Starting with an empty inventory.")

    # Method to save the current inventory to a CSV file.
    def save_inventory(self):
        # Create a dictionary to store data for saving to the CSV file.
        data = {'product_id': [], 'name': [], 'price': [], 'quantity': []}
        # Iterate through the inventory and populate the data dictionary with product information.
        for product_id, product in self.inventory.items():
            data['product_id'].append(product_id)
            data['name'].append(product.name)
            data['price'].append(product.price)
            data['quantity'].append(product.quantity)
        # Create a DataFrame from the data dictionary and save it to the specified CSV file.
        df = pd.DataFrame(data)
        df.to_csv(self.file_name, index=False)

# Import the 'inventory' module, prsent in same directory which has inventoryManagementSystem class
import inventory

# Define the main function.
def main():
    # Create an instance of the InventoryManagementSystem class.
    ims = inventory.InventoryManagementSystem()

    # Start an while loop for user interaction.
    while True:
        # Print a menu of options for the user.
        print("\nOptions:") #
        print("1. Add a new product") # This OPtion is used to add a new product into Inventory.
        print("2. Update product details") # This OPtion is used to updated an existing product in the Inventory.
        print("3. Delete a product") # This OPtion is used to Delete an Existing product in the  Inventory.
        print("4. Display available products") # This OPtion is used to Display all the Existing products in the Inventory.
        print("5. Quit") # this Option used to quit from the Application
        # try except block to handdle the user input errors
        try:
            # Attempt to get the user's choice as an integer.
            choice = int(input("Enter your choice: "))
        except:
            # Handle an exception if the input is not a valid integer.
            print("Enter a valid number between 1 - 5")
            continue # if error is occured starting a new iteration

        # Check the user's choice and perform the corresponding action.
        if choice == 1:
            try:
                # Get the product ID as an integer and validate it.
                product_id = int(input("Enter product ID: "))
                if product_id < 1: # checking if the entered price is less than 1
                    raise ValueError # raising a value error if price less than 1
            except ValueError:
                # Handle an exception if the input is not a valid integer.
                print("Enter a valid integer for product Id")
                continue # if error is occured starting a new iteration
            name = input("Enter product name: ") # taking the name of the product
            try:
                # Get the product price as a float and validate it.
                price = float(input("Enter product price: "))
                if price < 0:
                    raise ValueError
                # Get the product quantity as an integer and validate it.
                quantity = int(input("Enter product quantity: "))
                if quantity < 0: # checking the quantity is it less than 0
                    raise ValueError  # raising an error if value is less than 0
            except ValueError:
                # Handle an exception if the input is not a valid float or integer.
                print("Enter valid details")
                continue # if error is occured starting a new iteration

            # Call the 'add_product' method with the provided details.
            ims.add_product(product_id, name, price, quantity)
        elif choice == 2:
            try:
                # Get the product ID as an integer and validate it.
                product_id = int(input("Enter product ID: "))
                if product_id < 1:
                    raise ValueError # raisning an error if product id is less than 1
            except ValueError:
                # Handle an exception if the input is not a valid integer.
                print("Enter a valid integer for product Id")
                continue # if error is occured starting a new iteration
            # Get the field and new value for updating the product.
            field = input("Enter the field to update (name, price, quantity): ")
            new_value = input(f"Enter new value for {field}: ")
            # Call the 'update_product' method with the provided details.
            ims.update_product(product_id, field, new_value)
        elif choice == 3:
            try:
                # Get the product ID as an integer and validate it.
                product_id = int(input("Enter product ID: "))
                if product_id < 1: 
                    raise ValueError # raisning an error if product id is less than 1
            except ValueError:
                # Handle an exception if the input is not a valid integer.
                print("Enter a valid integer for product Id")
                continue # if error is occured starting a new iteration
            # Call the 'delete_product' method with the provided product ID.
            ims.delete_product(product_id)
        elif choice == 4:
            # Call the 'display_products' method to show available products.
            ims.display_products()
        elif choice == 5:
            # Exit the loop and terminate the program if the user chooses to quit.
            break
        else:
            # Handle invalid choices.
            print("Invalid choice. Please select a valid option.")

# Check if the script is being run as the main program.
if __name__ == '__main__':
    # Call the 'main' function to start the program.
    main()

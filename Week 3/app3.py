import os

# I'm using text files to save everything so we don't lose data when the app closes
PRODUCTS_FILE = "products.txt"
COURIERS_FILE = "couriers.txt"
ORDERS_FILE = "orders.txt"  # Added this for orders, might use it later

# This function helps me read stuff from files - learnt this from my Python course
def load_data(filename):
    # First check if the file exists to avoid errors on first run
    if os.path.exists(filename):
        with open(filename, "r") as file:
            # This grabs each line and strips any extra spaces/newlines
            return [line.strip() for line in file.readlines()]
    return []  # Return empty list if file doesn't exist yet

# I created this function to save our lists back to the files
def save_data(filename, data_list):
    with open(filename, "w") as file:
        # Each item gets its own line in the file
        for item in data_list:
            file.write(f"{item}\n")

# Load everything when the programme starts
products = load_data(PRODUCTS_FILE)
couriers = load_data(COURIERS_FILE)
orders = []  # I'm starting with empty orders for now

# These functions handle all the product stuff

# Shows all products with numbers
def view_products():
    print("\n----- Product List -----")
    if products:
        for index, product in enumerate(products):
            print(f"{index}. {product}")
    else:
        # In case we don't have any products yet
        print("No products available...")

# Adds a new product to our list
def add_product():
    name = input("\nEnter product name: ")
    # Had a bug before where empty names were being added - this fixes that
    if name.strip():
      products.append(name)
      print(f"Product '{name}' added successfully!")
    else:
        print("Product name cannot be empty...")

# Updates existing products
def update_product():
    view_products()
    if not products:
        return  # Nothing to update
        
    index = input("\nEnter product number to update: ")
    # Making sure the number makes sense - got errors before when I didn't check this!
    if index.isdigit() and 0 <= int(index) < len(products):
        new_name = input(f"Enter new name for '{products[int(index)]}' (or press enter to keep current): ")
        if new_name.strip():
            products[int(index)] = new_name
            print("Product updated successfully!")
    else:
        print("Invalid product number...")

# Removes a product from the list
def delete_product():
    view_products()
    if not products:
        return  # No products to delete
        
    index = input("\nEnter product number to delete: ")
    # Again checking the number is valid
    if index.isdigit() and 0 <= int(index) < len(products):
        removed = products.pop(int(index))
        print(f"Product '{removed}' deleted successfully...")
    else:
        print("Invalid product number...")

# Now for the courier functions - they're similar to the product ones
def view_couriers():
    print("\n--- Courier List ---")
    if couriers:
        for index, courier in enumerate(couriers):
            print(f"{index}. {courier}")
    else:
        print("No couriers available...")

def add_courier():
    name = input("\nEnter courier name: ")
    if name.strip():
        couriers.append(name)
        print(f"Courier '{name}' added successfully!")
    else:
        print("Courier name cannot be empty...")

def update_courier():
    view_couriers()
    if not couriers:
        return
        
    index = input("\nEnter courier number to update: ")
    if index.isdigit() and 0 <= int(index) < len(couriers):
        new_name = input(f"Enter new name for '{couriers[int(index)]}' (or press enter to keep current): ")
        if new_name.strip():
            couriers[int(index)] = new_name
            print("Courier updated successfully!")
    else:
        print("Invalid courier number...")

def delete_courier():
    view_couriers()
    if not couriers:
        return
        
    index = input("\nEnter courier number to delete: ")
    if index.isdigit() and 0 <= int(index) < len(couriers):
        removed = couriers.pop(int(index))
        print(f"Courier '{removed}' deleted successfully!")
    else:
        print("Invalid courier number...")

# Order functions are more complicated because orders have more info
def view_orders():
    print("\n- Order List ---")
    if orders:
        for index, order in enumerate(orders):
            print(f"\nOrder #{index}:")
            # I'm looping through each bit of info in the order
            for key, value in order.items():
                if key == "courier":
                    # Show the courier name instead of just a number - more user-friendly this way
                    courier_name = couriers[value] if 0 <= value < len(couriers) else "Unknown"
                    print(f"  Courier: {courier_name} (#{value})")
                else:
                    # This makes it look nicer by capitalising the labels and removing underscores
                    print(f"  {key.replace('_', ' ').title()}: {value}")
    else:
        print("No orders available...")

def create_order():
    # Need couriers before we can create an order
    if not couriers:
        print("No couriers available. Please add a courier first...")
        return
    
    # Getting all the customer details
    customer_name = input("\nEnter customer name: ")
    customer_address = input("Enter customer address: ")
    customer_phone = input("Enter customer phone: ")
    
    # Let them pick a courier from the list
    view_couriers()
    courier_index = input("Enter courier number: ")
    
    if courier_index.isdigit() and 0 <= int(courier_index) < len(couriers):
        # Using a dictionary to store all the order details together
        new_order = {
            "customer_name": customer_name,
            "customer_address": customer_address,
            "customer_phone": customer_phone,
            "courier": int(courier_index),
            "status": "Preparing"  # All new orders start as "Preparing"
        }
        orders.append(new_order)
        print("Order created successfully!")
    else:
        print("Invalid courier selection...")

def update_order_status():
    view_orders()
    if not orders:
        return
        
    index = input("\nEnter order number to update status: ")

    if index.isdigit() and 0 <= int(index) < len(orders):
        # I chose these 3 status options but we could add more later
        print("\nOrder Status Options: 0 - Preparing, 1 - Shipped, 2 - Delivered")
        status_choice = input("Enter status number: ")

        status_options = ["Preparing", "Shipped", "Delivered"]
        if status_choice.isdigit() and 0 <= int(status_choice) < len(status_options):
            orders[int(index)]["status"] = status_options[int(status_choice)]
            print("Order status updated successfully.")
        else:
            print("Invalid status selection.")
    else:
        print("Invalid order number.")

def update_order():
    view_orders()
    if not orders:
        return
        
    index = input("\nEnter order number to update: ")
    if index.isdigit() and 0 <= int(index) < len(orders):
        order = orders[int(index)]
        
        # I made it so you can just press enter to skip updating a field
        name = input(f"Enter new customer name (current: {order['customer_name']}) or press enter to skip: ")
        if name.strip():
            order["customer_name"] = name
        
        address = input(f"Enter new address (current: {order['customer_address']}) or press enter to skip: ")
        if address.strip():
            order["customer_address"] = address
        
        phone = input(f"Enter new phone (current: {order['customer_phone']}) or press enter to skip: ")
        if phone.strip():
            order["customer_phone"] = phone
        
        # I'm showing all couriers so the user can pick one by the index number
        view_couriers()
        courier = input(f"Enter new courier number (current: {order['courier']}) or press enter to skip: ")
        # Making sure the courier index is valid - don't want the app to crash :0
        if courier.isdigit() and 0 <= int(courier) < len(couriers):
            order["courier"] = int(courier)
        
        print("Order updated successfully!")
    else:
        print("Invalid order number...")

def delete_order():
    # First show all orders so the user knows what they can delete
    view_orders()
    if not orders:
        # If there's nothing to delete, just go back to the menu
        return
        
    index = input("\nEnter order number to delete: ")
    # Got to check if the number makes sense ;)
    if index.isdigit() and 0 <= int(index) < len(orders):
        orders.pop(int(index))
        print("Order deleted successfully!")
    else:
        print("Invalid order number..")

# I set up these menu functions to make the code more organised
# Each handles its own section so the main code isn't massive
def product_menu():
    while True:
        # Simple menu layout that's easy to follow
        print("\n--- Product Menu ---")
        print("1. View all products")
        print("2. Add a product")
        print("3. Update a product")
        print("4. Delete a product")
        print("0. Return to main menu")
        
        choice = input("\nEnter your choice: ")
        
        # Call the right function based on what the user picked
        if choice == "1":
            view_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            update_product()
        elif choice == "4":
            delete_product()
        elif choice == "0":
            break  # Go back to main menu
        else:
            print("Invalid choice. Please try again...")

def courier_menu():
    while True:
        print("\n--- Courier Menu ---")
        print("1. View all couriers")
        print("2. Add a courier")
        print("3. Update a courier")
        print("4. Delete a courier")
        print("0. Return to main menu")
        
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            view_couriers()
        elif choice == "2":
            add_courier()
        elif choice == "3":
            update_courier()
        elif choice == "4":
            delete_courier()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again...")

def order_menu():
    while True:
        print("\n--- Order Menu ---")
        print("1. View all orders")
        print("2. Create an order")
        print("3. Update order status")
        print("4. Update order details")
        print("5. Delete an order")
        print("0. Return to main menu")
        
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            view_orders()
        elif choice == "2":
            create_order()
        elif choice == "3":
            update_order_status()
        elif choice == "4":
            update_order()
        elif choice == "5":
            delete_order()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again...")

# This is where everything starts - the main menu that controls everything else
def main_menu():
    while True:
        print("\n------- Main Menu -------")
        print("1. Products")
        print("2. Couriers")
        print("3. Orders")
        print("0. Exit and Save")
        
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            product_menu()
        elif choice == "2":
            courier_menu()
        elif choice == "3":
            order_menu()
        elif choice == "0":
            # We need to save everything before exiting
            # I'm only saving products and couriers now, might add orders later
            save_data(PRODUCTS_FILE, products)
            save_data(COURIERS_FILE, couriers)
            print("Data saved successfully. Exiting...")
            break
        else:
            print("Invalid choice. Please try again...")

# This bit is important.. It makes sure the program starts from the main menu
# I found this pattern online and it's a good way to structure Python programs
if __name__ == "__main__":
    main_menu()
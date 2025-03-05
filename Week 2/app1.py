# First I need the list of my products and orders for when new ones are created and filled 
products = ["Mocha", "Americano", "Expresso", "Latte"]
orders = []

# I'll be using a function for the main menu and run a while true loop to make it run infinitely and print the menu options
def main_menu():
    while True:
        print("\nMain Menu")
        print("1 - Product Menu")
        print("2 - Order Menu")
        print("0 - Exit")
        
        # Depending on what the user chooses, like if they pick 0, it ends the loop.
        # If they pick 1, the loop jumps to the product menu.
        choice = input("\nEnter your choice: ")

        if choice == "0":
            print("Exiting program...")
            break
        elif choice == "1":
            product_menu()
        elif choice == "2":
            order_menu()
        else:
            print("Invalid choice, please try again...")

# Function to display the product menu when user picks 1 on the main menu 
def product_menu():
    while True:
        print("\nProduct Menu")
        print("1 - View Products")
        print("2 - Add New Product")
        print("3 - Update Existing Product")
        print("4 - Delete Product")
        print("0 - Return to Main Menu")

        # They will be prompted to pick an option like viewing products or updating them.
        product_choice = input("\nEnter your choice: ")

        if product_choice == "0":
            break  # Exits the product menu and returns to main menu
        elif product_choice == "1":
            view_products()
        elif product_choice == "2":
            add_product()
        elif product_choice == "3":
            update_product()
        elif product_choice == "4":
            delete_product()
        else:
            print("Invalid choice, please try again...")

# This is a function for them to view each of the products from the list with the correct indexing
def view_products():
    print("\nProduct List:")
    for i in range(len(products)):  # Loops through the list to show each product with a number
        print(i, "-", products[i])

# Function to add a new product
def add_product():
    new_product = input("\nEnter product name: ")  # Ask the user for a new product name
    products.append(new_product)  # Adds it to the product list
    print(f'"{new_product}" has been added! :)')

# Function to update a product
def update_product():
    view_products()  # Show the current products first
    index = input("\nEnter the product number to update: ")

    # Making sure the input is a number
    if index.isdigit():
        index = int(index)  
        if 0 <= index < len(products):  # Checking if the number is valid within the list
            products[index] = input("Enter new product name: ")  # Replace old product with new one
            print("Product updated successfully!")
        else:
            print("Invalid selection")
    else:
        print("Please enter a valid number...")

# Function to delete a product
def delete_product():
    view_products()  # Show products before deleting
    remove_product = input("\nEnter the product number to delete: ")

    if remove_product.isdigit():
        remove_product = int(remove_product)
        if 0 <= remove_product < len(products):  # Checking if the index exists in the list
            removed_item = products.pop(remove_product)  # Fully removes the product
            print(f'"{removed_item}" has been removed from the list.')
        else:
            print("Invalid selection...")
    else:
        print("Please enter a valid number...")


# Function to display the order menu when user picks 2 on the main menu
def order_menu():
    while True:
        print("\nOrder Menu")
        print("1 - View Orders")
        print("2 - Add Order")
        print("3 - Update Order Status")
        print("4 - Update Order Details")
        print("5 - Delete Order")
        print("0 - Return to Main Menu")

        # This lets the user pick what they want to do with orders
        order_choice = input("\nEnter your choice: ")

        if order_choice == "0":
            break
        elif order_choice == "1":
            view_orders()
        elif order_choice == "2":
            add_order()
        elif order_choice == "3":
            update_order_status()
        elif order_choice == "4":
            update_order_details()
        elif order_choice == "5":
            delete_order()
        else:
            print("Invalid choice, please try again...")

# Function to view all orders
def view_orders():
    print("\nOrder List:")
    if len(orders) > 0:
        for i in range(len(orders)):  # Loop through orders and show them with a number
            print(i, "-", orders[i])
    else:
        print("No orders yet...")

# Function to add a new order
def add_order():
    # Ask the user for customer details
    customer_name = input("\nEnter customer name: ")
    customer_address = input("Enter customer address: ")
    customer_phone = input("Enter customer phone number: ")

    # Creates a new order as a dictionary
    new_order = {
        "customer_name": customer_name,
        "customer_address": customer_address,
        "customer_phone": customer_phone,
        "status": "Preparing"
    }

    orders.append(new_order)  # Adds the new order to the orders list
    print("Order added :D")

# Function to update order status
def update_order_status():
    view_orders()
    index = input("\nEnter order number to update status: ")

    if index.isdigit():
        index = int(index)
        if 0 <= index < len(orders):
            print("\nOrder Status Options:")
            print("0 - Preparing")
            print("1 - Shipped :D")
            print("2 - Delivered :D")

            status_choice = input("\nEnter status number: ")
            if status_choice == "0":
                orders[index]["status"] = "Preparing"
            elif status_choice == "1":
                orders[index]["status"] = "Shipped :D"
            elif status_choice == "2":
                orders[index]["status"] = "Delivered :D"
            else:
                print("Invalid selection...")
            print("Order status updated")
        else:
            print("Invalid order number...")
    else:
        print("Please enter a valid number...")

# Function to update order details (name address or phone)
def update_order_details():
    view_orders()
    index = input("\nEnter order number to update: ")

    if index.isdigit():
        index = int(index)
        if 0 <= index < len(orders):
            print("Press Enter to keep the current value.")

            # Ask for updates if they leave blank the old value stays
            new_name = input("Enter new customer name: ")
            if new_name != "":
                orders[index]["customer_name"] = new_name

            new_address = input("Enter new address: ")
            if new_address != "":
                orders[index]["customer_address"] = new_address

            new_phone = input("Enter new phone number: ")
            if new_phone != "":
                orders[index]["customer_phone"] = new_phone

            print("Order updated.")
        else:
            print("Invalid order number...")
    else:
        print("Please enter a valid number...")

# Function to delete an order
def delete_order():
    view_orders()
    index = input("\nEnter order number to delete: ")

    if index.isdigit():
        index = int(index)
        if 0 <= index < len(orders):  # Checks if the index exists
            orders.pop(index)  # Removes the order from the list
            print("Order deleted.")
        else:
            print("Invalid selection...")
    else:
        print("Please enter a valid number...")

# Run the program
main_menu()

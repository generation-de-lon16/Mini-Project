# Creating a product list with 4 items
products = ["Mocha", "Americano", "Espresso", "Latte"]

# Display Main Menu
print("\nMain Menu")
print("1 - View Products")
print("2 - Add New Product")
print("3 - Update Existing Product")
print("4 - Delete Product")
print("0 - Exit")

choice = input("\nEnter your choice: ") #Asks user for input

if choice == "0":  # When they pick 0 the CLI prints this
    print("Exiting program...")

elif choice == "1":  # When user picks a product list is revealed using the number system (goes from 0-3)
    print("\nProduct List:")
    print("0:", products[0])
    print("1:", products[1])
    print("2:", products[2])
    print("3:", products[3])

elif choice == "2":  # When option 2 is picked the user is asked to input the new product
    new_product = input("\nEnter product name: ")

    if products[0] == "":
        products[0] = new_product
    elif products[1] == "":
        products[1] = new_product
    elif products[2] == "":
        products[2] = new_product
    elif products[3] == "":
        products[3] = new_product
    else:
        print("Product list is full, cannot ad more items")

    print(f'"{new_product}" has been added')

elif choice == "3":  # Changing existing product
    print("\nAvailable Products:")
    print("0:", products[0])
    print("1:", products[1])
    print("2:", products[2])
    print("3:", products[3])

    index = input("\nEnter the product number to update: ")

    if index == "0":
        new_name = input("Enter new product name: ")
        products[0] = new_name
    elif index == "1":
        new_name = input("Enter new product name: ")
        products[1] = new_name
    elif index == "2":
        new_name = input("Enter new product name: ")
        products[2] = new_name
    elif index == "3":
        new_name = input("Enter new product name: ")
        products[3] = new_name
    else:
        print("Invalid selection")

    print("Product updated successfully")

elif choice == "4":  # Deleting new products by simply changing their name
    print("\nAvailable Products:")
    print("0:", products[0])
    print("1:", products[1])
    print("2:", products[2])
    print("3:", products[3])

    remove_product = input("\nEnter the product number to delete: ")

    if remove_product == "0":
        products[0] = "Deleted"
    elif remove_product == "1":
        products[1] = "Deleted"
    elif remove_product == "2":
        products[2] = "Deleted"
    elif remove_product == "3":
        products[3] = "Deleted"
    else:
        print("Invalid selection")

    print("Product deleted")

else:
    print("Invalid choice, please try again")

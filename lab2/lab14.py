products = {}

while True:
    print("\nChoose an option:")
    print("a. Add a new product")
    print("b. Update price of an existing product")
    print("c. Find products within a price range")
    print("d. Exit")
    choice = input("Enter your choice (a/b/c/d): ").lower()

    if choice == 'a':
        name = input("Enter the product name: ")
        if name in products:
            print("Product already exists.")
        else:
            try:
                price = float(input("Enter the price: "))
                products[name] = price
                print(f"Added {name} with price {price}")
            except ValueError:
                print("Invalid price entered.")

    elif choice == 'b':
        name = input("Enter the product name to update: ")
        if name in products:
            try:
                price = float(input("Enter the new price: "))
                products[name] = price
                print(f"Updated {name} to new price {price}")
            except ValueError:
                print("Invalid price entered.")
        else:
            print("Product not found.")

    elif choice == 'c':
        try:
            min_price = float(input("Enter minimum price: "))
            max_price = float(input("Enter maximum price: "))
            found = False
            for product, price in products.items():
                if min_price <= price <= max_price:
                    print(f"{product}: {price}")
                    found = True
            if not found:
                print("No products found in this price range.")
        except ValueError:
            print("Invalid price entered.")

    elif choice == 'd':
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")
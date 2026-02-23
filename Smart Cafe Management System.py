MENU = {
    "Coffee": 450,
    "Tea": 300,
    "Sandwich": 850,
    "Pastry": 400,
    "Juice": 500
}


def display_menu():
    print("\n--- Cafe Central Perk Menu ---")
    for item, price in MENU.items():
        print(f"{item} - LKR {price}")


def take_order():
    orders = []
    while True:
        item = input("Enter item name (or 'done' to finish): ").title()
        if item == "Done":
            break
        if item not in MENU:
            print("Invalid item. Please try again.")
            continue
        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                raise ValueError
        except ValueError:
            print("Invalid quantity. Enter a number greater than zero.")
            continue
        subtotal = MENU[item] * quantity
        orders.append((item, quantity, subtotal))
    return orders


def apply_discount(total):
    if total > 2000:
        return total * 0.10
    return 0


def calculate_bill(orders):
    total = sum(order[2] for order in orders)
    discount = apply_discount(total)
    final_total = total - discount
    return total, discount, final_total


def print_receipt(orders, total, discount, final_total):
    print("\n--- Receipt ---")
    for item, qty, subtotal in orders:
        print(f"{item} x{qty} = LKR {subtotal}")
    print(f"Subtotal: LKR {total}")
    print(f"Discount: LKR {discount}")
    print(f"Final Total: LKR {final_total}")


def search_item():
    item = input("Enter item name to search: ").title()
    if item in MENU:
        print(f"{item} is available at LKR {MENU[item]}")
    else:
        print("Item not found")


def sort_menu():
    choice = input("Sort by 'name' or 'price': ").lower()
    if choice == "name":
        for item in sorted(MENU):
            print(item, MENU[item])
    elif choice == "price":
        for item, price in sorted(MENU.items(), key=lambda x: x[1]):
            print(item, price)
    else:
        print("Invalid sort option")


def main():
    while True:
        print("\n1. Display Menu  2. Take Order  3. Search Item  4. Sort Menu  5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            display_menu()
        elif choice == "2":
            orders = take_order()
            total, discount, final_total = calculate_bill(orders)
            print_receipt(orders, total, discount, final_total)
        elif choice == "3":
            search_item()
        elif choice == "4":
            sort_menu()
        elif choice == "5":
            print("Thank you for using Cafe Central Perk System")
            break
        else:
            print("Invalid option. Please try again.")


main()


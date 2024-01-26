from global_vars import *
from sys import exit


def display_food_menu():
    print('\n***** MENU *****\n')
    for sku, item in food_menu.items():
        # TODO The index displayed should not be a slice of the SKU. We would need some kind of mapping,
        # or maybe food_menu should be just a list rather than a dictionary.
        print(f"({sku[3:]}) {item['name']}: ${item['price']}")


#TODO We can think some of the following functions as methods of a cart object (a singleton)
def add_to_cart(sku: str, qty: int = 1):
    if sku not in food_menu:
        raise ValueError("Invalid SKU. Please check that the entered menu item is correct")
    if sku in cart:
        cart[sku] += qty
    else:
        cart[sku] = qty
    print(f"Added {qty} of {food_menu[sku]['name']} to the cart.")


def remove_from_cart(sku: str):
    if sku not in cart:
        raise UserWarning("The item is not in the cart!")
    qty = cart.pop(sku)
    print(f"Removed all {qty} of {food_menu[sku]['name']} from the cart.")


def modify_qty_cart(sku: str, new_qty: int):
    if sku not in cart:
        raise UserWarning("The item is not in the cart!")
    if new_qty < 0:
        raise ValueError("Invalid quantity value {new_qty}")
    elif new_qty > 0:
        old_qty = cart[sku]
        cart[sku] = new_qty
    else:
        old_qty = cart.pop(sku)
    print(f"Changed quantity of {food_menu[sku]['name']} in the cart from {old_qty} to {new_qty}.")


def view_cart():
    print('\n***** YOUR CART *****\n')
    # TODO alignment to be improved
    print("SKU\t\tName\t\t\tPrice\tQuantity\tTotal per item")
    subtotal = 0
    for sku, qty in cart.items():
        price_per_item = food_menu[sku]['price']
        total_price_per_item = price_per_item * qty
        subtotal += (price_per_item * qty)
        print(f"({sku[3:]})\t\t{food_menu[sku]['name']}\t\t${price_per_item}\tx\t{qty} = {total_price_per_item}")
    # TODO for taxes and total, only 2 decimal digits are needed
    taxes = subtotal * sales_tax
    total = subtotal + taxes
    print(f"Subtotal\t\t\t\t\t\t\t\t\t{subtotal}")
    print(f"Taxes\t\t\t\t\t\t\t\t\t{taxes}")
    print(f"Total\t\t\t\t\t\t\t\t\t{total}")


def checkout():
    view_cart()
    print("Are you sure you want to confirm your purchase? (Y/N)")
    action = input()
    if action.upper() == 'Y':
        # TODO Add logic to collect shipping and payment information and process them
        print("Order confirmed!\nYou can now start a new order.")
        cart.clear()
    else:
        print("The order has not been confirmed yet.")


def get_sku():
    print("Enter the index of the food item: ")
    item_idx = input()
    # TODO add some checks on item_idx
    sku = "sku" + item_idx
    if sku not in food_menu:
        raise ValueError("Item not found. Check the value of the index.")
    return sku


def get_qty():
    print("Enter the quantity: ")
    qty = int(input())
    if qty < 1:
        raise ValueError("Incorrect quantity. Value needs to be at least 1.")
    return qty


def display_actions():
    while True:
        print("What would you like to do? (type the number of the action)")
        for idx, action in actions.items():
            print(f'({idx}) {action}')
        #TODO what if choice is not an integer?
        choice = int(input())
        if choice not in actions:
            print("Value for the action is not correct.")
            continue
        if choice == 1:
            display_food_menu()
            sku = get_sku()
            qty = get_qty()
            add_to_cart(sku, qty)
        elif choice == 2:
            view_cart()
            sku = get_sku()
            remove_from_cart(sku)
        elif choice == 3:
            view_cart()
            sku = get_sku()
            qty = get_qty()
            modify_qty_cart(sku, qty)
        elif choice == 4:
            view_cart()
        elif choice == 5:
            checkout()
        elif choice == 6:
            exit()
        else:
            print("Incorrect option selected")


def main():
    display_actions()


if __name__ == '__main__':
    main()

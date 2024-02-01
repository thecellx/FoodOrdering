from cart import Cart
from global_vars import *
from menu import Menu
from sys import exit



class FoodOrdering:
    def __init__(self):
        self.food_menu = Menu()
        self.cart = Cart()

    def display_food_menu(self):
        print('\n***** MENU *****\n')
        for sku, name, price in self.food_menu:
            # TODO The index displayed should not be a slice of the SKU. We would need some kind of mapping,
            # or maybe food_menu should be just a list rather than a dictionary.
            print(f"({sku[3:]}) {name}: ${price}")

    def add_to_cart(self):
        self.display_food_menu()
        sku = self.get_sku()
        qty = FoodOrdering.get_qty()
        if not self.food_menu.does_item_exist(sku):
            raise ValueError("Invalid SKU {sku}.")
        self.cart.add(sku, qty)
        print(f"Added {qty} of {self.food_menu.get_name_by_sku(sku)} to the cart.")

    def remove_from_cart(self):
        self.view_cart()
        sku = self.get_sku()
        qty = self.cart.remove(sku)
        print(f"Removed all {qty} of {self.food_menu.get_name_by_sku(sku)} from the cart.")

    def modify_qty_cart(self):
        self.view_cart()
        sku = self.get_sku()
        new_qty = FoodOrdering.get_qty()
        old_qty = self.cart.change_qty(sku, new_qty)
        print(f"Changed quantity of {self.food_menu.get_name_by_sku(sku)} in the cart from {old_qty} to {new_qty}.")

    def view_cart(self):
        print('\n***** YOUR CART *****\n')
        # TODO alignment to be improved
        print("SKU\t\tName\t\t\tPrice\tQuantity\tTotal per item")
        subtotal = 0
        for sku, qty in self.cart:
            item_name = self.food_menu.get_name_by_sku(sku)
            price_per_item = self.food_menu.get_price_by_sku(sku)
            total_price_per_item = price_per_item * qty
            subtotal += (price_per_item * qty)
            print(f"({sku[3:]})\t\t{item_name}\t\t${price_per_item}\tx\t{qty} = {total_price_per_item}")
        # TODO for taxes and total, only 2 decimal digits are needed
        taxes = subtotal * sales_tax
        total = subtotal + taxes
        print(f"Subtotal\t\t\t\t\t\t\t\t\t{subtotal}")
        print(f"Taxes\t\t\t\t\t\t\t\t\t{taxes}")
        print(f"Total\t\t\t\t\t\t\t\t\t{total}")

    def checkout(self):
        self.view_cart()
        print("Are you sure you want to confirm your purchase? (Y/N)")
        action = input()
        if action.upper() == 'Y':
            # TODO Add logic to collect shipping and payment information and process them
            print("Order confirmed!\nYou can now start a new order.")
            self.cart.clear()
        else:
            print("The order has not been confirmed yet.")

    def get_sku(self):
        print("Enter the index of the food item: ")
        item_idx = input()
        # TODO add some checks on item_idx
        sku = "sku" + item_idx
        # TODO Evaluate if this check can be moved out of get_sku so that we can make this method static
        if not self.food_menu.does_item_exist(sku):
            raise ValueError("Item {sku} not found. Check the value of the index.")
        return sku

    @staticmethod
    def get_qty():
        print("Enter the quantity: ")
        qty = int(input())
        if qty < 1:
            raise ValueError("Incorrect quantity. Value needs to be at least 1.")
        return qty

    @staticmethod
    def action_request():
        print("What would you like to do? (type the number of the action)")
        for idx, action in actions.items():
            print(f'({idx}) {action}')
        action = int(input())
        return action

    def run(self):
        while True:
            # TODO what if choice is not an integer?
            user_action = FoodOrdering.action_request()
            if user_action not in actions:
                print("Value for the action is not correct.")
                continue
            if user_action == 1:
                self.add_to_cart()
            elif user_action == 2:
                self.remove_from_cart()
            elif user_action == 3:
                self.modify_qty_cart()
            elif user_action == 4:
                self.view_cart()
            elif user_action == 5:
                self.checkout()
            elif user_action == 6:
                exit()
            else:
                print("Incorrect option selected")


if __name__ == '__main__':
    app = FoodOrdering()
    app.run()

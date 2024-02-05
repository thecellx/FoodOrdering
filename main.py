from cart import Cart
from global_vars import *
from menu import Menu
from sys import exit
from data_ui import TextDataUI


class FoodOrdering:
    def __init__(self):
        self.food_menu = Menu()
        self.cart = Cart()
        self.data_ui = TextDataUI()

    def add_to_cart(self):
        self.data_ui.display_food_menu(self.food_menu)
        sku = self.data_ui.get_sku()
        if not self.food_menu.does_item_exist(sku):
            raise ValueError("Invalid SKU {sku}.")
        qty = self.data_ui.get_qty()
        self.cart.add(sku, qty)
        self.data_ui.display_msg(f"Added {qty} of {self.food_menu.get_name_by_sku(sku)} to the cart.")

    def remove_from_cart(self):
        self.data_ui.display_cart(self. cart, self.food_menu)
        sku = self.data_ui.get_sku()
        if not self.food_menu.does_item_exist(sku):
            raise ValueError("Invalid SKU {sku}.")
        qty = self.cart.remove(sku)
        self.data_ui.display_msg(f"Removed all {qty} of {self.food_menu.get_name_by_sku(sku)} from the cart.")

    def modify_qty_cart(self):
        self.data_ui.display_cart(self. cart, self.food_menu)
        sku = self.data_ui.get_sku()
        if not self.food_menu.does_item_exist(sku):
            raise ValueError("Invalid SKU {sku}.")
        new_qty = self.data_ui.get_qty()
        old_qty = self.cart.change_qty(sku, new_qty)
        self.data_ui.display_msg(f"Changed quantity of {self.food_menu.get_name_by_sku(sku)} in the cart from {old_qty} to {new_qty}.")

    #TODO evaluate if this method is really necessary
    def view_cart(self):
        self.data_ui.display_cart(self. cart, self.food_menu)

    def checkout(self):
        self.data_ui.display_cart(self.cart, self.food_menu)
        action = self.data_ui.request_confirmation("Are you sure you want to confirm your purchase?")
        if action.upper() == 'Y':
            # TODO Add logic to collect shipping and payment information and process them
            self.data_ui.display_msg("Order confirmed!\nYou can now start a new order.")
            self.cart.clear()
        else:
            self.data_ui.display_msg("The order has not been confirmed yet.")

    def run(self):
        while True:
            # TODO what if user_action is not an integer?
            user_action = self.data_ui.request_action()
            if user_action not in actions:
                self.data_ui.display_error("Value for the action is not correct.")
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
                self.data_ui.display_error("Incorrect option selected")


if __name__ == '__main__':
    app = FoodOrdering()
    app.run()

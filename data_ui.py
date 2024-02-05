from abc import ABC, abstractmethod
from cart import Cart
from global_vars import *
from menu import Menu


class DataUI(ABC):
    @abstractmethod
    def display_food_menu(self, food_menu: Menu):
        pass

    @abstractmethod
    def display_cart(self, cart: Cart, food_menu: Menu):
        pass

    @abstractmethod
    def request_action(self):
        pass

    @abstractmethod
    def request_confirmation(self, msg: str):
        pass

    @abstractmethod
    def display_error(self, error_msg: str):
        pass

    @abstractmethod
    def get_sku(self):
        pass

    @abstractmethod
    def get_qty(self, allow_zero: bool = False):
        pass

    @abstractmethod
    def display_msg(self, msg: str):
        pass


class TextDataUI(DataUI):
    def display_food_menu(self, food_menu: Menu):
        print('\n***** MENU *****\n')
        for sku, name, price in food_menu:
            # TODO The index displayed should not be a slice of the SKU. We would need some kind of mapping,
            # or maybe food_menu should be just a list rather than a dictionary.
            print(f"({sku[3:]}) {name}: ${price}")

    def display_cart(self, cart: Cart, food_menu: Menu):
        print('\n***** YOUR CART *****\n')
        # TODO alignment to be improved
        print("SKU\t\tName\t\t\tPrice\tQuantity\tTotal per item")
        subtotal = 0
        for sku, qty in cart:
            item_name = food_menu.get_name_by_sku(sku)
            price_per_item = food_menu.get_price_by_sku(sku)
            total_price_per_item = price_per_item * qty
            subtotal += (price_per_item * qty)
            print(f"({sku[3:]})\t\t{item_name}\t\t${price_per_item}\tx\t{qty} = {total_price_per_item}")
        taxes = round(subtotal * sales_tax, 2)
        total = round(subtotal + taxes, 2)
        print(f"Subtotal\t\t\t\t\t\t\t\t\t{subtotal}")
        print(f"Taxes\t\t\t\t\t\t\t\t\t{taxes}")
        print(f"Total\t\t\t\t\t\t\t\t\t{total}")

    def request_action(self):
        print("What would you like to do? (type the number of the action)")
        for idx, action in actions.items():
            print(f'({idx}) {action}')
        action = int(input())
        return action

    def request_confirmation(self, msg: str = "Please confirm"):
        while True:
            print(msg + " (Y/N)")
            action = input()
            action = action.upper()
            if action in ('Y', 'N'):
                return action

    def display_msg(self, msg: str):
        print(msg)

    def display_error(self, error_msg: str):
        print("ERROR: " + error_msg)

    def get_sku(self):
        print("Enter the index of the food item: ")
        item_idx = input()
        # TODO add some checks on item_idx
        sku = "sku" + item_idx
        return sku

    def get_qty(self, allow_zero: bool = False):
        print("Enter the quantity: ")
        qty = input()
        min_qty = 0 if allow_zero else 1
        while not qty.isnumeric() or int(qty) < min_qty:
            self.display_error(f"Incorrect quantity. Value needs to be a number greater than {min_qty}.")
            qty = input()
        return int(qty)

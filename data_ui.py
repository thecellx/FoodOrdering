from abc import ABC, abstractmethod
from cart import Cart
from global_vars import *
from menu import Menu


class DataUI(ABC):
    def __init__(self, food_menu: Menu):
        self._food_menu = food_menu

    @abstractmethod
    def display_food_menu(self):
        pass

    @abstractmethod
    def display_cart(self, cart: Cart):
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

    def __init__(self, food_menu: Menu):
        super().__init__(food_menu)
        # Dictionary to map SKUs to their indices. We assume the menu will never change during the execution
        # so we only initialize this map in the constructor
        self._sku_index_map = self._build_sku_index_map()

    def display_food_menu(self):
        print('\n***** MENU *****\n')
        for idx, (sku, name, price) in enumerate(self._food_menu, start=1):
            print(f"({idx}) {name}: ${price}")

    def display_cart(self, cart: Cart):
        print('\n***** YOUR CART *****\n')
        # TODO alignment to be improved
        print("ITEM #\t\tName\t\t\tPrice\tQuantity\tTotal per item")
        subtotal = 0
        for sku, qty in cart:
            item_name = self._food_menu.get_name_by_sku(sku)
            price_per_item = self._food_menu.get_price_by_sku(sku)
            total_price_per_item = price_per_item * qty
            subtotal += (price_per_item * qty)
            print(f"({self._sku_index_map[sku]})\t\t{item_name}\t\t${price_per_item}\tx\t{qty} = {total_price_per_item}")
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

    def get_sku(self) -> str:
        num_of_items = len(self._sku_index_map)
        assert num_of_items > 0, "Menu appears to be empty"
        while True:
            print(f"Enter the index of the food item: (1 to {num_of_items})")
            item_idx = input()
            if item_idx.isnumeric() and int(item_idx) in range(1, len(self._sku_index_map)+1):
                break
            self.display_error(f"Index needs to be between 1 and {num_of_items}.")
        sku = self._index2sku(int(item_idx))
        return sku

    def get_qty(self, allow_zero: bool = False):
        min_qty = 0 if allow_zero else 1
        while True:
            print("Enter the quantity: ")
            qty = input()
            if qty.isnumeric() and int(qty) >= min_qty:
                break
            self.display_error(f"Incorrect quantity. Value needs to be a number greater than {min_qty}.")
        return int(qty)

    def _build_sku_index_map(self) -> dict[str, int]:
        sku_index_map = dict()
        for idx, (sku, _, _) in enumerate(self._food_menu, start=1):
            sku_index_map[sku] = idx
        return sku_index_map

    def _index2sku(self, index: int) -> str:
        # Since dictionaries keep the order elements are added, we can assume
        # that _sku_index_map.keys() is a list of skus ordered by index
        index_sku_map = list(self._sku_index_map.keys())
        sku = index_sku_map[index-1]
        return sku

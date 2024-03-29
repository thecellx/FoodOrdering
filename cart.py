from collections.abc import Iterable


class Cart(Iterable):
    def __init__(self):
        self.cart = {}

    # It allows to iterate on sku's and quantities
    def __iter__(self):
        return iter(self.cart.items())

    def __len__(self) -> int:
        return sum(self.cart.values())

    def is_empty(self) -> bool:
        return len(self.cart) == 0

    def add(self, sku: str, qty: int = 1):
        if qty < 1:
            raise ValueError("Invalid quantity value {new_qty} for {sku}.")
        if sku in self.cart:
            self.cart[sku] += qty
        else:
            self.cart[sku] = qty

    def remove(self, sku: str) -> int:
        if sku not in self.cart:
            raise UserWarning("The item {sku} is not in the cart!")
        qty = self.cart.pop(sku)
        return qty

    def change_qty(self, sku: str, new_qty: int) -> int:
        if sku not in self.cart:
            raise UserWarning("The item {sku} is not in the cart!")
        if new_qty < 0:
            raise ValueError("Invalid quantity value {new_qty} for {sku}.")
        elif new_qty > 0:
            old_qty = self.cart[sku]
            self.cart[sku] = new_qty
        else:
            old_qty = self.cart.pop(sku)
        return old_qty

    def clear(self):
        self.cart.clear()

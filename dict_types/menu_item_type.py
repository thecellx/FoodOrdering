from typing import TypedDict


class MenuItemDataType(TypedDict):
    name: str
    price: float


class MenuItemType(MenuItemDataType):
    sku: str

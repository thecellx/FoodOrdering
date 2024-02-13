import json

from config import Config
from json_schemas.menu_item_schema import MenuItemSchema
from marshmallow.exceptions import ValidationError
from dict_types.menu_item_type import MenuItemDataType, MenuItemType


class Menu:
    def __init__(self, config: Config):
        self.food_menu = Menu._read_menu_from_file(config.get('menu_rel_path'))

    def __iter__(self):
        for sku, item in self.food_menu.items():
            yield sku, item['name'], item['price']

    def does_item_exist(self, sku: str):
        return sku in self.food_menu

    def get_name_by_sku(self, sku: str):
        if sku not in self.food_menu:
            raise ValueError(f"Invalid sku {sku}.")
        return self.food_menu[sku]['name']

    def get_price_by_sku(self, sku: str):
        if sku not in self.food_menu:
            raise ValueError(f"Invalid sku {sku}.")
        return self.food_menu[sku]['price']

    @staticmethod
    def _read_menu_from_file(filename: str):
        with open(filename) as file:
            menu_recs = json.load(file)

            # validate the json data
            menu_items_schema = MenuItemSchema(many=True)
            errors = menu_items_schema.validate(menu_recs)
            if errors:
                raise ValidationError(errors)

            menu_dict = Menu._menu_list_2_dict(menu_recs)
            return menu_dict

    @staticmethod
    def _menu_list_2_dict(menu: list[MenuItemType]) -> dict[str, MenuItemDataType]:
        menu_dict = {}
        for item in menu:
            sku, name, price = item.values()
            menu_dict[sku] = {'name': name, 'price': price}
        return menu_dict

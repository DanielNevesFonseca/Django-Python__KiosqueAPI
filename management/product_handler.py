from menu import products
from collections import Counter


def get_product_by_id(product_id: int):

    if not isinstance(product_id, int):
        raise TypeError("product id must be an int")

    for dict in products:
        if dict.get("_id") == product_id:
            return dict

    return {}


def get_products_by_type(product_type: str):

    if not isinstance(product_type, str):
        raise TypeError("product type must be a str")

    same_type_list = []

    for product_dict in products:
        for key, value in product_dict.items():
            if key == "type" and value == product_type:
                same_type_list.append(product_dict)

    return same_type_list


def add_product(menu_list: list, **product: dict):
    greater_id = 0
    dict_product = product

    for dict in menu_list:
        current_id = dict["_id"]
        if current_id > greater_id:
            greater_id = current_id

    greater_id += 1
    dict_product.update({"_id": greater_id})
    menu_list.append(dict_product)
    return dict_product


def menu_report():

    total_product_quantity = len(products)
    total_product_price = 0
    types_list = []

    for product_dict in products:
        total_product_price += product_dict["price"]

    average_price = total_product_price / total_product_quantity

    for product in products:
        for key, value in product.items():
            if key == "type":
                types_list.append(value)

    type_count = Counter(types_list)
    most_common_type = type_count.most_common(1)[0][0]
    log_str = f"Products Count: {total_product_quantity} - Average Price: ${average_price:.1f} - Most Common Type: {most_common_type}"
    return log_str


def add_product_extra(menu_list: list, *required_keys: dict, **product: dict):
    greater_id = 0
    dict_product = product
    required_keys_list = list(required_keys)
    dict_validated = {}

    for key, value in dict_product.items():
        if key in required_keys_list:
            dict_validated[key] = value
            required_keys_list.remove(key)

    if len(required_keys_list) != 0:
        for key in required_keys_list:
            raise KeyError(f"field {key} is required")

    for dict in menu_list:
        current_id = dict["_id"]
        if current_id > greater_id:
            greater_id = current_id

    greater_id += 1
    dict_validated.update({"_id": greater_id})
    menu_list.append(dict_validated)
    return dict_validated

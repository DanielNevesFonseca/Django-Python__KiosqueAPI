from menu import products


def get_product_by_id(product_id: int):

    for dict in products:
        if dict.get("_id") == product_id:
            return dict

    return {}


def get_products_by_type(product_type: str):

    same_type_list = []

    for dict in products:
        if dict.get("type") == product_type:
            same_type_list.append(dict)

    return same_type_list


def add_product(menu_list: list, *products: dict):
    greater_id = 0
    new_products_list = []

    for dict in menu_list:
        current_id = dict["_id"]
        if current_id > greater_id:
            greater_id = current_id

    for dict_product in products:
        greater_id += 1
        dict_product.update({"_id": greater_id})

        if len(products) > 1:
            new_products_list.append(dict_product)
        else:
            return dict_product

    return new_products_list

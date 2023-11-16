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
        else:
            return []

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
    products.append(dict_product)
    return dict_product


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

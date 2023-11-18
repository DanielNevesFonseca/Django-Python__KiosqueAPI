from menu import products


def calculate_tab(table: list):
    subtotal = 0

    for dict in products:
        for dict_table in table:
            if dict["_id"] == dict_table["_id"]:
                subtotal += (dict["price"] * dict_table["amount"])
    subtotal_dict = {"subtotal": f'${round(subtotal, 2)}'}
    return subtotal_dict

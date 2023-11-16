from menu import products

# {"_id": 10, "amount": 3},


def calculate_tab(table: list):
    subtotal = 0

    for dict in products:
        for dict_table in table:
            if dict["_id"] == dict_table["_id"]:
                subtotal += (dict["price"] * dict_table["amount"])
    
    subtotal_dict = {"subtotal": f'${subtotal:.2f}'}
    return subtotal_dict

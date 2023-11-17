from management import product_handler, tab_handler
from menu import products

if __name__ == "__main__":
    # Seus prints de teste aqui
    # print(product_handler.get_product_by_id("30"))
    # print()
    # print(product_handler.get_products_by_type(12342))
    # print()
    # new_product = {
    #     "title": "X-Python",
    #     "price": 5.0,
    #     "rating": 5,
    #     "description": "Sanduiche de Python",
    #     "type": "fast-food"
    # }
    # new_product1 = {
    #     "title": "X-Java",
    #     "price": 5.0,
    #     "rating": 5,
    #     "description": "Sanduiche de Java",
    #     "type": "fast-food"
    # }
    # print(product_handler.add_product(products, **new_product))
    # table_2 = [
    #     {"_id": 10, "amount": 3},
    #     {"_id": 20, "amount": 2},
    #     {"_id": 21, "amount": 5},
    # ]
    # table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    # print(tab_handler.calculate_tab(table_1))
    # print(product_handler.menu_report())
    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food",
        "extra_key_1": "extra_value_1",
        "extra_key_2": "extra_value_2"
    }

    required_keys = ("description", "price", "rating", "title", "type")

    product_handler.add_product_extra(products, *required_keys, **new_product)

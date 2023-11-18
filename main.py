from management import product_handler
if __name__ == "__main__":
    # Seus prints de teste aqui
    # print(product_handler.get_products_by_type("fruit"))
    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food"
    }
    print(product_handler.add_product([], **new_product))

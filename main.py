from management import product_handler
from menu import products

if __name__ == "__main__":
    # Seus prints de teste aqui
    # print(get_product_by_id(30))
    # print()
    # print(get_products_by_type("drink"))
    # print()
    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food"
    }
    new_product1 = {
        "title": "X-Java",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Java",
        "type": "fast-food"
    }
    print(product_handler.add_product(
        products, new_product, new_product1, new_product1
        ))

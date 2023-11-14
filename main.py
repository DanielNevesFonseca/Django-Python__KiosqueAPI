from management.product_handler import get_product_by_id, get_products_by_type

if __name__ == "__main__":
    # Seus prints de teste aqui
    print(get_product_by_id(30))
    print()
    print(get_products_by_type("drink"))

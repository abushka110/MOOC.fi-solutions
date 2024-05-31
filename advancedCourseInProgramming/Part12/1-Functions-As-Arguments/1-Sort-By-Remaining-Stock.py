# solution
def sort_by_remaining_stock(items: list):
    items_dict = {item[2] : item for item in items}
    peaces_remain = [peaces for peaces in items_dict.keys()]
    peaces_remain = sorted(peaces_remain)
    return [items_dict[peaces_count] for peaces_count in peaces_remain]

# test
if __name__ == "__main__":
    products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22)]
    for product in sort_by_remaining_stock(products):
        print(f"{product[0]} {product[2]} pcs")
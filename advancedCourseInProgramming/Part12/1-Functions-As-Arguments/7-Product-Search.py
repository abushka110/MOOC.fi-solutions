# solution
def search(products: list, criterion: callable):
    # create new list
    new_list = []

    # check if product fulfil the criterion
    for product in products:
        if criterion(product):
            new_list.append(product)
    
    return new_list

# test
if __name__ == "__main__":
    products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22), ("kale", 0.99, 1)]

    def price_under_4_euros(product):
        return product[1] < 4
    
    for product in search(products, price_under_4_euros):
        print(product)
    
    # expected output:
    # ('apple', 3.95, 3)
    # ('kale', 0.99, 1)

    for product in search(products, lambda t: t[2]>10):
        print(product)

    # expected output:
    # ('banana', 5.95, 12)
    # ('watermelon', 4.95, 22)
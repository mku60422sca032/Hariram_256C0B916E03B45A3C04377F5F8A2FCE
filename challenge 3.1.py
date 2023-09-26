def linear_search_product(product_list, target_product):
    indices = []
    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)
    return indices

# Example usage:
products = ["mango", "boot", "Orange", "Banana", "mango"]
target = "mango"
target2="apple"
result = linear_search_product(products, target)
print(result)

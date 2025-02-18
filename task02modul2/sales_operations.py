# sales_operations.py

def total_sold(sales_dict):
    return sum(sales_dict.values())

def most_sold_product(sales_dict):
    return max(sales_dict, key=lambda product: sales_dict[product])

def least_sold_product(sales_dict):
    return min(sales_dict, key=lambda product: sales_dict[product])

def get_product_sales(sales_dict, product):
    try:
        return sales_dict[product]
    except KeyError:
        return f"Produsul '{product}' nu există în datele de vânzări."

def validate_sales_data(sales_dict):
    return all(0 <= quantity <= 100000 for quantity in sales_dict.values())

def get_critical_products(sales_dict, threshold=50):
    return [product for product, quantity in sales_dict.items() if quantity < threshold]

# Modul sales_operations.py

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
    return list(filter(lambda product: sales_dict[product] < threshold, sales_dict))

# Scriptul principal main.py
import sales_operations as so

sales = {
    "Laptop": 15,
    "Mouse": 150,
    "Keyboards": 85,
    "Monitor": 30,
    "USB cables": 200
}

if "Web camera" not in sales:
    sales["Web camera"] = 0

sales["Monitor"] += 5

print("Dicționarul sales actualizat:", sales)
print("Total produse vândute:", so.total_sold(sales))
print("Produsul cel mai vândut:", so.most_sold_product(sales))
print("Produsul cel mai puțin vândut:", so.least_sold_product(sales))
print("Lista produselor critice:", so.get_critical_products(sales))
print("Date valide?:", so.validate_sales_data(sales))

import task02modul2.sales_operations as so

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

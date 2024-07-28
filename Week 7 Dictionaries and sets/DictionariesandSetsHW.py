sales_data = []
sales_dict = {}

with open ('sales.txt', mode='r') as file:
    for line in file:
        sales_data = line.strip().split(",")
        product = sales_data[0]
        amount = int(sales_data[1])
        price = float(sales_data[2])
        total = amount*price
        #print ("Printing current line of list", sales_data)
        #print ("Printing product, ammount, and price for current line", product, amount, price)

        if product not in sales_dict:
            sales_dict[product] = 0.0
        sales_dict[product] = sales_dict[product] + total
    print(sales_dict)

print()

print (f"{'Product':<10} {'Total Sales':>12}")
print("-" * 22)
for product, total in sales_dict.items():
    print(f"{product:<10}${total:>10.2f}")

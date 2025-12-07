price = float(input("Enter the price of the item: "))

if price <= 1000:
    price -= (price * 0.10)
    print(f"Discounted price is: {price}")
elif price > 1000 and price <= 5000:
    price -= (price * 0.15)
    print(f"Discounted price is: {price}")
elif price > 5000 and price <= 10000:
    price -= (price * 0.20)
    print(f"Discounted price is: {price}")
else:
    price -= (price * 0.25)
    print(f"Discounted price is: {price}")
def calculate_bill(price,quantity):
    return price*quantity
price1=int(input("Enter the price of product 1: "))
quantity1=int(input("Enter the quantity of product 1: "))
price2=int(input("Enter the price of product 2: "))
quantity2=int(input("Enter the quantity of product 2: "))
price3=int(input("Enter the price of product 3: "))
quantity3=int(input("Enter the quantity of product 3: "))
total_cost1=calculate_bill(price1,quantity1)
total_cost2=calculate_bill(price2,quantity2)
total_cost3=calculate_bill(price3,quantity3)
print(total_cost1)
print(total_cost2)
print(total_cost3)


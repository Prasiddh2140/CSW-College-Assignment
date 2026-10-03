def generate_bill(item, price, quantity=1, discount=0, tax_rate=0.05):
    # Step 1: Compute the subtotal
    subtotal = price * quantity
    # Step 2: Apply the discount percentage on the subtotal
    discount_amount = subtotal * (discount / 100)
    discounted_amount = subtotal - discount_amount
    # Step 3: Apply tax on the discounted amount
    tax_amount = discounted_amount * tax_rate
    # Step 4: Calculate final payable amount
    total_amount = discounted_amount + tax_amount
    # Print a detailed bill summary
    print(f"--- Bill Summary for {item} ---")
    print(f"Price per unit:  ${price:.2f}")
    print(f"Quantity:        {quantity}")
    print(f"Subtotal:        ${subtotal:.2f}")
    print(f"Discount:        {discount}% (-${discount_amount:.2f})")
    print(f"Tax Rate:        {tax_rate * 100}% (+${tax_amount:.2f})")
    print(f"Total Amount:    ${total_amount:.2f}")
    print("-" * 30 + "\n")
# i. Using only the required arguments (item and price)
print("Scenario i:")
generate_bill("Book", 15.0)
# ii. Providing a custom quantity while keeping default discount and tax
print("Scenario ii:")
generate_bill("Pen", 2.5, quantity=5)
# iii. Using named arguments for discount and tax while keeping default quantity
print("Scenario iii:")
generate_bill("Headphones", 80.0, discount=15, tax_rate=0.08)
# iv. Providing all arguments explicitly (Using the example values)
print("Scenario iv (Example Scenario):")
generate_bill(item="Laptop", price=50000, quantity=2, discount=10, tax_rate=0.05)


# Get user input
num_people = int(input("Enter the number of people: "))
cost_per_meal = float(input("Enter the cost of each meal: $"))
sales_tax_percentage = float(input("Enter the sales tax percentage: "))
tip_percentage = float(input("Enter the tip percentage: "))
# Calculate totals
total_cost_of_food = num_people * cost_per_meal
total_sales_tax = (sales_tax_percentage / 100) * total_cost_of_food
total_tip_amount = (tip_percentage / 100) * total_cost_of_food
total_bill_amount = total_cost_of_food + total_sales_tax + total_tip_amount
bill_per_person = total_bill_amount / num_people


# Print results
print(f"\nTotal Cost of Food: ${total_cost_of_food:.2f}")
print(f"Total Sales Tax: ${total_sales_tax:.2f}")
print(f"Total Tip Amount: ${total_tip_amount:.2f}")
print(f"Total Bill Amount: ${total_bill_amount:.2f}")
print(f"Bill Amount per Person: ${bill_per_person:.2f}")


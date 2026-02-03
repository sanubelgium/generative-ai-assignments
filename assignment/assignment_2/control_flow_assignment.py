## Assignment 2: Control Flow (Conditional & Loops)

# Task 1
order_input = input("Enter the order amount: ")
order_amount = int(order_input)


if order_input.isdigit():
    if order_amount >= 2000:
        discount_rate = 0.15
    elif order_amount >= 1500:
        discount_rate = 0.10
    elif order_amount >= 1000:
        discount_rate = 0.07
    else:
        discount_rate = 0.0
    discount = order_amount * discount_rate
    subtotal = order_amount - discount
    tax = subtotal * 0.05
    final_total = subtotal + tax

    print("Print for Task# 1")
    print("Original Amount:", order_amount)
    print("Discount:", discount)
    print("Subtotal:", subtotal)
    print("Tax (5%):", tax)
    print("Final Amount:", final_total)
else:
    print("Error: Please enter a valid number")

# Task 2
orders = [1200, 2500, 800, 1750, 3000]
total_revenue = 0
discounted_order = 0

for order in orders:
    if order >= 2000:
        discount = 0.15
    elif order >= 1500:
        discount = 0.10
    elif order >= 1000:
        discount = 0.07
    else:
        discount = 0.0
    
    if discount > 0:
        discounted_order += 1

    final_discount = order * discount
    final_total = order - final_discount
    total_revenue += final_total
    print(order, "->", discount,"%->",final_total)
    
print("Print for Task# 2")
print("Total Revenue:", total_revenue)
print("Discounted Orders:", discounted_order)

# Task 3
orders = []

while True:
    print("Menu")
    print("1 - Add order amount")
    print("2 - Show all orders and totals after discount")
    print("q - Quit")

    user_choice = input("Choose your option: ")

    if user_choice == "1":
        user_entered_amount = input("Enter order amount: ")
        if not user_entered_amount.isdigit():
            print("Invalid amount.")
            continue
        orders.append(int(user_entered_amount))

    elif user_choice == "2":
        if not orders:
            print("No orders yet.")
            continue

        for order in orders:
            if order >= 2000:
                discount_rate = 0.15
            elif order >= 1500:
                discount_rate = 0.10
            elif order >= 1000:
                discount_rate = 0.07
            else:
                discount_rate = 0.0

            discount = order * discount_rate
            final_amount = order - discount
            print(order, "->", final_amount)

    elif user_choice == "q":
        print("Exiting program.")
        break

    else:
        print("Invalid option.")
        continue

# Task 4
daily = [200, 150, 0, 400, 50, -1, 300]
total_sales = 0

for sale in daily:
    if sale == -1:
        print("Corrupted data found. Stopping.")
        break

    if sale == 0:
        print("No sales today.")
        continue

    total_sales += sale

print("Print for Task# 4")
print("Total Sales:", total_sales)
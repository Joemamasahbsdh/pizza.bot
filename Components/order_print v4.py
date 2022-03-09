# list to store ordered pizzas
order_list = ['Margherita', 'Pepperoni', 'Hawaiian','BBQ Chicken Deluxe']
# list to store pizza costs
order_cost = [8.50, 8.50, 8.50, 13.50]

cust_details = {"name": "Louis", "phone": "012345", "house": "21", "street": "Gian", "suburb": "FlatBush"  }

def print_order():
    total_cost = sum(order_cost)
    print ("Customer Details")
    print(f" \nCustomer Name: {cust_details['name']} \nCustomer Phone: {cust_details['phone']} \nCustomer Adress: {cust_details['house']} {cust_details['street']}  {cust_details['suburb']}")
    print ()
    print ("Order Details")
    count = 0 
    for item in order_list:
        print("Ordered: {} Cost ${:.2f}" .format(item, order_cost[count]))
        count = count+1
    print()
    print("Total Order Cost")
    print(f"${total_cost:.2f}")

print_order()
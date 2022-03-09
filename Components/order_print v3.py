# list to store ordered pizzas
order_list = ['Margherita', 'Pepperoni', 'Hawaiian','BBQ Chicken Deluxe']
# list to store pizza costs
order_cost = [8.50, 8.50, 8.50, 13.50]

cust_details = {"name": "Louis", "phone": "012345", "house": "21", "street": "Gian", "suburb": "FlatBush"  }




#print("\n Customer Name:{} Customer Phone:\n{} Customer House:\n{} Customer Street:\n{} Customer Suburb:\n{}".format(cust_details['name'],cust_details['phone'],cust_details['house'],cust_details['street'],cust_details['suburb']))
print(f" \nCustomer Name: {cust_details['name']} \nCustomer Phone: {cust_details['phone']} \nCustomer Adress: {cust_details['house']} {cust_details['street']}  {cust_details['suburb']}")

count = 0 
for item in order_list:
    print("Ordered: {} Cost ${:.2f}" .format(item, order_cost[count]))
    count = count+1
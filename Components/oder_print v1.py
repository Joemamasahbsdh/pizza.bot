# list to store ordered pizzas
order_list = ['Margherita', 'Pepperoni', 'Hawaiian','BBQ Chicken Deluxe']


count = 0 
for item in order_list:
    print("Ordered: {} Cost ${:.2f}" .format(item, order_cost[count]))
    count = count+1
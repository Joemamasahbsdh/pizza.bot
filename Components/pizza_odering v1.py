# list of pizza names
pizza_names = ['Margherita','Pepperoni','Hawaiian','Cheese','Italian','Vegie','Vegan',
                'Chicken Deluxe','Mega Meat Lovers','Seafood Deluxe','Apricot Chicken Deluxe','BBQ Chicken Deluxe'] 
# list of pizza prices
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

# list to store ordered pizzas
order_list = []
order_cost = []

def menu():
    number_pizas = 12
    for count in range (number_pizas):
        print("{} {} ${:.2f}".format(count+1,pizza_names[count],pizza_prices[count]))

menu()


# ask for total number of pizzas required 
num_pizzas = 0 

while True:
    num_pizzas = int(input("How many pizzas would you like to order?"))
    if num_pizzas >= 1 and num_pizzas <= 5:
        break
    else:
        print("Your order must be between 1 and 5")


print(num_pizzas)

#Choose pizza from menu
print("Plase chooes your pizzas by entering the number from the menu ")
for item in range (num_pizzas):
    while num_pizzas > 0: 
        pizza_ordered = int(input())
        order_list.append(pizza_names[pizza_ordered])
        order_cost.append(pizza_prices[pizza_ordered])
        print("{} ${:.2f}" .format(pizza_names[pizza_ordered],pizza_prices[pizza_ordered]))
        num_pizzas = num_pizzas -1 

print(order_list)
print(order_cost)




#Count down until all pizzas OrderedDict



#print order
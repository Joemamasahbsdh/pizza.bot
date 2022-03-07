pizza_names = ['Margherita','Pepperoni','Hawaiian','Cheese','Italian','Vegie','Vegan',
                'Chicken Deluxe','Mega Meat Lovers','Seafood Deluxe','Apricot Chicken Deluxe','BBQ Chicken Deluxe'] 

pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

def menu():

    number_pizas = 12

    #print("How many pizzas would you like to order?")
    #num_pizza = int(input())

    for count in range (number_pizas):
        print("{} {} ${:.2f}".format(count+1,pizza_names[count],pizza_prices[count]))


menu()
 
 
 
 
 
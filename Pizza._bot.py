# Pizza bot program
#Bugs - phone number input allows letters
#Bugs - name input allow numbers
import random 
from random import randint          

# list of random names
names  = ["Louis", "Gian", "Mikara", "Joaquin", "Tomboy", "BigBen", "Calicdan", "Barlo", "Yacob", "Marcas"]
# list of pizza names
pizza_names = ['Margherita','Pepperoni','Hawaiian','Cheese','Italian','Vegie','Vegan',
                'Chicken Deluxe','Mega Meat Lovers','Seafood Deluxe','Apricot Chicken Deluxe','BBQ Chicken Deluxe'] 
# list of pizza prices
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]
# list to store ordered pizzas
order_list = []
# list to store pizza costs
order_cost = []


#customer details dictionary
customer_details ={}

#validates inputs to check if they are blank 
def not_blank(question):
    valid = False 
    while not valid: 
        response = input(question)
        if response != "": 
            return response.title()
        else:
            print("This cannot be blank")


def welcome():
    '''
Purpose: To generate a random name from the list and print out 
a welcome message
Parameters: None
Returns: None 
    '''
    num = randint(0,9)
    name = (names[num])
    print("*** Welcome to Dream Pizza***")
    print("*** My name is",name, "***")
    print("***I am here to take your order***")

# Menu for pickup or deliver
def order_type():
    print ("Is your order for pickup or delivery?")
    print ("For pickup please enter 1.")
    print ("For delivery please enter 2.")
    while True: 
        try:
            delivery = int(input ("Please enter number ") )
            if delivery >= 1 and delivery <= 2: 
                if delivery == 1:
                    print ("Pickup")
                    pickup_info()
                    break
                elif delivery == 2:
                    print ("Delivery")
                    delivery_info()
                    break
                else:
                    print("number must be 1 or 2.")
        except ValueError: 
            print ("That is not a valid number")
            print ("Please enter 1 or 2")


# Pick up information - name and phone number
def pickup_info():
    question = ("Please enter your name")
    customer_details ['name'] = not_blank(question) 
    #print(customer_details ['name'])
   
    question = ("Please enter your number")
    customer_details ['phone'] = not_blank(question) 
    #print(customer_details ['phone'])
    print(customer_details)

# Delivery information - name address and phone
def delivery_info():
    question = ("Please enter your name")
    customer_details ['name'] = not_blank(question) 
    #print(customer_details ['name'])
   
    question = ("Please enter your number")
    customer_details ['phone'] = not_blank(question) 
    #print(customer_details ['phone'])
    
    question = ("Please enter your house number")
    customer_details ['house'] = not_blank(question) 
    print(customer_details ['house'])

    question = ("Please enter your street name")
    customer_details ['street'] = not_blank(question) 
    print(customer_details ['street'])

    question = ("Please enter your suburb")
    customer_details ['suburb'] = not_blank(question) 
    print(customer_details ['suburb'])
    


# Pizza menu
def menu():
    number_pizas = 12
    for count in range (number_pizas):
        print("{} {} ${:.2f}".format(count+1,pizza_names[count],pizza_prices[count]))







# Choose total number Pizzas - max 5
# PIzza ordering - from menu - print each pizza ordered with cost
def order_pizza():
# ask for total number of pizzas required 
    num_pizzas = 0 
    while True:
        try:
            num_pizzas = int(input("How many pizzas would you like to order?"))
            if num_pizzas >=1 and num_pizzas <= 5:
                break
            else:
                print("Your order must be between 1 and 5")
        except ValueError:
            print("That is not a valid number")
            print("Number must be between 1 and 5")
    #Choose pizza from menu
    for item in range (num_pizzas):
        while num_pizzas > 0: 
            while True:
                try:
                    pizza_ordered = int(input("Plase chooes your pizzas by entering the number from the menu"))
                    if pizza_ordered >=1 and pizza_ordered <= 12:
                        break
                    else:
                        print("Your pizza order must be between 1 and 12")
                except ValueError:
                    print("That is not a valid number")
                    print("Number must be between 1 and 12")
            pizza_ordered = pizza_ordered -1 
            order_list.append(pizza_names[pizza_ordered])
            order_cost.append(pizza_prices[pizza_ordered])
            print("{} ${:.2f}" .format(pizza_names[pizza_ordered],pizza_prices[pizza_ordered]))
            num_pizzas = num_pizzas -1 




# Print order out - including if order is del or pick up and names and price of each pizza - total cost including any delivery charge




# Ability to cancel or proceed with order 





# Option for new order or to exit







# Main function
def main():
         '''
        Purpose: To run all functions 
        a welcome message
        Parameters: None
        Returns: None 
         '''
         welcome()
         order_type()
         menu()
         order_pizza()

main()

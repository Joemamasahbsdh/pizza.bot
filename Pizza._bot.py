# Pizza bot program
import random 
from random import randint          

# list of random names
names  = ["Louis", "Gian", "Mikara", "Joaquin", "Tomboy", "BigBen", "Calicdan", "Barlo", "Yacob", "Marcas"]

# welcome message with randome name
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






# Pick up information - name and phone number






# Delivery information - name address and phone





# Choose total number Pizzas - max 5






# Pizza menu






# PIzza ordering - from menu - print each pizza ordered with cost





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


main()

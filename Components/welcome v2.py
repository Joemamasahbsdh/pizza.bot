import random 
from random import randint          

# list of random names
names  = ["Louis", "Gian", "Mikara", "Joaquin", "Tomboy", "BigBen", "Calicdan", "Barlo", "Yacob", "Marcas"]

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

    
def main():
         '''
        Purpose: To run all functions 
        a welcome message
        Parameters: None
        Returns: None 
         '''
         welcome()


main()

# Pizza bot program
import random
from random import randint

#List of random names
names = ["James", "Mark", "John", "Pheobe", "Sally", "Michael", "Denise", "Ellen", "Bob", "Joe"]

# Customer details dictionary
customer_details = {}

# Validates inputs to check if they are blank

def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response.title() 
        else:
            print("This cannot be blank")

# Welcome message with random name

def welcome():
    '''
    Purpose: To generate a random name from the list and print out
    a welcome message
    Parameters: none
    Returns: none
    '''

    num = randint(0,9)

    name = (names[num])

    print("*** Welcome to Dream Pizza ***")
    print("*** My name is",name,"***")
    print("*** I will be here to help you order your delicious Dream Pizza ***")

# Menu for pickup and delivery

def order_type():
    print ("Is your order for pickup or delivery?")

    print ("For pickup please enter 1")
    print ("For delivery please enter 2")

    while True:
        try:
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print ("Pickup")
                    pickup()
                    break

                elif delivery == 2:
                    print ("Delivery")
                    break
            else:
                print("The number must be 1 or 2")
        except ValueError:
            print ("That is not a valid number")
            print ("Please enter 1 or 2")



# Pickup information - name and phone number

def pickup():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)
    #print(customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    #print(customer_details['phone'])
    print(customer_details)


# Delivery information - name, address and phone number




# Choose total number of pizzas - max 5



# Pizza menu




# Pizza order - from menu - print each pizza ordered with cost



# Print order out - including if order is delivery or pickup and names and price of each pizza
# Total cost including any delivery charge



# Ability to cancel or proceed with order





# Option for new order or to exit





# Main function
def main():
    '''
    Purpose: To run all functions
    Parameters: none
    Returns: none
    '''
    welcome()
    order_type()


main()
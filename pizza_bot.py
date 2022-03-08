# Pizza bot program
# 24/02/2022
# Bugs - Phone number input allows letters
#      - Name input allows numbers

import random
from random import randint

#List of random names
names = ["James", "Mark", "John", "Pheobe", "Sally", "Michael", "Denise", "Ellen", "Bob", "Joe"]

# list of pizza names
pizza_names = ['Margerita', 'Pepperoni', 'Hawaiian', 'Cheese', 'Italian', 'Veggie', 'Vegan', 
              'Chicken Deluxe', 'Mega Meat Lovers', 'Seafood Deluxe', 'Apricot Chicken Deluxe',
               'BBQ Chicken Deluxe']
# list of pizza prices
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50 ,13.50, 13.50]

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
                    pickup_info()
                    break

                elif delivery == 2:
                    print ("Delivery")
                    delivery_info()
                    break
            else:
                print("The number must be 1 or 2")
        except ValueError:
            print ("That is not a valid number")
            print ("Please enter 1 or 2")



# Pickup information - name and phone number

def pickup_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)
    #print(customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    #print(customer_details['phone'])


# Delivery information - name, address and phone number

def delivery_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)
    print(customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    print(customer_details['phone'])
    
    question = ("Please enter your house number ")
    customer_details['house'] = not_blank(question)
    print(customer_details['house'])

    question = ("Please enter your street name ")
    customer_details['street'] = not_blank(question)
    print(customer_details['street'])

    question = ("Please enter your suburb name ")
    customer_details['suburb'] = not_blank(question)
    print(customer_details['suburb'])

# Pizza menu

def menu():
    number_pizzas = 12

    for count in range (number_pizzas):
        print ("{} {} ${:.2f}" .format(count+1, pizza_names[count], pizza_prices[count]))


# Choose total number of pizzas - max 5

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
    menu()


main()
pizza_names = ['Margerita', 'Pepperoni', 'Hawaiian', 'Cheese', 'Italian', 'Veggie', 'Vegan', 
              'Chicken Deluxe', 'Mega Meat Lovers', 'Seafood Deluxe', 'Apricot Chicken Deluxe',
               'BBQ Chickeh Deluxe']
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50 ,13.50, 13.50]

def menu():
    number_pizzas = 12

    for count in range (number_pizzas):
        print ("{} {} ${:.2f}" .format(count+1, pizza_names[count], pizza_prices[count]))
menu()
# ask for total number of pizzas for order
num_pizzas = 0

num_pizzas = input("How many pizzas do you want to order? ")

print(num_pizzas)

# choose pizza from menu




# count down until all pizzas are ordered



# print order
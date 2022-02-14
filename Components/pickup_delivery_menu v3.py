# Menu so that user can choose either pickup or delivery

print ("Is your order for pickup or delivery?")

print ("For pickup please enter 1")
print ("For delivery please enter 2")



low = 1
high = 2

while True:
    try:
        delivery = int(input())

        if delivery == 1:
            print ("Pickup")

        elif delivery == 2:
            print ("Delivery")

        else:
            print ("That was not a valid input")
    
    except ValueError:
        print ("That is not a valid number")
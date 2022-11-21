print("The Invoice Line Item Calculator")

def prices():
    logical = True
    global price
    while logical:
        try:
            price = float(input("Eanter Price: ")) 
            logical = False
        except ValueError:
            print("Invalid decimal number. Please try again.")
def number_quantity():
    logical = True 
    global qty
    while logical: 
        try: 
            qty = int(input("Enter Qty: "))
            logical = False
        except ValueError: 
            print("Invalid decimal number. Please try again.")
def quantity_prices():
    global totalPrices 
    totalPrices = price * qty
def printTotals():
    print(f"Price:  ${price:,.2f}")
    print(f"Quantity:    {qty}")
    print(f"Total:   ${totalPrices:,.2f}")
cont = True 
while cont:
    prices()
    number_quantity()
    quantity_prices()
    printTotals()
    contIn = input("Enter another line item? (y/n): ")
    if contIn.lower() == "n":
        print("")
        cont = False 
if not cont:
    print("Have a good day!") 




    
     



# Write a while loop that will:

# Call a function that will prompt the user to enter a price. The price must be a float. If a value is entered in an invalid format a message will display and the user will be prompted to enter another price, otherwise return the value in price.
# Call a function that will prompt the user to enter a quantity. The price must be an integer. If a value is entered in an invalid format a message will display and the user will be prompted to enter another quantity, otherwise return the value in quantity
# Compute the total by multiplying quantity times price.
# Display the totals in the format shown in the sample screenshot
# Prompt the user to enter another line item. If the user enters a y continue, if the user enters an n end the program.
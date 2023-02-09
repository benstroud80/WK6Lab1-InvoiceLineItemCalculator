#!?usr/bin/env python3

def get_price():
    while True:
        try:
            price = float(input('Enter price: '))
            return price
        except ValueError:
            print('Invalid decimalnumber. Please try again.')

def get_quantity():
    while True:
        try:
            quantity = int(input('Enter quantity:'))
            return quantity
        except ValuError:
            print('Invalid integer. Please try again.')

def main():
    print('The Invoice Line Item Calculaltor\n')

    answer = 'y'
    while answer.lower() == 'y':
        #get the price and quantity
        price = get_price()
        quantity = get_quantity()

        #calculate the total
        total = price * quantity()

        #display the results
        print()
        print('Price:       ', f"{price: .2f}")
        print('QUANTITY')
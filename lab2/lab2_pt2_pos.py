#!/usr/bin/python3

price = float(input('What is the price of the item? '))

discount = float(input('What is the percentage discount? '))

savings = price * discount
price -= savings

print('The discounted price is ${:3,.2f}'.format(price))

tax = price * 0.07
price += tax

print('Total Amount: ${:3,.2f}'.format(price))
print('Sales Tax: ${:3,.2f}'.format(tax))
print('You Saved: ${:3,.2f}'.format(savings))


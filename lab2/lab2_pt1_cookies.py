#!/usr/bin/python3

sugar = 1.5
butter = 1.0
flour = 2.75

cookies = int(input('How many cookies do you want to bake? '))
ratio = cookies / 48

# This is a long string, so we're going to build it over two lines
output = 'You need {:3.2f} cups of sugar, {:3.2f} cups of butter, '
output += ' {:3.2f} cups of flour'
print(output.format(sugar * ratio, butter * ratio, flour * ratio))




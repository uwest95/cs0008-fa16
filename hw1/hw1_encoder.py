#!/usr/bin/python3

orig_message = input('Please enter your message: ')
message = orig_message + ' ' * 10
message = message[:10].upper()

encoder = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '

pin = input('Please enter your 3 digit pin: ')

# Step 1:
encoded = 0
step1 = encoder.find(message[0])
step1 += encoder.find(message[3])
step1 += encoder.find(message[6])
step1 *= int(pin[0])
print(step1)
encoded = step1

# Step 2:
step2 = encoder.find(message[1])
step2 *= encoder.find(message[4])
step2 *= encoder.find(message[7])
step2 //= int(pin[1])
print(step2)
encoded += step2

# Step 3:
step3 = encoder.find(message[2]) + int(pin[2])
step3 += encoder.find(message[5]) + int(pin[2])
step3 += encoder.find(message[8]) + int(pin[2])
step3 = step3 ** 2
print(step3)
encoded -= step3

print('Unencoded message: "{}"'.format(orig_message))
print('Encoded message: "{}"'.format(encoded))

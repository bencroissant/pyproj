import random

print('welcome to your free password generator!')

chars = 'qewrtyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@£$%^&*()_+-=[]{};:'">.<,`~1234567890"


length = input('how long should your password be? no of chars: ')
length = int(length)

print('\nhere is your password:')

for pwd in range(length):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
print(passwords)
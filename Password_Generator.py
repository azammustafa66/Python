import random

alphabets =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'k', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '_']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

password = ""
password_list = []
for i in range(3):
    password_list.append(random.choice(alphabets))
for j in range(3):
    password_list.append(random.choice(symbols))
for k in range(3):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

for l in password_list:
    password += l

print(password, end="")
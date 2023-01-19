import random as rd

names = input("Enter everybody's name separated by ',': ")
sep_names = names.split(",")
print(rd.choice(sep_names))

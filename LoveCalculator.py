your_name = input("Enter your name: ")
crush_name = input("Enter your crush's name: ")

combined = your_name + crush_name
lower_case = combined.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")
true = t + r + u + e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")
love = l + o + v + e

total = str(true) + str(love)
print(total)
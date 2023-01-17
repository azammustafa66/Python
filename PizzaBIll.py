size = input("What size pizza do you want S, M or L?: ")
add_p = input("Do want add p topping?(Y or N): ")
extra_c = input("Do want extra cheese?: ")
bill = 0
if size == "S":
    bill += 15
if size == "M":
    bill += 20
else:
    bill += 25

if add_p == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_c == "Y":
    bill += 1

print(f"Your total bill is ${bill}")
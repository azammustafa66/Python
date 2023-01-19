print("Welcome to the tip calculator")
bill = float(input("What is the bill amount: Rs."))
people = int(input("Number of people to be shared: "))
tip = int(input("What % of bill would you like to tip: "))

bill += bill * (tip / 100)
bill_per_head = float(bill / people)

print("The bill per head will be Rs.",f"{bill_per_head : .2f}")

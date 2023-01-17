def main():
    year = int(input("Enter a year: "))
    leap_check(year)

def leap_check(year):
    if year % 400 == 0 | year % 4 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

main()
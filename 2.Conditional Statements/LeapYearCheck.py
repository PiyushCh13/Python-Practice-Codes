#365.2425 = 365 + 0.25 - 0.01 + 0.0025
#365.2425 = 365 + 1/4 - 1/100 + 1/400

year = int(input("Enter a year: "))

if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print(f"{year} is a Leap Year.")
        else:
            print(f"{year} is not a Leap Year.")
    else:
        print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")
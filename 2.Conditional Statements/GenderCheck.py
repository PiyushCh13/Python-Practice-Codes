gender = input("Enter your gender (M/F): ")

if(gender == 'M' or gender == 'm'):
    print("You are Male.")
elif(gender == 'F' or gender == 'f'):
    print("You are Female.")
else:
    print("Invalid input. Please enter 'M' for Male or 'F' for Female.")
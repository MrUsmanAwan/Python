print("Welcome to Leap Year Checker")
year = int(input("Enter a Year: "))
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("It's a Leap Year")
        else:
            print("Not a Leap Year")    
    else:
        print("It's a Leap Year")
else:
    print("Not a leap Year")    
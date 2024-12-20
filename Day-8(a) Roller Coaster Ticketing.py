print("Welcome To Roller Coaster Ride") 
height = float(input("What is your 'Height' in 'Feet'?\n")) 
if height >= 5.2: 
    print("You can Ride") 
    age = int(input("What's Your 'Age'?\n")) 
    if age < 12: 
        bill = 200
        print("Pay Rs-200") 
    elif age < 18: 
        bill = 300 
        print("Pay Rs-300") 
    else: 
        bill = 350 
        print("Pay Rs-350") 
    photo = input("Want Photo 'yes' or 'no':\n") 
    if photo == "yes": 
        bill = bill + 50 
        print(f"Your Total Bill is Rs-{bill}") 
    else: 
        print(f"Pay Rs-{bill}") 
else: 
    print("You Can't Ride, Sorry!") 

print("Welcome to Roller Coaster")
age = int(input("Your Age in Years? \n"))
if age<=15 :
    print("Sorry, You are not Allowed!")
elif age<=18:
    print("Please Pay Rs200 for Ticket")
elif age<=25:
    print("Please Pay Rs300 for Ticket")
elif age<=60:
    print("Please Pay Rs400 for Ticket")
else:
    print("Sorry, You are Not Allowed")   
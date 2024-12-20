print("Welcome To Pizza Buzz")
menu = input("Menu\n(1):Small Pizza ('s') -$15\n(2):Medium Pizza ('m')-$20\n(3):Large Pizza ('l')-$25\n:")
if menu == 's' :
    bill=15
    peporoni = input("Add Peporonni For Small-Pizza\nPrice: $2\n (y or n)\n:")
    if peporoni == 'y':
        bill+=2
    elif peporoni == 'n':
        bill+=0
    else:
        print("Choose Correct Please")

elif menu == 'm':
    bill=20
    peporoni = input("Add Peporonni For Medium-Pizza\nPrice: $3\n (y or n)\n:")
    if peporoni == 'y':
        bill+=3
    elif peporoni == 'n':
        bill+=0
    else:
        print("Choose Correct Please")        
elif menu == 'l': 
    bill=25
    peporoni = input("Add Peporonni For Large-Pizza\nPrice: $3\n (y or n)\n:")
    if peporoni == 'y':
        bill+=3
    elif peporoni == 'n':
        bill+=0
    else:
        print("Choose Correct Please")
else:
    print("Please Choose Correct Size")
bill=bill
cheese = input("Cheese for any Pizza is for $1\n(y or n)\n:")
if cheese == 'y':
    bill+=1
elif cheese == 'n':
    bill+=0
else:
    print("Choose Correct Please")
print(f"Your Total Bill is ${bill}")            


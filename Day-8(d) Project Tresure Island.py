print('"WELCOME TO TRESURE ISLAND"\n"Your Mission is to Find Tresure"')
direction = input('''You're at a Cross-Road. Where you want to go?\nType "left" or "right":\n''' )
if direction == 'right':
    print("Game-Over!")
elif direction == 'left':
    print("You come to lake.\nThere is an Island in the middle of the lake.")
    opt = input('Type "wait" to wait for a boat.\nType "swim" to swim across:\n')
    if opt == 'swim':
        print("Game-Over!")
    elif opt == "wait":
        print("You arrived at the Island Unharmed")
        door = input("There is a house with 3 doors.\n(1):red\n(2):yellow\n(3):blue:\n")
        if door == 'red':
            print("Game-Over!")
        elif door == 'yellow':
            print("You Win!")
        elif door == 'blue':
            print("Game-Over!")
        else:
            print("Please Choose Correct Option!!!")    
    else:
        print("Please Choose Correct Option!!!")           
else:
    print("Please Choose Correct Option!!!")
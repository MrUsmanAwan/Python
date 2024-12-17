print("Bill and Tip Calculator")
bill = float(input("Enter Total Amount of Bill: \n"))
tip = float(input("Enter Percentage for 'Tip': \n"))
tip_0 = bill*tip/100
total_bill = bill + tip_0
print("Total Bill After Tip:",total_bill)
people = int(input("People for Spilliting: \n"))
split = round(total_bill/people,2)
print("Per Head =",split)
print("Thanks For Using")
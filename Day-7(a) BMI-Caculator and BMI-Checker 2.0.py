print("Welcome to BMI Calculator")
height = float(input("Enter your 'Height' in 'Meters': "))
weight = float(input("Enter your 'Weight' in 'KiloGrams': "))
BMI = weight/height**2
print("Your BMI is",BMI)
if BMI<=18.5 :
    print("You are 'Under-Weight'")
elif BMI<=25 :
    print("You have 'Normal-Weight'")
elif BMI<=30 :
    print("You are 'Slightly Over-Weight'")
elif BMI<=35 :
    print("You are 'Obese'")
elif BMI>35:
    print("You are 'clinically-Obese'")            
print("Weeks you have left in your lifetime if you reach 90")
years = input("Your AGE: ")
rem_years = 90-int(years)
age_in_weeks = rem_years*52
print(f"You have {age_in_weeks} weeks left.")
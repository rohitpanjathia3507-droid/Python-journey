# day2_age_calculator.py
import datetime
birth_year = int(input("Enter your birth year: "))
present_year = datetime.datetime.now().year
your_age = present_year - birth_year
print("Your age is:", your_age)
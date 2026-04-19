# day3_grade_checker.py
marks = int(input("Enter marks: "))
if marks > 100 or marks < 0:
    print("Wrong input")
elif marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
elif marks >= 35:
    print("Grade: E")
else:
    print("Grade: F")
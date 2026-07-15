"""
=========================================================
        MINI PROJECT

        Student Grade System

Python for AI

Author: Muhammad Sohail Akhtar
=========================================================
"""

print("=" * 65)
print("             STUDENT GRADE SYSTEM")
print("=" * 65)

# -----------------------------------------
# Student Information
# -----------------------------------------

name = input("Student Name        : ")
roll_no = input("Roll Number         : ")
department = input("Department          : ")

print("\nEnter Marks (Out of 100)")

math = float(input("Mathematics         : "))
physics = float(input("Physics             : "))
programming = float(input("Programming         : "))
english = float(input("English             : "))
ai = float(input("Artificial Intelligence : "))

# -----------------------------------------
# Calculations
# -----------------------------------------

total = math + physics + programming + english + ai

percentage = total / 5

# -----------------------------------------
# Grade Calculation
# -----------------------------------------

if percentage >= 90:
    grade = "A+"
    remarks = "Outstanding"

elif percentage >= 80:
    grade = "A"
    remarks = "Excellent"

elif percentage >= 70:
    grade = "B"
    remarks = "Very Good"

elif percentage >= 60:
    grade = "C"
    remarks = "Good"

elif percentage >= 50:
    grade = "D"
    remarks = "Satisfactory"

else:
    grade = "F"
    remarks = "Needs Improvement"

# -----------------------------------------
# Pass / Fail
# -----------------------------------------

if percentage >= 50:
    status = "PASS"
else:
    status = "FAIL"

# -----------------------------------------
# Report Card
# -----------------------------------------

print("\n")
print("=" * 65)
print("                STUDENT REPORT CARD")
print("=" * 65)

print(f"Student Name : {name}")
print(f"Roll Number  : {roll_no}")
print(f"Department   : {department}")

print("-" * 65)

print(f"Mathematics              : {math}")
print(f"Physics                  : {physics}")
print(f"Programming              : {programming}")
print(f"English                  : {english}")
print(f"Artificial Intelligence  : {ai}")

print("-" * 65)

print(f"Total Marks : {total:.2f}/500")
print(f"Percentage  : {percentage:.2f}%")
print(f"Grade       : {grade}")
print(f"Status      : {status}")
print(f"Remarks     : {remarks}")

print("=" * 65)
print("Thank you for using Student Grade System!")
print("=" * 65)
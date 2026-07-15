"""
=========================================================
             MINI PROJECT
         Student Information System

Python for AI
Author: Muhammad Sohail Akhtar
=========================================================
"""

print("=" * 60)
print("        STUDENT INFORMATION SYSTEM")
print("=" * 60)

# ------------------------------------
# Student Input
# ------------------------------------

name = input("Enter Student Name       : ")
roll_no = input("Enter Roll Number        : ")
department = input("Enter Department         : ")
semester = input("Enter Semester           : ")

age = int(input("Enter Age                : "))
cgpa = float(input("Enter CGPA               : "))

# ------------------------------------
# Display Student Information
# ------------------------------------

print("\n" + "=" * 60)
print("          STUDENT PROFILE")
print("=" * 60)

print(f"Name        : {name}")
print(f"Roll No.    : {roll_no}")
print(f"Department  : {department}")
print(f"Semester    : {semester}")
print(f"Age         : {age}")
print(f"CGPA        : {cgpa:.2f}")

print("=" * 60)

# ------------------------------------
# Academic Status
# ------------------------------------

if cgpa >= 3.5:
    status = "Excellent"
elif cgpa >= 3.0:
    status = "Very Good"
elif cgpa >= 2.5:
    status = "Good"
elif cgpa >= 2.0:
    status = "Satisfactory"
else:
    status = "Needs Improvement"

print(f"Academic Status : {status}")

print("=" * 60)
print("Thank you for using the Student Information System!")
print("=" * 60)
"""
=========================================================
        Python for AI
Lesson 04: Conditional Statements Practice

Author: Muhammad Sohail Akhtar
Repository: Python-for-AI
=========================================================
"""

print("=" * 60)
print("LESSON 04: CONDITIONAL STATEMENTS PRACTICE")
print("=" * 60)

# =====================================================
# 1. Check Voting Eligibility
# =====================================================

print("\n1. Voting Eligibility")

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# =====================================================
# 2. Positive or Negative Number
# =====================================================

print("\n2. Positive or Negative Number")

number = float(input("Enter a number: "))

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")

# =====================================================
# 3. Even or Odd
# =====================================================

print("\n3. Even or Odd")

num = int(input("Enter an integer: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# =====================================================
# 4. Largest of Two Numbers
# =====================================================

print("\n4. Largest Number")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print(f"{a} is larger.")
elif b > a:
    print(f"{b} is larger.")
else:
    print("Both numbers are equal.")

# =====================================================
# 5. Grade System
# =====================================================

print("\n5. Grade System")

marks = float(input("Enter marks (0-100): "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

# =====================================================
# 6. Scholarship Eligibility
# =====================================================

print("\n6. Scholarship Eligibility")

cgpa = float(input("Enter CGPA: "))
attendance = float(input("Enter Attendance (%): "))

if cgpa >= 3.50 and attendance >= 85:
    print("Congratulations! Scholarship Approved.")
else:
    print("Scholarship Not Approved.")

# =====================================================
# 7. AI Example
# =====================================================

print("\n7. AI Prediction Example")

probability = float(input("Enter prediction probability (0-1): "))

if probability >= 0.80:
    print("Prediction: Positive")
else:
    print("Prediction: Negative")

print("\nLesson 04 Practice Completed Successfully!")
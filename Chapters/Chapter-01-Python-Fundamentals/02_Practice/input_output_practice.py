"""
=========================================================
        Python for AI
Lesson 03: Input, Output, and Type Casting Practice

Author: Muhammad Sohail Akhtar
Repository: Python-for-AI
=========================================================
"""

print("=" * 60)
print("LESSON 03: INPUT, OUTPUT, AND TYPE CASTING PRACTICE")
print("=" * 60)

# =====================================================
# 1. User Input
# =====================================================

print("\n1. User Input")

name = input("Enter your name: ")
print(f"Welcome, {name}!")

# =====================================================
# 2. Integer Input
# =====================================================

print("\n2. Integer Input")

age = int(input("Enter your age: "))
print(f"You are {age} years old.")

# =====================================================
# 3. Float Input
# =====================================================

print("\n3. Float Input")

height = float(input("Enter your height (meters): "))
print(f"Your height is {height} meters.")

# =====================================================
# 4. Addition of Two Numbers
# =====================================================

print("\n4. Addition")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum_result = num1 + num2

print(f"Sum = {sum_result}")

# =====================================================
# 5. Type Conversion
# =====================================================

print("\n5. Type Conversion")

number = "100"

print("Original Value:", number)
print("Original Type :", type(number))

number = int(number)

print("Converted Value:", number)
print("Converted Type :", type(number))

# =====================================================
# 6. Implicit Type Casting
# =====================================================

print("\n6. Implicit Type Casting")

a = 15
b = 4.5

result = a + b

print("Result:", result)
print("Result Type:", type(result))

# =====================================================
# 7. Formatted Output
# =====================================================

print("\n7. Formatted Output")

student = "Ali"
cgpa = 3.82

print(f"Student Name : {student}")
print(f"CGPA         : {cgpa}")

# =====================================================
# 8. AI Example
# =====================================================

print("\n8. AI Example")

learning_rate = float(input("Learning Rate: "))
epochs = int(input("Epochs: "))
accuracy = float(input("Accuracy: "))

print("\nTraining Configuration")
print("------------------------")
print(f"Learning Rate : {learning_rate}")
print(f"Epochs        : {epochs}")
print(f"Accuracy      : {accuracy}")

print("\nPractice Completed Successfully!")
"""
=========================================================
        Python for AI

Lesson 06: Functions Practice

Author: Muhammad Sohail Akhtar
Repository: Python-for-AI
=========================================================
"""

print("=" * 65)
print("LESSON 06: FUNCTIONS PRACTICE")
print("=" * 65)


# =====================================================
# 1. Greeting Function
# =====================================================

def greet(name):
    print(f"Hello {name}, Welcome to Python for AI!")

print("\n1. Greeting Function")
greet("Sohail")


# =====================================================
# 2. Square of a Number
# =====================================================

def square(number):
    return number ** 2

print("\n2. Square Function")
num = int(input("Enter a number: "))
print("Square =", square(num))


# =====================================================
# 3. Area of a Rectangle
# =====================================================

def rectangle_area(length, width):
    return length * width

print("\n3. Rectangle Area")

length = float(input("Enter Length: "))
width = float(input("Enter Width: "))

print("Area =", rectangle_area(length, width))


# =====================================================
# 4. Largest of Two Numbers
# =====================================================

def largest(a, b):

    if a > b:
        return a
    else:
        return b

print("\n4. Largest Number")

a = float(input("First Number: "))
b = float(input("Second Number: "))

print("Largest =", largest(a, b))


# =====================================================
# 5. Even or Odd
# =====================================================

def even_or_odd(number):

    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("\n5. Even or Odd")

number = int(input("Enter Number: "))
print(even_or_odd(number))


# =====================================================
# 6. Factorial
# =====================================================

def factorial(n):

    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact

print("\n6. Factorial")

n = int(input("Enter Number: "))
print("Factorial =", factorial(n))


# =====================================================
# 7. Average Marks
# =====================================================

def average_marks(m1, m2, m3):

    return (m1 + m2 + m3) / 3

print("\n7. Average Marks")

m1 = float(input("Marks 1: "))
m2 = float(input("Marks 2: "))
m3 = float(input("Marks 3: "))

print("Average =", average_marks(m1, m2, m3))


# =====================================================
# 8. Celsius to Fahrenheit
# =====================================================

def celsius_to_fahrenheit(c):

    return (c * 9 / 5) + 32

print("\n8. Temperature Conversion")

temp = float(input("Temperature (°C): "))

print("Temperature (°F):", celsius_to_fahrenheit(temp))


# =====================================================
# 9. GPA Calculator
# =====================================================

def calculate_gpa(total_points, total_courses):

    return total_points / total_courses

print("\n9. GPA Calculator")

points = float(input("Total Grade Points: "))
courses = int(input("Total Courses: "))

print("GPA =", round(calculate_gpa(points, courses), 2))


# =====================================================
# 10. Simple Calculator
# =====================================================

def calculator(a, b, operator):

    if operator == "+":
        return a + b

    elif operator == "-":
        return a - b

    elif operator == "*":
        return a * b

    elif operator == "/":

        if b != 0:
            return a / b
        else:
            return "Division by zero is not allowed."

    else:
        return "Invalid Operator"

print("\n10. Simple Calculator")

num1 = float(input("First Number : "))
num2 = float(input("Second Number: "))

op = input("Operator (+ - * /): ")

print("Result =", calculator(num1, num2, op))


# =====================================================
# 11. AI Example
# =====================================================

def calculate_accuracy(correct, total):

    return (correct / total) * 100

print("\n11. AI Accuracy Example")

correct = int(input("Correct Predictions: "))
total = int(input("Total Predictions: "))

accuracy = calculate_accuracy(correct, total)

print(f"Model Accuracy = {accuracy:.2f}%")

print("\nLesson 06 Practice Completed Successfully!")
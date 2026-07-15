"""
=========================================================
        Python for AI

Lesson 05: Loops Practice

Author: Muhammad Sohail Akhtar
Repository: Python-for-AI
=========================================================
"""

print("=" * 60)
print("LESSON 05: LOOPS PRACTICE")
print("=" * 60)

# =====================================================
# 1. Print Numbers from 1 to 10
# =====================================================

print("\n1. Numbers from 1 to 10")

for i in range(1, 11):
    print(i)

# =====================================================
# 2. Even Numbers
# =====================================================

print("\n2. Even Numbers")

for i in range(2, 21, 2):
    print(i)

# =====================================================
# 3. Odd Numbers
# =====================================================

print("\n3. Odd Numbers")

for i in range(1, 20, 2):
    print(i)

# =====================================================
# 4. Sum of First 100 Numbers
# =====================================================

print("\n4. Sum of First 100 Numbers")

total = 0

for i in range(1, 101):
    total += i

print("Sum =", total)

# =====================================================
# 5. Multiplication Table
# =====================================================

print("\n5. Multiplication Table")

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# =====================================================
# 6. Factorial
# =====================================================

print("\n6. Factorial")

n = int(input("Enter a positive integer: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"Factorial of {n} = {factorial}")

# =====================================================
# 7. Fibonacci Series
# =====================================================

print("\n7. Fibonacci Series")

terms = int(input("Enter number of terms: "))

a = 0
b = 1

for _ in range(terms):
    print(a, end=" ")
    a, b = b, a + b

print()

# =====================================================
# 8. Star Pattern
# =====================================================

print("\n8. Star Pattern")

for i in range(1, 6):
    print("*" * i)

# =====================================================
# 9. Countdown
# =====================================================

print("\n9. Countdown")

count = 5

while count >= 1:
    print(count)
    count -= 1

print("Go!")

# =====================================================
# 10. AI Example
# =====================================================

print("\n10. AI Training Simulation")

epochs = 5

for epoch in range(1, epochs + 1):
    print(f"Epoch {epoch} completed successfully.")

print("\nLesson 05 Practice Completed Successfully!")
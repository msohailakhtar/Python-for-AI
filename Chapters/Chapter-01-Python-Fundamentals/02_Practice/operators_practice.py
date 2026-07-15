"""
=========================================================
        Python for AI
Lesson 02: Operators and Expressions Practice

Author : Muhammad Sohail Akhtar
Repository : Python-for-AI
=========================================================
"""

print("=" * 60)
print("OPERATORS PRACTICE")
print("=" * 60)

# =====================================================
# 1. Arithmetic Operators
# =====================================================

print("\n1. Arithmetic Operators")

a = 20
b = 6

print("a =", a)
print("b =", b)

print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)
print("Floor Division :", a // b)
print("Modulus        :", a % b)
print("Exponent       :", a ** 2)

# =====================================================
# 2. Comparison Operators
# =====================================================

print("\n2. Comparison Operators")

x = 15
y = 10

print("x == y :", x == y)
print("x != y :", x != y)
print("x > y  :", x > y)
print("x < y  :", x < y)
print("x >= y :", x >= y)
print("x <= y :", x <= y)

# =====================================================
# 3. Assignment Operators
# =====================================================

print("\n3. Assignment Operators")

number = 10

print("Original:", number)

number += 5
print("After += :", number)

number -= 2
print("After -= :", number)

number *= 4
print("After *= :", number)

number /= 2
print("After /= :", number)

# =====================================================
# 4. Logical Operators
# =====================================================

print("\n4. Logical Operators")

age = 22
cgpa = 3.60

print(age > 18 and cgpa > 3.0)
print(age > 25 or cgpa > 3.0)
print(not(age > 30))

# =====================================================
# 5. Identity Operators
# =====================================================

print("\n5. Identity Operators")

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print(list1 is list2)
print(list1 is list3)
print(list1 == list3)

# =====================================================
# 6. Membership Operators
# =====================================================

print("\n6. Membership Operators")

fruits = ["Apple", "Banana", "Orange"]

print("Apple" in fruits)
print("Mango" in fruits)
print("Banana" not in fruits)

# =====================================================
# 7. Bitwise Operators
# =====================================================

print("\n7. Bitwise Operators")

a = 5
b = 3

print("a & b :", a & b)
print("a | b :", a | b)
print("a ^ b :", a ^ b)
print("~a    :", ~a)
print("a << 1:", a << 1)
print("a >> 1:", a >> 1)

# =====================================================
# 8. Operator Precedence
# =====================================================

print("\n8. Operator Precedence")

print(10 + 5 * 2)
print((10 + 5) * 2)
print(2 ** 3 * 4)
print((2 ** 3) * 4)

# =====================================================
# 9. AI Example
# =====================================================

print("\n9. AI Example")

learning_rate = 0.01
epochs = 100
accuracy = 95.75

epochs += 1

print("Learning Rate :", learning_rate)
print("Epochs        :", epochs)
print("Accuracy      :", accuracy)

# =====================================================
# End
# =====================================================

print("\nLesson 02 Practice Completed Successfully!")
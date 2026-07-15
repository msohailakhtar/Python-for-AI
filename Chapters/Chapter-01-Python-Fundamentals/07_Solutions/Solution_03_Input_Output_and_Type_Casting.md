# Solution 03 – Input, Output, and Type Casting

## Chapter 01: Python Fundamentals

**Course:** Python for Artificial Intelligence

**Author:** Muhammad Sohail Akhtar

**Repository:** Python-for-AI

---

# Learning Objectives

After studying this solution, you should be able to:

- Take user input using input().
- Display output using print().
- Perform type casting.
- Convert between int, float, str, and bool.
- Build interactive Python programs.
- Understand the role of data conversion in AI applications.

---

# Assignment Solutions

## Question 1

Take user information as input and display it.

### Solution

```python
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

print("Name:", name)
print("Age:", age)
print("City:", city)
```

---

## Question 2

Perform arithmetic operations using user input.

### Solution

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
```

---

## Question 3

Convert Celsius to Fahrenheit.

### Solution

```python
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)
```

---

# Quiz Solutions

## Part A – Multiple Choice Questions

| Question | Answer |
|----------|:------:|
| Q1 | B |
| Q2 | D |
| Q3 | D |
| Q4 | B |
| Q5 | B |
| Q6 | C |
| Q7 | B |
| Q8 | B |
| Q9 | C |
| Q10 | B |

---

## Part B – True / False

| Question | Answer |
|----------|:------:|
| 1 | True |
| 2 | True |
| 3 | True |
| 4 | True |
| 5 | True |

---

# Explanation of Important Concepts

## Input Function

Used to receive data from the user.

Example:

```python
name = input("Enter your name: ")
```

---

## Output Function

Used to display information.

Example:

```python
print("Welcome to Python")
```

---

## Type Casting

Type casting converts one data type into another.

Examples:

```python
int("25")
float("3.14")
str(100)
bool(1)
```

---

## Common Conversion Functions

### Convert to Integer

```python
age = int("25")
```

### Convert to Float

```python
price = float("99.99")
```

### Convert to String

```python
text = str(100)
```

### Convert to Boolean

```python
status = bool(1)
```

---

# AI Connection

In Artificial Intelligence, data often comes from:

- Users
- Files
- Sensors
- APIs
- Databases

Before processing, data must be converted into appropriate types.

Examples:

```python
age = int(user_input)
salary = float(dataset_column)
```

Machine Learning models require numerical data, so type casting is essential.

---

# Common Mistakes

## Mistake 1

Adding user inputs without conversion.

Incorrect:

```python
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print(num1 + num2)
```

Output:

```text
1020
```

instead of

```text
30
```

---

Correct:

```python
num1 = int(input())
num2 = int(input())

print(num1 + num2)
```

---

## Mistake 2

Forgetting to convert decimal values.

Incorrect:

```python
price = int(input())
```

for

```text
12.5
```

This causes an error.

Use:

```python
price = float(input())
```

---

# Interview Questions

### Q1

Why does input() return a string?

### Q2

What is type casting?

### Q3

Difference between int() and float()?

### Q4

When is type conversion required?

### Q5

Why is type casting important in Machine Learning?

---

# Practice Challenge

Create a Student Result Calculator.

Requirements:

- Take student name.
- Take marks in three subjects.
- Calculate total marks.
- Calculate average marks.
- Display formatted results.

---

# Summary

In this lesson, you learned:

- Input using input()
- Output using print()
- Type casting
- int()
- float()
- str()
- bool()

These concepts are essential for building interactive applications and preparing data for Artificial Intelligence and Machine Learning systems.

---

**End of Solution 03**
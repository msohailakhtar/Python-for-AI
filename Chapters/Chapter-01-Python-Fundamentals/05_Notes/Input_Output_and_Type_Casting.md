# Input, Output, and Type Casting

## Chapter 01: Python Fundamentals

**Course:** Python for Artificial Intelligence

**Author:** Muhammad Sohail Akhtar

**Repository:** Python-for-AI

---

# Introduction

Almost every computer program interacts with users by receiving information (input), processing it, and displaying the results (output). Python provides simple built-in functions for these tasks.

Type casting allows us to convert data from one type to another, ensuring that mathematical operations and data processing work correctly.

Whether you are building a calculator, a web application, or an Artificial Intelligence system, input, output, and type conversion are fundamental programming concepts.

---

# Learning Objectives

After completing this lesson, you will be able to:

- Understand input and output in Python.
- Use the `input()` function.
- Display information using `print()`.
- Apply formatted output.
- Convert between Python data types.
- Build interactive Python programs.
- Understand the importance of type conversion in AI applications.

---

# What is Input?

Input is the data provided by a user or another source for processing by a program.

Python uses the `input()` function to receive user input.

Example:

```python
name = input("Enter your name: ")
```

The entered value is stored in the variable `name`.

---

# What is Output?

Output is the information displayed after processing.

Python uses the `print()` function.

Example:

```python
print("Welcome to Python for AI!")
```

---

# The input() Function

Syntax:

```python
variable = input("Message")
```

Example:

```python
city = input("Enter your city: ")

print(city)
```

---

# The print() Function

The `print()` function displays values on the screen.

Example:

```python
name = "Sohail"
age = 30

print(name)
print(age)
```

---

# Formatted Output

Using f-strings:

```python
name = "Ali"
age = 22

print(f"My name is {name} and I am {age} years old.")
```

Output:

```
My name is Ali and I am 22 years old.
```

---

# Why Does input() Return a String?

Regardless of what the user enters, `input()` returns a string.

Example:

```python
age = input("Enter Age: ")

print(type(age))
```

Output:

```
<class 'str'>
```

Therefore, numerical calculations require type conversion.

---

# Type Casting

Type casting converts one data type into another.

Common functions:

- `int()`
- `float()`
- `str()`
- `bool()`

---

## Integer Conversion

```python
age = int(input("Enter Age: "))
```

---

## Float Conversion

```python
price = float(input("Enter Price: "))
```

---

## String Conversion

```python
number = 25

text = str(number)
```

---

## Boolean Conversion

```python
print(bool(1))
print(bool(0))
```

Output:

```
True
False
```

---

# Practical Example

```python
name = input("Enter Name: ")
marks = float(input("Enter Marks: "))

print(f"Student: {name}")
print(f"Marks: {marks}")
```

---

# Real-World Example

An online shopping website asks the customer to enter:

- Name
- Address
- Phone Number
- Payment Details

The system processes the input and displays an order confirmation.

Similarly, AI applications collect user input before generating predictions or recommendations.

---

# Think Like an AI Engineer

Imagine you are building a student performance prediction system.

The program asks the user to enter:

- Study Hours
- Attendance Percentage
- Previous GPA

These values become inputs for a Machine Learning model that predicts the student's expected performance.

Without correct input handling and type conversion, the AI model cannot process the data accurately.

---

# Common Mistakes

## Forgetting Type Conversion

Incorrect:

```python
age = input("Enter Age: ")

print(age + 5)
```

Correct:

```python
age = int(input("Enter Age: "))

print(age + 5)
```

---

## Incorrect Conversion

Incorrect:

```python
marks = int("95.5")
```

Correct:

```python
marks = float("95.5")
```

---

## Using Wrong Variable Types

```python
price = "100"

total = price + 50
```

This results in an error because `price` is a string.

---

# Best Practices

- Always validate user input.
- Convert data to the correct type before calculations.
- Use descriptive prompts.
- Display meaningful output.
- Prefer f-strings for formatting.

---

# AI Applications

Input and output are used in:

- Chatbots
- Voice Assistants
- Recommendation Systems
- Medical Diagnosis Systems
- Face Recognition
- Autonomous Vehicles
- Machine Learning Prediction Systems

Example:

```python
age = int(input("Enter Customer Age: "))

salary = float(input("Enter Salary: "))
```

These values may be used by an AI model to predict loan approval or customer behavior.

---

# Summary

In this lesson, you learned:

- Input
- Output
- print()
- input()
- Type Casting
- Formatted Output
- Best Practices
- AI Applications

---

# Interview Questions

1. What is the purpose of the `input()` function?
2. Why does `input()` return a string?
3. Explain type casting with examples.
4. What is the difference between `print()` and `input()`?
5. How are input and output used in Machine Learning applications?

---

# Key Takeaways

✅ Every interactive program uses input and output.

✅ `input()` always returns a string.

✅ Type casting converts data into the required format.

✅ Formatted output improves readability.

✅ Correct input handling is essential for Artificial Intelligence systems.

---

**Next Lesson:** Conditional Statements
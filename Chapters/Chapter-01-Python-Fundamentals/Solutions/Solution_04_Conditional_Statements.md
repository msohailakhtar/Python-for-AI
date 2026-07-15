# Solution 04 – Conditional Statements

## Chapter 01: Python Fundamentals

**Course:** Python for Artificial Intelligence

**Author:** Muhammad Sohail Akhtar

**Repository:** Python-for-AI

---

# Learning Objectives

After studying this solution, you should be able to:

- Understand conditional statements.
- Use `if`, `elif`, and `else`.
- Apply comparison and logical operators in decision-making.
- Write nested conditional statements.
- Solve real-world decision-making problems.
- Understand how AI systems make decisions using conditions.

---

# Assignment Solutions

## Question 1

Determine whether a student has passed or failed.

### Solution

```python
marks = int(input("Enter marks: "))

if marks >= 50:
    print("Pass")
else:
    print("Fail")
```

---

## Question 2

Display the grade of a student.

### Solution

```python
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")
```

---

## Question 3

Determine whether a number is positive, negative, or zero.

### Solution

```python
number = float(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

---

## Question 4

Check whether a person is eligible to vote.

### Solution

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")
```

---

## Question 5

Check username and password.

### Solution

```python
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "PythonAI2026":
    print("Login Successful")
else:
    print("Invalid Username or Password")
```

---

# Quiz Solutions

## Part A – Multiple Choice Questions

| Question | Answer |
|----------|:------:|
| Q1 | B |
| Q2 | B |
| Q3 | B |
| Q4 | B |
| Q5 | B |
| Q6 | B |
| Q7 | B |
| Q8 | A |
| Q9 | B |
| Q10 | A |

---

## Part B – True / False

| Question | Answer |
|----------|:------:|
| 1 | True |
| 2 | False |
| 3 | True |
| 4 | True |
| 5 | True |

---

# Explanation of Important Concepts

## The `if` Statement

Executes code only when the condition is True.

Example:

```python
age = 20

if age >= 18:
    print("Adult")
```

---

## The `if...else` Statement

Provides two possible execution paths.

```python
marks = 45

if marks >= 50:
    print("Pass")
else:
    print("Fail")
```

---

## The `if...elif...else` Statement

Used when multiple conditions need to be checked.

```python
marks = 82

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
else:
    print("F")
```

---

## Nested Conditional Statements

A conditional statement inside another conditional statement.

```python
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to Vote")
```

---

## Logical Operators in Conditions

### AND

```python
if age >= 18 and citizen:
```

Both conditions must be True.

---

### OR

```python
if marks >= 90 or sports_certificate:
```

At least one condition must be True.

---

### NOT

```python
if not is_blocked:
```

Reverses the logical value.

---

# AI Connection

Conditional statements are fundamental in Artificial Intelligence.

Examples:

- Spam email detection
- Face recognition verification
- Loan approval systems
- Fraud detection
- Medical diagnosis
- Chatbot response selection
- Recommendation systems

Every AI system makes decisions based on conditions before producing predictions or actions.

---

# Common Mistakes

## Mistake 1

Using `=` instead of `==`.

❌ Incorrect

```python
if marks = 50:
```

✅ Correct

```python
if marks == 50:
```

---

## Mistake 2

Incorrect indentation.

❌ Incorrect

```python
if age >= 18:
print("Adult")
```

✅ Correct

```python
if age >= 18:
    print("Adult")
```

---

## Mistake 3

Forgetting the colon (`:`).

❌ Incorrect

```python
if marks >= 50
```

✅ Correct

```python
if marks >= 50:
```

---

# Interview Questions

### Q1

What is a conditional statement?

---

### Q2

Differentiate between `if`, `elif`, and `else`.

---

### Q3

Why is indentation important in Python?

---

### Q4

What are nested conditional statements?

---

### Q5

How are conditional statements used in Machine Learning and AI?

---

# Practice Challenge

Create a Python program that asks the user to enter:

- Username
- Password
- OTP

Display:

- Login Successful
- Invalid Credentials
- Access Denied

using nested conditional statements.

---

# Summary

In this lesson, you learned:

- `if` statement
- `if...else`
- `if...elif...else`
- Nested conditionals
- Logical operators
- Decision-making in Python

These concepts are essential for building intelligent systems because Artificial Intelligence relies on decision-making logic to analyze data and produce appropriate outcomes.

---

**End of Solution 04**
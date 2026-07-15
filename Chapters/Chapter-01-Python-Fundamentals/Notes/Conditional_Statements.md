# Conditional Statements

## Chapter 01: Python Fundamentals

**Course:** Python for Artificial Intelligence

**Author:** Muhammad Sohail Akhtar

**Repository:** Python-for-AI

---

# Introduction

Programs become intelligent when they can make decisions. Instead of executing every instruction sequentially, they evaluate conditions and choose different actions based on the results.

Python provides conditional statements such as `if`, `elif`, and `else` to control the flow of a program.

Conditional statements are widely used in Artificial Intelligence, Machine Learning, robotics, expert systems, recommendation engines, and autonomous systems where decisions are made based on available data.

---

# Learning Objectives

After completing this lesson, you will be able to:

- Understand conditional statements.
- Use `if`, `elif`, and `else`.
- Write nested conditional statements.
- Build decision-making programs.
- Apply conditional logic in AI applications.

---

# What is a Conditional Statement?

A conditional statement allows a program to make decisions based on whether a condition is `True` or `False`.

Example:

```python
age = 20

if age >= 18:
    print("Eligible to Vote")
```

---

# The if Statement

The `if` statement executes a block of code only when its condition is true.

Syntax:

```python
if condition:
    statements
```

Example:

```python
temperature = 35

if temperature > 30:
    print("Hot Weather")
```

---

# The if...else Statement

When the condition is false, the `else` block executes.

Example:

```python
marks = 45

if marks >= 50:
    print("Pass")
else:
    print("Fail")
```

---

# The if...elif...else Statement

Use `elif` to check multiple conditions.

Example:

```python
marks = 82

if marks >= 90:
    print("Grade A")

elif marks >= 80:
    print("Grade B")

elif marks >= 70:
    print("Grade C")

else:
    print("Needs Improvement")
```

---

# Nested if Statements

An `if` statement can be placed inside another `if` statement.

Example:

```python
age = 22
cgpa = 3.70

if age >= 18:
    if cgpa >= 3.50:
        print("Scholarship Eligible")
```

---

# Comparison Operators in Conditions

Common comparison operators:

| Operator | Meaning |
|----------|---------|
| == | Equal to |
| != | Not Equal to |
| > | Greater than |
| < | Less than |
| >= | Greater than or Equal to |
| <= | Less than or Equal to |

Example:

```python
salary = 120000

if salary > 100000:
    print("High Income")
```

---

# Logical Operators in Conditions

Logical operators combine multiple conditions.

### and

```python
age = 20
cgpa = 3.80

if age >= 18 and cgpa >= 3.50:
    print("Eligible")
```

### or

```python
if marks >= 90 or sports_certificate:
    print("Qualified")
```

### not

```python
registered = False

if not registered:
    print("Registration Required")
```

---

# Indentation in Python

Python uses indentation to define code blocks.

Correct:

```python
if True:
    print("Correct")
```

Incorrect:

```python
if True:
print("Incorrect")
```

Indentation errors will cause the program to fail.

---

# Real-World Example

An ATM machine checks:

- Is the PIN correct?
- Is there enough balance?
- Is the withdrawal amount within the daily limit?

Based on these conditions, the system approves or rejects the transaction.

---

# Think Like an AI Engineer

Suppose you are building a university admission prediction system.

The program evaluates:

- Entry Test Marks
- Interview Score
- Previous GPA

Using conditional statements, it decides whether the applicant is:

- Selected
- Waiting List
- Rejected

This is a simplified example of AI-based decision making.

---

# Common Mistakes

## Using = instead of ==

Incorrect:

```python
if marks = 90:
```

Correct:

```python
if marks == 90:
```

---

## Missing Colon

Incorrect:

```python
if age >= 18
```

Correct:

```python
if age >= 18:
```

---

## Incorrect Indentation

Incorrect:

```python
if age >= 18:
print("Eligible")
```

Correct:

```python
if age >= 18:
    print("Eligible")
```

---

# Best Practices

- Keep conditions simple and readable.
- Avoid unnecessary nested `if` statements.
- Use meaningful variable names.
- Add comments for complex logic.
- Test all possible cases.

---

# AI Applications

Conditional statements are widely used in:

- Face Recognition
- Spam Detection
- Medical Diagnosis
- Fraud Detection
- Recommendation Systems
- Autonomous Vehicles
- Intelligent Chatbots
- Credit Approval Systems

Example:

```python
accuracy = 95

if accuracy >= 90:
    print("Model Accepted")
else:
    print("Model Needs Improvement")
```

---

# Summary

In this lesson, you learned:

- if Statement
- if...else Statement
- if...elif...else Statement
- Nested if
- Comparison Operators
- Logical Operators
- Indentation
- Decision Making
- AI Applications

---

# Interview Questions

1. What is a conditional statement?
2. What is the difference between `if` and `if...else`?
3. When should you use `elif`?
4. Why is indentation important in Python?
5. How are conditional statements used in AI systems?

---

# Key Takeaways

✅ Conditional statements allow programs to make decisions.

✅ Python uses `if`, `elif`, and `else` for decision-making.

✅ Proper indentation is mandatory in Python.

✅ Logical operators help combine multiple conditions.

✅ Decision-making is a core component of Artificial Intelligence.

---

**Next Lesson:** Loops
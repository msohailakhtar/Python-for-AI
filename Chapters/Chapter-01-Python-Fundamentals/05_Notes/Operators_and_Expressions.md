# Operators and Expressions

## Chapter 01: Python Fundamentals

**Course:** Python for Artificial Intelligence

**Author:** Muhammad Sohail Akhtar

**Repository:** Python-for-AI

---

# Introduction

Operators are symbols that perform operations on variables and values. Expressions combine variables, operators, and values to produce new results.

Almost every Python program uses operators. Whether performing mathematical calculations, comparing values, making decisions, or training Artificial Intelligence models, operators are an essential part of programming.

---

# Learning Objectives

After completing this lesson, you will be able to:

- Understand Python operators.
- Perform arithmetic calculations.
- Compare values using comparison operators.
- Use logical operators.
- Apply assignment operators.
- Understand identity and membership operators.
- Perform basic bitwise operations.
- Apply operators in AI applications.

---

# What is an Operator?

An operator is a symbol that performs an operation on one or more operands.

Example:

```python
a = 10
b = 5

print(a + b)
```

Output:

```
15
```

Here:

- `+` is the operator.
- `a` and `b` are operands.

---

# What is an Expression?

An expression is a combination of variables, values, and operators that produces a result.

Example:

```python
total = marks + bonus
```

Another example:

```python
result = (a + b) * c
```

---

# Types of Operators in Python

Python provides several categories of operators.

---

# 1. Arithmetic Operators

Used for mathematical calculations.

| Operator | Description | Example |
|----------|-------------|---------|
| + | Addition | a + b |
| - | Subtraction | a - b |
| * | Multiplication | a * b |
| / | Division | a / b |
| // | Floor Division | a // b |
| % | Modulus | a % b |
| ** | Exponent | a ** b |

Example:

```python
a = 12
b = 5

print(a + b)
print(a % b)
print(a ** 2)
```

---

# 2. Comparison Operators

Used to compare two values.

| Operator | Meaning |
|----------|---------|
| == | Equal to |
| != | Not equal to |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal to |
| <= | Less than or equal to |

Example:

```python
marks = 85

print(marks >= 50)
```

Output:

```
True
```

---

# 3. Logical Operators

Used to combine conditions.

| Operator | Description |
|----------|-------------|
| and | Both conditions must be True |
| or | At least one condition must be True |
| not | Reverses the result |

Example:

```python
age = 20
cgpa = 3.8

print(age >= 18 and cgpa >= 3.5)
```

---

# 4. Assignment Operators

Used to assign and update values.

| Operator | Example |
|----------|---------|
| = | x = 10 |
| += | x += 5 |
| -= | x -= 5 |
| *= | x *= 2 |
| /= | x /= 2 |
| %= | x %= 3 |

Example:

```python
score = 50

score += 10

print(score)
```

---

# 5. Identity Operators

Used to compare object identity.

| Operator | Description |
|----------|-------------|
| is | Same object |
| is not | Different object |

Example:

```python
a = [1, 2]
b = a

print(a is b)
```

---

# 6. Membership Operators

Used to check whether a value exists inside a sequence.

| Operator | Description |
|----------|-------------|
| in | Present |
| not in | Not present |

Example:

```python
text = "Python for AI"

print("AI" in text)
```

---

# 7. Bitwise Operators

Operate on binary representations of integers.

| Operator | Description |
|----------|-------------|
| & | AND |
| \| | OR |
| ^ | XOR |
| ~ | NOT |
| << | Left Shift |
| >> | Right Shift |

Example:

```python
a = 5
b = 3

print(a & b)
print(a | b)
```

---

# Operator Precedence

Python follows precedence rules when evaluating expressions.

Example:

```python
result = 5 + 2 * 3
```

Output:

```
11
```

Multiplication is performed before addition.

Use parentheses to control evaluation.

```python
result = (5 + 2) * 3
```

Output:

```
21
```

---

# Common Mistakes

❌ Using `=` instead of `==`

```python
if marks = 90:
```

Correct:

```python
if marks == 90:
```

---

❌ Confusing `is` with `==`

Use:

- `==` for value comparison.
- `is` for object identity.

---

❌ Dividing integers without considering float output.

```python
10 / 3
```

Result:

```
3.3333333333333335
```

---

# Best Practices

- Use parentheses to improve readability.
- Keep expressions simple.
- Use meaningful variable names.
- Avoid deeply nested expressions.
- Prefer clarity over cleverness.

---

# AI Applications

Operators are widely used in AI and Machine Learning.

Examples include:

- Calculating model accuracy.
- Updating weights during training.
- Comparing prediction results.
- Evaluating loss functions.
- Setting learning rates.
- Implementing decision logic.

Example:

```python
learning_rate = 0.001
accuracy = 95.7

print(accuracy > 90)
```

---

# Summary

In this lesson you learned:

- Operators
- Expressions
- Arithmetic Operators
- Comparison Operators
- Logical Operators
- Assignment Operators
- Identity Operators
- Membership Operators
- Bitwise Operators
- Operator Precedence

---

# Interview Questions

1. What is an operator?
2. What is an expression?
3. Explain operator precedence.
4. What is the difference between `==` and `is`?
5. Where are operators used in Machine Learning?

---

# Key Takeaways

✅ Operators perform actions on data.

✅ Expressions combine values and operators.

✅ Use `==` for value comparison.

✅ Use `is` for identity comparison.

✅ Operators are essential in AI algorithms, data processing, and model evaluation.

---

**Next Lesson:** Input, Output, and Type Casting
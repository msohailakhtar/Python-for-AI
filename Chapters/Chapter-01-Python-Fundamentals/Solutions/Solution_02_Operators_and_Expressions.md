# Solution 02 – Operators and Expressions

## Chapter 01: Python Fundamentals

**Course:** Python for Artificial Intelligence

**Author:** Muhammad Sohail Akhtar

**Repository:** Python-for-AI

---

# Learning Objectives

After studying this solution, you should be able to:

- Understand arithmetic operators.
- Apply comparison operators.
- Use logical operators.
- Work with assignment operators.
- Understand identity and membership operators.
- Apply bitwise operators.
- Recognize the importance of operators in Artificial Intelligence.

---

# Assignment Solutions

## Question 1

Perform all arithmetic operations on two numbers.

### Solution

```python
a = 20
b = 6

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
```

---

## Question 2

Compare two numbers.

### Solution

```python
x = 15
y = 10

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
```

---

## Question 3

Demonstrate assignment operators.

### Solution

```python
number = 10

number += 5
print(number)

number -= 3
print(number)

number *= 2
print(number)

number /= 4
print(number)
```

---

## Question 4

Demonstrate logical operators.

### Solution

```python
age = 20
citizen = True

print(age >= 18 and citizen)
print(age < 18 or citizen)
print(not citizen)
```

---

## Question 5

Demonstrate identity and membership operators.

### Solution

```python
list1 = [1,2,3]
list2 = list1
list3 = [1,2,3]

print(list1 is list2)
print(list1 is list3)

print(2 in list1)
print(5 not in list1)
```

---

# Quiz Solutions

## Part A – Multiple Choice Questions

| Question | Answer |
|----------|:------:|
| Q1 | C |
| Q2 | C |
| Q3 | A |
| Q4 | A |
| Q5 | B |
| Q6 | B |
| Q7 | C |
| Q8 | B |
| Q9 | A |
| Q10 | B |

---

## Part B – True / False

| Question | Answer |
|----------|:------:|
| 1 | True |
| 2 | False |
| 3 | True |
| 4 | False |
| 5 | True |

---

# Explanation of Important Concepts

## Arithmetic Operators

Used for mathematical calculations.

Examples:

- +
- -
- *
- /
- //
- %
- **

---

## Comparison Operators

Used to compare values.

Examples:

```python
10 > 5
```

returns

```text
True
```

---

## Logical Operators

Used to combine multiple conditions.

```python
age > 18 and citizen
```

---

## Assignment Operators

Used to update variable values efficiently.

Instead of

```python
x = x + 5
```

write

```python
x += 5
```

---

## Identity Operators

Used to compare object identity.

```python
is

is not
```

---

## Membership Operators

Used to check whether a value exists inside a collection.

```python
in

not in
```

---

## Bitwise Operators

Operate directly on binary values.

Examples:

```python
&
|
^
~
<<
>>
```

Bitwise operators are commonly used in:

- Computer Graphics
- Networking
- Cryptography
- Embedded Systems

---

# AI Connection

Operators are fundamental in Artificial Intelligence.

Examples include:

- Comparing prediction accuracy.
- Updating model parameters.
- Checking training conditions.
- Implementing decision logic.
- Performing matrix and tensor computations.

---

# Common Mistakes

❌ Using `=` instead of `==`

Incorrect

```python
if x = 5:
```

Correct

```python
if x == 5:
```

---

❌ Confusing `/` and `//`

```python
10 / 3
```

returns

```text
3.3333
```

while

```python
10 // 3
```

returns

```text
3
```

---

# Interview Questions

### Q1

Difference between `/` and `//`.

### Q2

Difference between `==` and `is`.

### Q3

What are logical operators?

### Q4

Explain bitwise operators.

### Q5

Where are operators used in Machine Learning?

---

# Practice Challenge

Write a Python calculator that performs:

- Addition
- Subtraction
- Multiplication
- Division
- Modulus
- Exponentiation

using user input.

---

# Summary

In this lesson, you learned:

- Arithmetic Operators
- Comparison Operators
- Logical Operators
- Assignment Operators
- Identity Operators
- Membership Operators
- Bitwise Operators

These operators are the foundation of Python programming and are heavily used in Data Science, Artificial Intelligence, and Machine Learning.

---

**End of Solution 02**
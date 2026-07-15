# 📘 Chapter 01 Cheat Sheet – Python Fundamentals

## Python for Artificial Intelligence

**Course:** Python for Artificial Intelligence

**Author:** Muhammad Sohail Akhtar

**Repository:** Python-for-AI

---

# Quick Revision Guide

This cheat sheet provides a quick overview of all concepts covered in **Chapter 01 – Python Fundamentals**.

---

# 1. Variables

Store data in memory.

```python
name = "Ali"
age = 22
salary = 45000.50
```

Rules

- Start with a letter or underscore (_)
- Cannot start with a number
- Case-sensitive
- Use meaningful names

Example

```python
student_name = "Sara"
```

---

# 2. Data Types

| Data Type | Example |
|-----------|----------|
| int | 10 |
| float | 3.14 |
| str | "Python" |
| bool | True |

Check data type

```python
type(value)
```

---

# 3. Operators

## Arithmetic

```python
+
-
*
/
/
//
%
**
```

## Comparison

```python
==
!=
>
<
>=
<=
```

## Logical

```python
and
or
not
```

## Assignment

```python
=
+=
-=
*=
/=
```

---

# 4. Input

```python
name = input("Enter name: ")
```

Integer

```python
age = int(input())
```

Float

```python
salary = float(input())
```

---

# 5. Output

```python
print("Hello")
```

Formatted Output

```python
print(f"Name: {name}")
```

---

# 6. Type Casting

```python
int()

float()

str()

bool()
```

Example

```python
age = int("20")
```

---

# 7. Conditional Statements

## if

```python
if age >= 18:
    print("Adult")
```

---

## if...else

```python
if marks >= 50:
    print("Pass")
else:
    print("Fail")
```

---

## if...elif...else

```python
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
else:
    print("C")
```

---

# 8. Loops

## for Loop

```python
for i in range(5):
    print(i)
```

## while Loop

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

# Loop Control Statements

Break

```python
break
```

Continue

```python
continue
```

Pass

```python
pass
```

---

# 9. Functions

Create

```python
def greet():
    print("Hello")
```

Call

```python
greet()
```

Return

```python
def square(x):
    return x*x
```

---

# 10. Strings

Create

```python
text = "Python"
```

Indexing

```python
text[0]
```

Negative Index

```python
text[-1]
```

Slicing

```python
text[1:4]
```

---

# Common String Methods

```python
upper()

lower()

title()

strip()

split()

replace()

find()

count()

startswith()

endswith()
```

---

# Useful Built-in Functions

```python
print()

input()

type()

len()

max()

min()

sum()

round()

range()
```

---

# Common Errors

## Indentation Error

Incorrect

```python
if True:
print("Hello")
```

Correct

```python
if True:
    print("Hello")
```

---

## Syntax Error

Missing colon

```python
if age >= 18
```

Correct

```python
if age >= 18:
```

---

## Type Error

Incorrect

```python
"Age " + 20
```

Correct

```python
"Age " + str(20)
```

---

# Python Best Practices

- Use meaningful variable names.
- Follow proper indentation.
- Write reusable functions.
- Keep code simple and readable.
- Comment important code.
- Use f-strings for formatting.
- Avoid repeating code.

---

# Python in Artificial Intelligence

Python Fundamentals are used in:

- Machine Learning
- Deep Learning
- Data Science
- Computer Vision
- Natural Language Processing
- Robotics
- Reinforcement Learning
- Generative AI
- Large Language Models (LLMs)

---

# Important Interview Questions

- What is Python?
- What are variables?
- Difference between list and tuple?
- Difference between == and is?
- Difference between / and //?
- Difference between for and while?
- Difference between break and continue?
- Difference between parameters and arguments?
- What is type casting?
- What are f-strings?

---

# Chapter 01 Checklist

| Topic | Status |
|--------|:------:|
| Variables | ✅ |
| Data Types | ✅ |
| Operators | ✅ |
| Input & Output | ✅ |
| Type Casting | ✅ |
| Conditional Statements | ✅ |
| Loops | ✅ |
| Functions | ✅ |
| Strings | ✅ |

---

# What's Next?

In **Chapter 02**, you will build upon these fundamentals by exploring Python data structures such as:

- Lists
- Tuples
- Sets
- Dictionaries

These structures are essential for storing, organizing, and processing data in Artificial Intelligence and Machine Learning applications.

---

**End of Chapter 01 Cheat Sheet**
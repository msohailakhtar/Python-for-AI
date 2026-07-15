# Variables and Data Types

## Chapter 01: Python Fundamentals

**Course:** Python for Artificial Intelligence

**Author:** Muhammad Sohail Akhtar

**Repository:** Python-for-AI

---

# Introduction

Variables are one of the most fundamental concepts in programming. They allow us to store, modify, and retrieve information while a program is running.

Every Artificial Intelligence, Machine Learning, and Data Science application relies on variables to store data such as images, numerical values, model parameters, predictions, and user inputs.

---

# Learning Objectives

After completing this lesson, you should be able to:

- Understand variables.
- Create variables.
- Use meaningful variable names.
- Identify Python data types.
- Convert between data types.
- Apply variables in AI applications.

---

# What is a Variable?

A variable is a named memory location used to store data.

Example:

```python
name = "Sohail"
age = 30
```

Here,

- `name` stores a string.
- `age` stores an integer.

---

# Why Do We Need Variables?

Variables make programs flexible and reusable.

Without variables:

```python
print("Muhammad Sohail Akhtar")
```

With variables:

```python
name = "Muhammad Sohail Akhtar"

print(name)
```

The value can now be changed without modifying the rest of the code.

---

# Rules for Naming Variables

✅ Valid

```python
student_name
total_marks
learning_rate
age
cgpa
```

❌ Invalid

```python
2name
student-name
class
my name
total$
```

---

# Python Data Types

Python provides several built-in data types.

## Integer (int)

Stores whole numbers.

```python
age = 30
```

---

## Float

Stores decimal numbers.

```python
cgpa = 3.85
```

---

## String

Stores text.

```python
department = "Computer Science"
```

---

## Boolean

Stores True or False.

```python
passed = True
```

---

# Checking Data Types

Use:

```python
type(variable)
```

Example:

```python
name = "Ali"

print(type(name))
```

Output:

```
<class 'str'>
```

---

# Type Casting

Python allows conversion between data types.

Examples:

```python
int("25")

float(20)

str(100)

bool(1)
```

---

# Practical Example

```python
name = "Ayesha"

age = 21

cgpa = 3.76

print(name)
print(age)
print(cgpa)
```

---

# Common Mistakes

❌ Using keywords as variable names

```python
class = 5
```

❌ Beginning a variable with a number

```python
1student = "Ali"
```

❌ Forgetting quotation marks around strings

```python
name = Sohail
```

---

# Best Practices

- Use descriptive variable names.
- Follow snake_case naming.
- Keep names meaningful.
- Avoid single-letter variables unless appropriate.

---

# AI Applications

Variables are used to store:

- Training datasets
- Learning rate
- Number of epochs
- Batch size
- Accuracy
- Loss
- Predictions
- User input

Example:

```python
learning_rate = 0.001

epochs = 100

accuracy = 98.45
```

---

# Summary

In this lesson you learned:

- Variables
- Data Types
- Type Casting
- Naming Rules
- Best Practices
- AI Applications

---

# Interview Questions

1. What is a variable?
2. What is the difference between int and float?
3. Explain type casting.
4. What is snake_case?
5. Why are variables important in AI?

---

# Key Takeaways

✅ Variables store data.

✅ Python is dynamically typed.

✅ Use meaningful variable names.

✅ Always understand the data type you are working with.

✅ Variables are the foundation of Artificial Intelligence programs.

---

**Next Lesson:** Operators and Expressions
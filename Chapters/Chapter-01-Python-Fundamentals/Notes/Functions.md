# Functions

## Chapter 01: Python Fundamentals

**Course:** Python for Artificial Intelligence

**Author:** Muhammad Sohail Akhtar

**Repository:** Python-for-AI

---

# Introduction

As programs become larger and more complex, writing all code in a single file becomes difficult to understand, maintain, and debug. Python solves this problem through **functions**, which allow us to divide a program into smaller, reusable blocks.

Functions improve code organization, reduce duplication, and make programs easier to maintain. They are one of the most important concepts in Python programming and are heavily used in Artificial Intelligence, Machine Learning, Data Science, and software engineering.

---

# Learning Objectives

After completing this lesson, you will be able to:

- Understand the purpose of functions.
- Define and call functions.
- Pass arguments to functions.
- Return values from functions.
- Understand variable scope.
- Build reusable Python programs.
- Apply functions in AI applications.

---

# What is a Function?

A function is a reusable block of code that performs a specific task.

Instead of writing the same code repeatedly, we write it once inside a function and call it whenever needed.

Example:

```python
def greet():
    print("Welcome to Python for AI!")

greet()
```

Output:

```
Welcome to Python for AI!
```

---

# Why Do We Need Functions?

Without functions:

```python
print("Welcome")
print("Welcome")
print("Welcome")
```

With functions:

```python
def welcome():
    print("Welcome")

welcome()
welcome()
welcome()
```

Functions reduce repetition and improve readability.

---

# Defining a Function

Syntax:

```python
def function_name():
    statements
```

Example:

```python
def display_message():
    print("Learning Python")
```

---

# Calling a Function

A function executes only when it is called.

Example:

```python
display_message()
```

---

# Function Parameters

Parameters allow data to be passed into a function.

Example:

```python
def greet(name):
    print(f"Hello, {name}")

greet("Ali")
```

Output:

```
Hello, Ali
```

---

# Function Arguments

Arguments are the actual values passed to a function.

Example:

```python
def square(number):
    print(number * number)

square(5)
```

Here:

- Parameter → `number`
- Argument → `5`

---

# Returning Values

The `return` statement sends a value back to the caller.

Example:

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```
30
```

---

# Difference Between print() and return

### print()

Displays a value on the screen.

```python
def show():
    print(10)
```

---

### return

Returns a value for further use.

```python
def get_value():
    return 10

number = get_value()

print(number + 5)
```

Output:

```
15
```

---

# Types of Functions

## Built-in Functions

Provided by Python.

Examples:

```python
print()
len()
type()
input()
sum()
max()
min()
```

---

## User-defined Functions

Created by the programmer.

Example:

```python
def calculate_area(radius):
    return 3.1416 * radius ** 2
```

---

# Variable Scope

## Local Variables

Accessible only inside the function.

```python
def example():
    number = 10
    print(number)
```

---

## Global Variables

Accessible throughout the program.

```python
name = "Python"

def show():
    print(name)

show()
```

---

# Real-World Example

An online banking system may use separate functions for:

- Login
- Deposit
- Withdrawal
- Balance Inquiry
- Transaction History

Each function performs one specific task, making the system easier to maintain.

---

# Think Like an AI Engineer

Imagine you are developing a Machine Learning pipeline.

Instead of writing one large program, you create separate functions for:

- Loading data
- Cleaning data
- Feature engineering
- Training the model
- Evaluating the model
- Making predictions

Example:

```python
def load_data():
    pass

def preprocess_data():
    pass

def train_model():
    pass

def evaluate_model():
    pass
```

This modular design is used in professional AI projects.

---

# Common Mistakes

## Forgetting Parentheses

Incorrect:

```python
greet
```

Correct:

```python
greet()
```

---

## Forgetting return

Incorrect:

```python
def add(a, b):
    a + b
```

Correct:

```python
def add(a, b):
    return a + b
```

---

## Incorrect Indentation

Incorrect:

```python
def hello():
print("Hello")
```

Correct:

```python
def hello():
    print("Hello")
```

---

# Best Practices

- Give functions meaningful names.
- Each function should perform one task.
- Avoid writing very long functions.
- Use parameters instead of global variables when possible.
- Write reusable code.

---

# AI Applications

Functions are used extensively in:

- Data preprocessing
- Machine Learning model training
- Model evaluation
- Feature extraction
- Neural network implementation
- Natural Language Processing
- Computer Vision
- Reinforcement Learning

Example:

```python
def calculate_accuracy(correct, total):
    return (correct / total) * 100

accuracy = calculate_accuracy(95, 100)

print(f"Accuracy: {accuracy}%")
```

---

# Summary

In this lesson, you learned:

- Functions
- Function Definition
- Function Calls
- Parameters
- Arguments
- Return Statement
- Variable Scope
- Built-in Functions
- User-defined Functions
- AI Applications

---

# Interview Questions

1. What is a function?
2. Why are functions important?
3. What is the difference between parameters and arguments?
4. What is the difference between `print()` and `return`?
5. What is the difference between local and global variables?
6. How are functions used in Machine Learning libraries?

---

# Key Takeaways

✅ Functions make programs modular and reusable.

✅ Parameters receive data; arguments supply data.

✅ `return` sends values back to the caller.

✅ Good functions perform one specific task.

✅ Professional AI systems consist of hundreds or thousands of reusable functions.

---

**Next Lesson:** Strings
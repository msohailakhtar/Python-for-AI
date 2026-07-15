# Solution 06 – Functions

## Chapter 01: Python Fundamentals

**Course:** Python for Artificial Intelligence

**Author:** Muhammad Sohail Akhtar

**Repository:** Python-for-AI

---

# Learning Objectives

After studying this solution, you should be able to:

- Define and call functions.
- Use parameters and arguments.
- Return values from functions.
- Differentiate between local and global variables.
- Write reusable and modular Python programs.
- Understand the importance of functions in Artificial Intelligence and Machine Learning.

---

# Assignment Solutions

## Question 1

Write a function that adds two numbers.

### Solution

```python
def add_numbers(num1, num2):
    return num1 + num2

result = add_numbers(10, 20)

print("Sum =", result)
```

---

## Question 2

Write a function to calculate the area of a circle.

### Solution

```python
import math

def calculate_area(radius):
    return math.pi * radius ** 2

area = calculate_area(7)

print("Area =", area)
```

---

## Question 3

Write a function that determines the grade of a student.

### Solution

```python
def student_grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 80:
        return "B"

    elif marks >= 70:
        return "C"

    elif marks >= 60:
        return "D"

    else:
        return "F"

print(student_grade(85))
```

---

## Question 4

Write a function that checks whether a number is even or odd.

### Solution

```python
def check_even_odd(number):

    if number % 2 == 0:
        return "Even"

    return "Odd"

print(check_even_odd(17))
```

---

## Question 5

Write a function that finds the maximum of three numbers.

### Solution

```python
def largest(a, b, c):
    return max(a, b, c)

print(largest(25, 18, 40))
```

---

# Quiz Solutions

## Part A – Multiple Choice Questions

| Question | Answer |
|----------|:------:|
| Q1 | C |
| Q2 | B |
| Q3 | A |
| Q4 | C |
| Q5 | B |
| Q6 | B |
| Q7 | C |
| Q8 | C |
| Q9 | B |
| Q10 | B |

---

## Part B – True / False

| Question | Answer |
|----------|:------:|
| 1 | True |
| 2 | False |
| 3 | True |
| 4 | True |
| 5 | False |

---

# Explanation of Important Concepts

## What is a Function?

A function is a reusable block of code designed to perform a specific task.

Example

```python
def greet():
    print("Welcome to Python!")
```

---

## Calling a Function

A function executes only when it is called.

```python
greet()
```

---

## Parameters

Parameters receive values inside the function definition.

```python
def square(number):
    return number * number
```

Here, `number` is a parameter.

---

## Arguments

Arguments are the actual values passed to a function.

```python
square(5)
```

Here, `5` is an argument.

---

## Return Statement

The `return` statement sends a value back to the caller.

```python
def multiply(a, b):
    return a * b
```

---

## Local Variables

A local variable exists only inside the function.

```python
def demo():
    x = 10
```

`x` cannot be accessed outside the function.

---

## Global Variables

A global variable is defined outside all functions.

```python
message = "Hello"

def display():
    print(message)
```

The variable `message` is accessible throughout the program.

---

# AI Connection

Functions make AI programs modular and easier to maintain.

Typical Machine Learning projects contain functions such as:

```python
load_data()

preprocess_data()

train_model()

evaluate_model()

predict()

save_model()
```

Benefits:

- Code reuse
- Better organization
- Easier debugging
- Improved collaboration
- Easier testing
- Scalable AI systems

---

# Common Mistakes

## Mistake 1

Forgetting to call a function.

❌ Incorrect

```python
def greet():
    print("Hello")
```

Nothing happens.

✅ Correct

```python
greet()
```

---

## Mistake 2

Forgetting the `return` statement.

❌ Incorrect

```python
def add(a, b):
    a + b
```

✅ Correct

```python
def add(a, b):
    return a + b
```

---

## Mistake 3

Confusing parameters with arguments.

```python
def add(x, y):
```

`x` and `y` are parameters.

```python
add(5, 10)
```

`5` and `10` are arguments.

---

# Interview Questions

### Q1

What is a function?

---

### Q2

Why do we use functions?

---

### Q3

Differentiate between parameters and arguments.

---

### Q4

Explain the purpose of the `return` statement.

---

### Q5

How are functions used in Machine Learning?

---

# Practice Challenge

Create a Python program that defines the following functions:

- calculate_sum()
- calculate_average()
- find_maximum()
- check_pass_fail()
- display_student_information()

Call each function from the main program and display the results.

---

# Summary

In this lesson, you learned:

- Defining functions
- Calling functions
- Parameters
- Arguments
- Return values
- Local variables
- Global variables

Functions are one of the most important concepts in programming. They make code reusable, organized, and maintainable. In Artificial Intelligence, functions help build modular systems for data processing, model training, prediction, evaluation, and deployment.

---

**End of Solution 06**
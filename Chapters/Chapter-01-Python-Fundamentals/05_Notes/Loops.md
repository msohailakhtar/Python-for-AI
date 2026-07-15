# Loops

## Chapter 01: Python Fundamentals

**Course:** Python for Artificial Intelligence

**Author:** Muhammad Sohail Akhtar

**Repository:** Python-for-AI

---

# Introduction

Programming often requires repeating the same task multiple times. Writing the same code repeatedly is inefficient and difficult to maintain. Python solves this problem using **loops**, which allow a block of code to execute repeatedly until a condition is satisfied.

Loops are widely used in Artificial Intelligence, Machine Learning, Data Science, automation, simulations, and game development. Whether processing millions of records or training a neural network over hundreds of epochs, loops play a central role.

---

# Learning Objectives

After completing this lesson, you will be able to:

- Understand the purpose of loops.
- Use `for` loops.
- Use `while` loops.
- Apply nested loops.
- Control loops using `break`, `continue`, and `pass`.
- Solve repetitive computational problems.
- Understand the role of loops in AI applications.

---

# Why Do We Need Loops?

Without loops:

```python
print("Welcome")
print("Welcome")
print("Welcome")
print("Welcome")
print("Welcome")
```

With a loop:

```python
for i in range(5):
    print("Welcome")
```

Loops reduce code duplication and improve readability.

---

# Types of Loops in Python

Python provides two primary looping structures:

- `for` loop
- `while` loop

---

# The for Loop

A `for` loop is used when the number of iterations is known or when iterating over a sequence.

Syntax:

```python
for variable in sequence:
    statements
```

Example:

```python
for number in range(1, 6):
    print(number)
```

Output:

```
1
2
3
4
5
```

---

# The range() Function

The `range()` function generates a sequence of numbers.

Examples:

```python
range(5)
```

Output:

```
0 1 2 3 4
```

```python
range(1, 6)
```

Output:

```
1 2 3 4 5
```

```python
range(2, 11, 2)
```

Output:

```
2 4 6 8 10
```

---

# The while Loop

A `while` loop executes as long as a condition remains true.

Syntax:

```python
while condition:
    statements
```

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

# Infinite Loops

A loop that never ends is called an infinite loop.

Example:

```python
while True:
    print("Running...")
```

Always provide a condition to stop the loop unless continuous execution is intended.

---

# Loop Control Statements

## break

Terminates the loop immediately.

```python
for number in range(10):

    if number == 5:
        break

    print(number)
```

Output:

```
0
1
2
3
4
```

---

## continue

Skips the current iteration.

```python
for number in range(6):

    if number == 3:
        continue

    print(number)
```

Output:

```
0
1
2
4
5
```

---

## pass

Acts as a placeholder when no action is required.

```python
for number in range(5):

    if number == 2:
        pass

    print(number)
```

---

# Nested Loops

A loop inside another loop is called a nested loop.

Example:

```python
for row in range(3):

    for column in range(3):
        print("*", end=" ")

    print()
```

Output:

```
* * *
* * *
* * *
```

---

# Looping Through Strings

Example:

```python
text = "Python"

for character in text:
    print(character)
```

---

# Looping Through Lists

Example:

```python
marks = [85, 90, 78, 95]

for mark in marks:
    print(mark)
```

---

# Real-World Example

A bank calculates monthly interest for thousands of customer accounts.

Instead of writing code for every customer individually, a loop processes every account automatically.

---

# Think Like an AI Engineer

Suppose you are training a Machine Learning model.

The model is trained for **100 epochs**.

```python
for epoch in range(1, 101):

    print(f"Epoch {epoch} Completed")
```

Every epoch improves the model by updating its parameters based on the training data.

---

# Common Mistakes

## Forgetting the Colon

Incorrect:

```python
for i in range(5)
```

Correct:

```python
for i in range(5):
```

---

## Forgetting to Update the Counter

Incorrect:

```python
count = 1

while count <= 5:
    print(count)
```

This creates an infinite loop.

Correct:

```python
count += 1
```

---

## Incorrect Indentation

Incorrect:

```python
for i in range(5):
print(i)
```

Correct:

```python
for i in range(5):
    print(i)
```

---

# Best Practices

- Use `for` loops when the number of iterations is known.
- Use `while` loops for condition-based repetition.
- Avoid unnecessary nested loops.
- Use meaningful loop variable names.
- Ensure `while` loops have a termination condition.

---

# AI Applications

Loops are used extensively in:

- Machine Learning model training
- Deep Learning epochs
- Dataset preprocessing
- Data augmentation
- Reinforcement Learning episodes
- Image processing
- Natural Language Processing
- Simulation and optimization algorithms

Example:

```python
epochs = 10

for epoch in range(1, epochs + 1):

    print(f"Training Epoch {epoch}")
```

---

# Summary

In this lesson, you learned:

- for Loop
- while Loop
- range() Function
- Nested Loops
- break
- continue
- pass
- Infinite Loops
- AI Applications

---

# Interview Questions

1. What is a loop?
2. What is the difference between a `for` loop and a `while` loop?
3. What is the purpose of the `range()` function?
4. Explain the difference between `break` and `continue`.
5. How are loops used in Machine Learning?

---

# Key Takeaways

✅ Loops eliminate repetitive code.

✅ `for` loops are ideal for known iterations.

✅ `while` loops depend on conditions.

✅ `break`, `continue`, and `pass` provide loop control.

✅ Loops are essential for AI model training, dataset processing, and automation.

---

**Next Lesson:** Functions
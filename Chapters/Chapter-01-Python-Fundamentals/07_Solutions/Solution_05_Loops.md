# Solution 05 – Loops

## Chapter 01: Python Fundamentals

**Course:** Python for Artificial Intelligence

**Author:** Muhammad Sohail Akhtar

**Repository:** Python-for-AI

---

# Learning Objectives

After studying this solution, you should be able to:

- Understand the purpose of loops.
- Use `for` and `while` loops effectively.
- Apply the `range()` function.
- Control loop execution using `break`, `continue`, and `pass`.
- Create nested loops.
- Understand the importance of loops in Artificial Intelligence and Machine Learning.

---

# Assignment Solutions

## Question 1

Print the numbers from 1 to 20 using a `for` loop.

### Solution

```python
for number in range(1, 21):
    print(number)
```

---

## Question 2

Print the multiplication table of any number entered by the user.

### Solution

```python
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} × {i} = {number * i}")
```

---

## Question 3

Calculate the sum of the first 100 natural numbers.

### Solution

```python
total = 0

for number in range(1, 101):
    total += number

print("Sum =", total)
```

---

## Question 4

Print all even numbers from 1 to 50.

### Solution

```python
for number in range(2, 51, 2):
    print(number)
```

---

## Question 5

Print the following pattern.

```
*
**
***
****
*****
```

### Solution

```python
for i in range(1, 6):
    print("*" * i)
```

---

# Quiz Solutions

## Part A – Multiple Choice Questions

| Question | Answer |
|----------|:------:|
| Q1 | B |
| Q2 | C |
| Q3 | B |
| Q4 | C |
| Q5 | B |
| Q6 | C |
| Q7 | A |
| Q8 | B |
| Q9 | B |
| Q10 | B |

---

## Part B – True / False

| Question | Answer |
|----------|:------:|
| 1 | True |
| 2 | False |
| 3 | False |
| 4 | True |
| 5 | True |

---

# Explanation of Important Concepts

## The `for` Loop

A `for` loop is used when the number of iterations is known.

Example:

```python
for i in range(5):
    print(i)
```

Output

```
0
1
2
3
4
```

---

## The `while` Loop

A `while` loop continues executing as long as the condition remains `True`.

Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## The `range()` Function

The `range()` function generates a sequence of numbers.

Examples

```python
range(5)
```

Produces

```
0 1 2 3 4
```

```python
range(1,11)
```

Produces

```
1 2 3 ... 10
```

```python
range(2,21,2)
```

Produces

```
2 4 6 ... 20
```

---

## The `break` Statement

Stops the loop immediately.

Example

```python
for i in range(10):

    if i == 5:
        break

    print(i)
```

Output

```
0
1
2
3
4
```

---

## The `continue` Statement

Skips the current iteration.

Example

```python
for i in range(6):

    if i == 3:
        continue

    print(i)
```

Output

```
0
1
2
4
5
```

---

## The `pass` Statement

Acts as a placeholder.

Example

```python
for i in range(5):

    if i == 3:
        pass

    print(i)
```

---

## Nested Loops

A loop inside another loop.

Example

```python
for row in range(3):

    for column in range(3):
        print("*", end=" ")

    print()
```

Output

```
* * *
* * *
* * *
```

---

# AI Connection

Loops are one of the most important concepts in Artificial Intelligence.

They are used for:

- Training Machine Learning models over multiple epochs.
- Processing large datasets.
- Reading thousands of images.
- Making predictions for many samples.
- Iterating through neural network layers.
- Running optimization algorithms.
- Reinforcement Learning episodes.

Without loops, AI systems would only process one data sample at a time.

---

# Common Mistakes

## Mistake 1

Infinite `while` loop.

❌ Incorrect

```python
count = 1

while count <= 5:
    print(count)
```

The value of `count` never changes.

✅ Correct

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## Mistake 2

Incorrect indentation.

❌ Incorrect

```python
for i in range(5):
print(i)
```

✅ Correct

```python
for i in range(5):
    print(i)
```

---

## Mistake 3

Using `break` instead of `continue`.

Remember:

- `break` stops the loop.
- `continue` skips one iteration.

---

# Interview Questions

### Q1

What is the difference between a `for` loop and a `while` loop?

---

### Q2

What is the purpose of the `range()` function?

---

### Q3

Differentiate between `break` and `continue`.

---

### Q4

What is a nested loop?

---

### Q5

How are loops used in Artificial Intelligence?

---

# Practice Challenge

Create a Python program that:

- Accepts a positive integer `n` from the user.
- Prints the factorial of `n`.
- Uses a `for` loop.
- Displays each multiplication step before printing the final result.

Example

```
Enter n: 5

1 × 2 × 3 × 4 × 5 = 120
```

---

# Summary

In this lesson, you learned:

- `for` loops
- `while` loops
- `range()`
- `break`
- `continue`
- `pass`
- Nested loops

Loops are fundamental in programming because they automate repetitive tasks. In Artificial Intelligence and Machine Learning, loops are used to process data, train models, optimize algorithms, and perform repeated computations efficiently.

---

**End of Solution 05**
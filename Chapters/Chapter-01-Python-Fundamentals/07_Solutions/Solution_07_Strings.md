# Solution 07 – Strings

## Chapter 01: Python Fundamentals

**Course:** Python for Artificial Intelligence

**Author:** Muhammad Sohail Akhtar

**Repository:** Python-for-AI

---

# Learning Objectives

After studying this solution, you should be able to:

- Create and manipulate strings.
- Access characters using indexing.
- Extract substrings using slicing.
- Apply commonly used string methods.
- Format strings using f-strings.
- Understand the importance of strings in Artificial Intelligence and Natural Language Processing (NLP).

---

# Assignment Solutions

## Question 1

Write a program that displays a string in different formats.

### Solution

```python
name = input("Enter your full name: ")

print("Original :", name)
print("Upper    :", name.upper())
print("Lower    :", name.lower())
print("Title    :", name.title())
```

---

## Question 2

Count the number of vowels in a sentence.

### Solution

```python
sentence = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
count = 0

for character in sentence:
    if character in vowels:
        count += 1

print("Total Vowels:", count)
```

---

## Question 3

Display information about a sentence.

### Solution

```python
sentence = input("Enter a sentence: ")

words = sentence.split()

print("Characters :", len(sentence))
print("Words      :", len(words))
print("First Word :", words[0])
print("Last Word  :", words[-1])
```

---

## Question 4

Reverse a string.

### Solution

```python
text = input("Enter a string: ")

print("Reversed String:", text[::-1])
```

---

## Question 5

Check whether a word is a palindrome.

### Solution

```python
word = input("Enter a word: ")

if word.lower() == word.lower()[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
```

---

# Quiz Solutions

## Part A – Multiple Choice Questions

| Question | Answer |
|----------|:------:|
| Q1 | B |
| Q2 | B |
| Q3 | A |
| Q4 | A |
| Q5 | C |
| Q6 | B |
| Q7 | B |
| Q8 | B |
| Q9 | C |
| Q10 | C |

---

## Part B – True / False

| Question | Answer |
|----------|:------:|
| 1 | True |
| 2 | True |
| 3 | True |
| 4 | True |
| 5 | True |

---

# Explanation of Important Concepts

## What is a String?

A string is a sequence of characters enclosed in single or double quotation marks.

Example

```python
language = "Python"
```

---

## Indexing

Indexing accesses a single character from a string.

```python
text = "Python"

print(text[0])
```

Output

```
P
```

Negative indexing starts from the end.

```python
print(text[-1])
```

Output

```
n
```

---

## Slicing

Slicing extracts a portion of a string.

```python
text = "Python"

print(text[1:4])
```

Output

```
yth
```

---

## String Methods

### Convert to Uppercase

```python
text.upper()
```

---

### Convert to Lowercase

```python
text.lower()
```

---

### Title Case

```python
text.title()
```

---

### Remove Extra Spaces

```python
text.strip()
```

---

### Replace Text

```python
text.replace("Python", "AI")
```

---

### Split String

```python
text.split()
```

Returns a list of words.

---

### Find Text

```python
text.find("AI")
```

Returns the position of the substring.

---

## String Formatting

Modern Python recommends using **f-strings**.

Example

```python
name = "Ali"
age = 22

print(f"{name} is {age} years old.")
```

---

# AI Connection

Strings are one of the most important data types in Artificial Intelligence.

Applications include:

- Natural Language Processing (NLP)
- Chatbots
- Sentiment Analysis
- Text Classification
- Machine Translation
- Speech Recognition
- Question Answering Systems
- Large Language Models (LLMs)

Before text is processed by AI models, it is often cleaned using methods such as:

```python
lower()
strip()
replace()
split()
```

These preprocessing steps improve the quality and consistency of textual data.

---

# Common Mistakes

## Mistake 1

Using an invalid index.

❌ Incorrect

```python
text = "AI"

print(text[5])
```

This causes an `IndexError`.

---

## Mistake 2

Forgetting that strings are immutable.

❌ Incorrect

```python
text = "Python"

text[0] = "J"
```

Correct

```python
text = "J" + text[1:]
```

---

## Mistake 3

Using `+` with strings and integers.

❌ Incorrect

```python
age = 20

print("Age: " + age)
```

Correct

```python
print("Age:", age)
```

or

```python
print(f"Age: {age}")
```

---

# Interview Questions

### Q1

What is a string?

---

### Q2

Differentiate between indexing and slicing.

---

### Q3

What is the difference between `split()` and `strip()`?

---

### Q4

Why are f-strings preferred over older formatting methods?

---

### Q5

How are strings used in Natural Language Processing?

---

# Practice Challenge

Create a Python program that asks the user to enter a paragraph and displays:

- Total characters
- Total words
- Total vowels
- Total consonants
- Number of spaces
- Reverse of the paragraph
- Whether the first word is a palindrome

---

# Summary

In this lesson, you learned:

- String creation
- Indexing
- Slicing
- String methods
- String formatting
- String preprocessing
- String applications in Artificial Intelligence

Strings are the foundation of text processing. They play a central role in Python programming and are essential for Natural Language Processing, chatbots, search engines, recommendation systems, and modern AI applications.

---

**End of Solution 07**
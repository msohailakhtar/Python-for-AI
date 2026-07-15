"""
=========================================================
                PYTHON FOR AI

Mini Project 05

AI Text Analyzer

Author: Muhammad Sohail Akhtar
Repository: Python-for-AI
=========================================================
"""


# =====================================================
# Function 1 : Read Paragraph
# =====================================================

def get_paragraph():

    print("\nEnter a paragraph below:\n")

    paragraph = input("> ")

    return paragraph


# =====================================================
# Function 2 : Character Count
# =====================================================

def count_characters(text):

    return len(text)


# =====================================================
# Function 3 : Word Count
# =====================================================

def count_words(text):

    return len(text.split())


# =====================================================
# Function 4 : Sentence Count
# =====================================================

def count_sentences(text):

    sentences = text.count(".")
    sentences += text.count("!")
    sentences += text.count("?")

    return sentences


# =====================================================
# Function 5 : Count Vowels
# =====================================================

def count_vowels(text):

    vowels = "aeiouAEIOU"

    count = 0

    for ch in text:

        if ch in vowels:
            count += 1

    return count


# =====================================================
# Function 6 : Count Consonants
# =====================================================

def count_consonants(text):

    vowels = "aeiouAEIOU"

    count = 0

    for ch in text:

        if ch.isalpha() and ch not in vowels:
            count += 1

    return count


# =====================================================
# Function 7 : Uppercase
# =====================================================

def convert_upper(text):

    return text.upper()


# =====================================================
# Function 8 : Lowercase
# =====================================================

def convert_lower(text):

    return text.lower()


# =====================================================
# Function 9 : Keyword Search
# =====================================================

def keyword_search(text):

    keyword = input("\nEnter keyword to search: ")

    occurrences = text.lower().count(keyword.lower())

    return keyword, occurrences


# =====================================================
# Function 10 : Longest Word
# =====================================================

def longest_word(text):

    words = text.split()

    longest = ""

    for word in words:

        cleaned = word.strip(".,!?;:")

        if len(cleaned) > len(longest):
            longest = cleaned

    return longest


# =====================================================
# Function 11 : Character Frequency
# =====================================================

def character_frequency(text):

    frequency = {}

    for char in text:

        if char != " ":

            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

    return frequency


# =====================================================
# Function 12 : Display Report
# =====================================================

def display_report(text):

    print("\n")
    print("=" * 65)
    print("               AI TEXT ANALYSIS REPORT")
    print("=" * 65)

    print(f"Characters : {count_characters(text)}")
    print(f"Words      : {count_words(text)}")
    print(f"Sentences  : {count_sentences(text)}")
    print(f"Vowels     : {count_vowels(text)}")
    print(f"Consonants : {count_consonants(text)}")

    keyword, total = keyword_search(text)

    print(f"\nKeyword '{keyword}' appears {total} time(s).")

    print(f"\nLongest Word : {longest_word(text)}")

    print("\nUPPERCASE")
    print(convert_upper(text))

    print("\nLOWERCASE")
    print(convert_lower(text))

    print("\nCharacter Frequency")

    frequency = character_frequency(text)

    for key, value in sorted(frequency.items()):
        print(f"{key} : {value}")

    print("=" * 65)


# =====================================================
# Main Function
# =====================================================

def main():

    print("=" * 65)
    print("                AI TEXT ANALYZER")
    print("=" * 65)

    paragraph = get_paragraph()

    display_report(paragraph)


# =====================================================
# Program Starts Here
# =====================================================

if __name__ == "__main__":
    main()
"""
=========================================================
            PYTHON FOR AI

Mini Project 03

Multiplication Table Generator

Author: Muhammad Sohail Akhtar
Repository: Python-for-AI
=========================================================
"""

print("=" * 65)
print("          MULTIPLICATION TABLE GENERATOR")
print("=" * 65)

while True:

    print("\nChoose an option")
    print("1. Generate Multiplication Table")
    print("2. Exit")

    choice = input("\nEnter your choice (1 or 2): ")

    if choice == "1":

        number = int(input("\nEnter a number: "))

        print("\n" + "=" * 40)
        print(f"Multiplication Table of {number}")
        print("=" * 40)

        for i in range(1, 11):
            print(f"{number:2} x {i:2} = {number * i}")

        print("=" * 40)

    elif choice == "2":

        print("\nThank you for using Python for AI!")
        print("Goodbye 👋")
        break

    else:

        print("\nInvalid Choice.")
        print("Please enter 1 or 2.")
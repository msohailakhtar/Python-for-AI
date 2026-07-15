"""
=========================================================
                PYTHON FOR AI

Mini Project 04

Student Result Analyzer

Author: Muhammad Sohail Akhtar
Repository: Python-for-AI
=========================================================
"""


# =====================================================
# Function 1: Student Information
# =====================================================

def get_student_information():

    print("\nEnter Student Information")

    name = input("Student Name : ")
    roll = input("Roll Number  : ")

    return name, roll


# =====================================================
# Function 2: Input Marks
# =====================================================

def get_marks():

    print("\nEnter Subject Marks")

    math = float(input("Mathematics : "))
    python = float(input("Python      : "))
    ai = float(input("Artificial Intelligence : "))

    return math, python, ai


# =====================================================
# Function 3: Total Marks
# =====================================================

def calculate_total(math, python, ai):

    return math + python + ai


# =====================================================
# Function 4: Percentage
# =====================================================

def calculate_percentage(total):

    return (total / 300) * 100


# =====================================================
# Function 5: Grade
# =====================================================

def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    else:
        return "F"


# =====================================================
# Function 6: Pass or Fail
# =====================================================

def result_status(percentage):

    if percentage >= 50:
        return "PASS"

    else:
        return "FAIL"


# =====================================================
# Function 7: Display Result
# =====================================================

def display_result(name, roll, total, percentage, grade, status):

    print("\n" + "=" * 55)
    print("            STUDENT RESULT REPORT")
    print("=" * 55)

    print(f"Student Name : {name}")
    print(f"Roll Number  : {roll}")
    print(f"Total Marks  : {total:.2f} / 300")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Grade        : {grade}")
    print(f"Status       : {status}")

    print("=" * 55)


# =====================================================
# Main Program
# =====================================================

def main():

    print("=" * 60)
    print("         STUDENT RESULT ANALYZER")
    print("=" * 60)

    name, roll = get_student_information()

    math, python, ai = get_marks()

    total = calculate_total(math, python, ai)

    percentage = calculate_percentage(total)

    grade = calculate_grade(percentage)

    status = result_status(percentage)

    display_result(
        name,
        roll,
        total,
        percentage,
        grade,
        status
    )


# =====================================================
# Program Execution
# =====================================================

if __name__ == "__main__":
    main()
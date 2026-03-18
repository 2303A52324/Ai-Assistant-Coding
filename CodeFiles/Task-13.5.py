"""Lab 13: Code Refactoring – Improving Legacy Code with AI Suggestions
Lab Objectives:
•	Identify code smells and inefficiencies in legacy Python scripts.
•	Use AI-assisted coding tools to refactor for readability, maintainability, and performance.
•	Apply modern Python best practices while ensuring output correctness.
"""
"""Task Description #1 (Refactoring – Removing Code Duplication)
•	Task: Use AI to refactor a given Python script that contains multiple repeated code blocks.
•	Instructions:
o	Prompt AI to identify duplicate logic and replace it with functions or classes.
o	Ensure the refactored code maintains the same output.
o	Add docstrings to all functions.
•	Sample Legacy Code:
# Legacy script with repeated logic
print("Area of Rectangle:", 5 * 10)
print("Perimeter of Rectangle:", 2 * (5 + 10))

print("Area of Rectangle:", 7 * 12)
print("Perimeter of Rectangle:", 2 * (7 + 12))

print("Area of Rectangle:", 10 * 15)
print("Perimeter of Rectangle:", 2 * (10 + 15))
•	Expected Output:
o	Refactored code with a reusable function and no duplication.
o	Well documented code
"""

# def print_rectangle_metrics(width, height):
#     """Compute and print area and perimeter for a rectangle.
#     Args:
#         width (int | float): The width of the rectangle.
#         height (int | float): The height of the rectangle.
#     Prints:
#         Two lines:
#         - "Area of Rectangle: <area>"
#         - "Perimeter of Rectangle: <perimeter>"
#     """
#     area = width * height
#     perimeter = 2 * (width + height)
#     print("Area of Rectangle:", area)
#     print("Perimeter of Rectangle:", perimeter)
# if __name__ == "__main__":
#     print_rectangle_metrics(5, 10)
#     print()  # preserve spacing between blocks like original script
#     print_rectangle_metrics(7, 12)
#     print()
#     print_rectangle_metrics(10, 15)


"""Task Description #2 (Refactoring – Extracting Reusable Functions)
•	Task: Use AI to refactor a legacy script where multiple calculations are embedded directly inside the main code block.
•	Instructions:
o	Identify repeated or related logic and extract it into reusable functions.
o	Ensure the refactored code is modular, easy to read, and documented with docstrings.
•	Sample Legacy Code:
# Legacy script with inline repeated logic
price = 250
tax = price * 0.18
total = price + tax
print("Total Price:", total)
price = 500
tax = price * 0.18
total = price + tax
print("Total Price:", total)
•	Expected Output:
o	Code with a function calculate_total(price) that can be reused for multiple price inputs.
o	Well documented code
"""

# def calculate_total(price, tax_rate=0.18):
#     """Calculate the total price including tax.
#     Args:
#         price (int | float): The base price.
#         tax_rate (float): Tax rate as a decimal (default 0.18).
#     Returns:
#         float: Total price including tax.
#     """
#     tax = price * tax_rate
#     return price + tax
# if __name__ == "__main__":
#     print("Total Price:", calculate_total(250))
#     print("Total Price:", calculate_total(500))


"""Task Description #3: Refactoring Using Classes and Methods (Eliminating Redundant Conditional Logic)
Refactor a Python script that contains repeated if–elif–else grading logic by implementing a structured, object-oriented solution using a class and a method.
Problem Statement
The given script contains duplicated conditional statements used to assign grades based on student marks. This redundancy violates clean code principles and reduces maintainability.
You are required to refactor the script using a class-based design to improve modularity, reusability, and readability while preserving the original grading logic.
Mandatory Implementation Requirements
1.	Class Name: GradeCalculator
2.	Method Name: calculate_grade(self, marks)
3.	The method must:
o	Accept marks as a parameter.
o	Return the corresponding grade as a string.
o	The grading logic must strictly follow the conditions below:
	Marks ≥ 90 and ≤ 100 → "Grade A"
	Marks ≥ 80 → "Grade B"
	Marks ≥ 70 → "Grade C"
	Marks ≥ 40 → "Grade D"
	Marks ≥ 0 → "Fail"
      Note: Assume marks are within the valid range of 0 to 100.
4.	Include proper docstrings for:
o	The class
o	The method (with parameter and return descriptions)
5.	The method must be reusable and called multiple times without rewriting conditional logic.
• Given code:
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")
marks = 72
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")
Expected Output:
•	 Define a class named GradeCalculator.
•	Implement a method calculate_grade(self, marks) inside the class.
•	Create an object of the class.
•	Call the method for different student marks.
•	Print the returned grade values.
"""


# marks = 85
# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# else:
#     print("Grade C")
# marks = 72
# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# else:
#     print("Grade C")
#     class GradeCalculator:
#         """Calculate a letter grade from numeric marks (0-100)."""
#         def calculate_grade(self, marks):
#             """Return the grade for given marks.
#             Args:
#                 marks (int | float): Student marks between 0 and 100.
#             Returns:
#                 str: One of "Grade A", "Grade B", "Grade C", "Grade D", or "Fail".
#             """
#             if 90 <= marks <= 100:
#                 return "Grade A"
#             if marks >= 80:
#                 return "Grade B"
#             if marks >= 70:
#                 return "Grade C"
#             if marks >= 40:
#                 return "Grade D"
#             return "Fail"
#     if __name__ == "__main__":
#         grader = GradeCalculator()
#         print(grader.calculate_grade(85))
#         print(grader.calculate_grade(72))

"""Task Description #4 (Refactoring – Converting Procedural Code to Functions)
• Task: Use AI to refactor procedural input–processing logic into functions.
Instructions:
o Identify input, processing, and output sections.
o Convert each into a separate function.
o Improve code readability without changing behavior.
• Sample Legacy Code:
num = int(input("Enter number: "))
square = num * num
print("Square:", square)
• Expected Output:
o Modular code using functions like get_input(), calculate_square(), and display_result().
"""

# def get_input(prompt: str = "Enter number: ") -> int:
#     """Prompt the user and return the entered integer.
#     Args:
#         prompt: Prompt message shown to the user.
#     Returns:
#         The integer entered by the user.
#     """
#     return int(input(prompt))
# def calculate_square(num: int) -> int:
#     """Calculate and return the square of a number.
#     Args:
#         num: The number to square.
#     Returns:
#         The squared value.
#     """
#     return num * num
# def display_result(square: int) -> None:
#     """Display the computed square.
#     Args:
#         square: The squared value to print.
#     """
#     print("Square:", square)
# def main() -> None:
#     """Main program flow: get input, compute square, and display result."""
#     num = get_input()
#     square = calculate_square(num)
#     display_result(square)
# if __name__ == "__main__":
#     main()


"""Task 5 (Refactoring Procedural Code into OOP Design)
• Task: Use AI to refactor procedural code into a class-based design.
Focus Areas:
o Object-Oriented principles
o Encapsulation
Legacy Code:
salary = 50000
tax = salary * 0.2
net = salary - tax
print(net)
Expected Outcome:
o A class like EmployeeSalaryCalculator with methods and attributes.
"""

# salary = 50000
# tax = salary * 0.2
# net = salary - tax
# print(net)
# class EmployeeSalaryCalculator:
#     """Encapsulate salary and tax calculations for an employee."""
#     def __init__(self, salary: float, tax_rate: float = 0.2) -> None:
#         """Initialize calculator with salary and tax rate.
#         Args:
#             salary: Gross salary amount.
#             tax_rate: Tax rate as a decimal (default 0.2).
#         """
#         self._salary = float(salary)
#         self._tax_rate = float(tax_rate)
#     def set_salary(self, salary: float) -> None:
#         """Set a new gross salary."""
#         self._salary = float(salary)
#     def get_salary(self) -> float:
#         """Return the current gross salary."""
#         return self._salary
#     def calculate_tax(self) -> float:
#         """Return the tax amount for the current salary."""
#         return self._salary * self._tax_rate
#     def calculate_net(self) -> float:
#         """Return the net salary after deducting tax."""
#         return self._salary - self.calculate_tax()
# if __name__ == "__main__":
#     calculator = EmployeeSalaryCalculator(salary)
#     print(calculator.calculate_net())



"""Task 6 (Optimizing Search Logic)
• Task: Refactor inefficient linear searches using appropriate data structures.
• Focus Areas:
o Time complexity
o Data structure choice
Legacy Code:
users = ["admin", "guest", "editor", "viewer"]
name = input("Enter username: ")
found = False
for u in users:
    if u == name:
        found = True
print("Access Granted" if found else "Access Denied")
Expected Outcome:
o Use of sets or dictionaries with complexity justification
"""

# def is_user_allowed(username: str, allowed_users) -> bool:
#     """Return True if username is in allowed_users.
#     allowed_users can be a list or set. Converting a list to a set costs O(n) once,
#     afterwards membership checks are O(1) on average.
#     """
#     if not isinstance(allowed_users, set):
#         allowed_users = set(allowed_users)  # O(n) one-time cost
#     return username in allowed_users  # O(1) average
# if __name__ == "__main__":
#     users = ["admin", "guest", "editor", "viewer"]
#     # Build set once to enable O(1) average membership checks for repeated lookups
#     users_set = set(users)  # O(n)
#     name = input("Enter username: ")
#     print("Access Granted" if is_user_allowed(name, users_set) else "Access Denied")


"""Task 7 – Refactoring the Library Management System
Problem Statement
You are provided with a poorly structured Library Management script that:
•	Contains repeated conditional logic
•	Does not use reusable functions
•	Lacks documentation
•	Uses print-based procedural execution
•	Does not follow modular programming principles
Your task is to refactor the code into a proper format 
1.	Create a module library.py with functions:
o	add_book(title, author, isbn)
o	remove_book(isbn)
o	search_book(isbn)
2.	Insert triple quotes under each function and let Copilot complete the docstrings.
3.	Generate documentation in the terminal.
4.	Export the documentation in HTML format.
5.	Open the file in a browser.
Given Code 
# Library Management System (Unstructured Version)
# This code needs refactoring into a proper module with documentation.
library_db = {}
# Adding first book
title = "Python Basics"
author = "John Doe"
isbn = "101"
if isbn not in library_db:
    library_db[isbn] = {"title": title, "author": author}
    print("Book added successfully.")
else:
    print("Book already exists.")
# Adding second book (duplicate logic)
title = "AI Fundamentals"
author = "Jane Smith"
isbn = "102"
if isbn not in library_db:
    library_db[isbn] = {"title": title, "author": author}
    print("Book added successfully.")
else:
    print("Book already exists.")
# Searching book (repeated logic structure)
isbn = "101"
if isbn in library_db:
    print("Book Found:", library_db[isbn])
else:
    print("Book not found.")
# Removing book (again repeated pattern)
isbn = "101"
if isbn in library_db:
    del library_db[isbn]
    print("Book removed successfully.")
else:
    print("Book not found.")
# Searching again
isbn = "101"
if isbn in library_db:
    print("Book Found:", library_db[isbn])
else:
    print("Book not found.")
"""


# import os
# import sys
# import importlib
# import pydoc
# import webbrowser

# library_db = {}
# # Adding first book
# title = "Python Basics"
# author = "John Doe"
# isbn = "101"
# if isbn not in library_db:
#     library_db[isbn] = {"title": title, "author": author}
#     print("Book added successfully.")
# else:
#     print("Book already exists.")
# # Adding second book (duplicate logic)
# title = "AI Fundamentals"
# author = "Jane Smith"
# isbn = "102"
# if isbn not in library_db:
#     library_db[isbn] = {"title": title, "author": author}
#     print("Book added successfully.")
# else:
#     print("Book already exists.")
# # Searching book (repeated logic structure)
# isbn = "101"
# if isbn in library_db:
#     print("Book Found:", library_db[isbn])
# else:
#     print("Book not found.")
# # Removing book (again repeated pattern)
# isbn = "101"
# if isbn in library_db:
#     del library_db[isbn]
#     print("Book removed successfully.")
# else:
#     print("Book not found.")
# # Searching again
# isbn = "101"
# if isbn in library_db:
#     print("Book Found:", library_db[isbn])
# else:
#     print("Book not found.")
#     # Create a proper library module, generate docs, and demonstrate usage.


#     module_code = '''"""
#     library.py - Simple Library Management Module

#     Provides functions to add, remove, and search books stored in an in-memory
#     dictionary keyed by ISBN.
#     """

#     library_db = {}

#     def add_book(title: str, author: str, isbn: str) -> bool:
#         """
#         Add a book to the library database if the ISBN does not already exist.

#         Args:
#             title (str): Book title.
#             author (str): Book author.
#             isbn (str): Unique book ISBN key.

#         Returns:
#             bool: True if the book was added, False if ISBN already exists.
#         """
#         if isbn in library_db:
#             return False
#         library_db[isbn] = {"title": title, "author": author}
#         return True

#     def remove_book(isbn: str) -> bool:
#         """
#         Remove a book from the library database by ISBN.

#         Args:
#             isbn (str): ISBN of the book to remove.

#         Returns:
#             bool: True if the book was removed, False if ISBN not found.
#         """
#         if isbn in library_db:
#             del library_db[isbn]
#             return True
#         return False

#     def search_book(isbn: str):
#         """
#         Search for a book by ISBN.

#         Args:
#             isbn (str): ISBN to search for.

#         Returns:
#             dict | None: Book dictionary with keys 'title' and 'author' if found,
#                          otherwise None.
#         """
#         return library_db.get(isbn)
#     '''

#     # Write the module file
#     with open("library.py", "w", encoding="utf-8") as f:
#         f.write(module_code)

#     # Ensure fresh import of the newly written module
#     if "library" in sys.modules:
#         del sys.modules["library"]
#     library = importlib.import_module("library")

#     # Demonstrate usage (replaces previous procedural blocks)
#     library.add_book("Python Basics", "John Doe", "101")
#     library.add_book("AI Fundamentals", "Jane Smith", "102")

#     print("Search 101 ->", library.search_book("101"))
#     print("Remove 101 ->", "Removed" if library.remove_book("101") else "Not found")
#     print("Search 101 ->", library.search_book("101"))

#     # Generate and print documentation to terminal
#     doc_text = pydoc.render_doc(library)
#     print("\n--- Library Module Documentation ---\n")
#     print(doc_text)

#     # Export documentation to HTML and open in browser
#     pydoc.writedoc("library")  # writes library.html in current directory
#     html_path = os.path.abspath("library.html")
#     print("\nDocumentation written to:", html_path)

#     try:
#         webbrowser.open(f"file://{html_path}")
#     except Exception:
#         pass

"""Task 8– Fibonacci Generator
Write a program to generate Fibonacci series up to n.
The initial code has:
•	Global variables.
•	Inefficient loop.
•	No functions or modularity.
Task for Students:
•	Refactor into a clean reusable function (generate_fibonacci).
•	Add docstrings and test cases.
•	Compare AI-refactored vs original.
Bad Code Version:
# fibonacci bad version
n=int(input("Enter limit: "))
a=0
b=1
print(a)
print(b)
for i in range(2,n):
 c=a+b
 print(c)
 a=b
 b=c
"""

# import time
# n=int(input("Enter limit: "))
# a=0
# b=1
# print(a)
# print(b)
# for i in range(2,n):
#  c=a+b
#  print(c)
#  a=b
#  b=c
# def generate_fibonacci(n: int):
#     """Generate Fibonacci sequence with n terms.

#     Args:
#         n (int): Number of terms to generate (n >= 0).

#     Returns:
#         list[int]: List of the first n Fibonacci numbers starting with 0, 1.
#     """
#     if n <= 0:
#         return []
#     if n == 1:
#         return [0]
#     seq = [0, 1]
#     for _ in range(2, n):
#         seq.append(seq[-1] + seq[-2])
#     return seq


# def legacy_style_fibonacci(n: int):
#     """Return Fibonacci sequence produced by a legacy iterative approach.

#     This function mirrors the procedural logic used in legacy code but returns
#     a list instead of printing values, enabling automated comparison.
#     """
#     if n <= 0:
#         return []
#     if n == 1:
#         return [0]
#     a, b = 0, 1
#     seq = [a, b]
#     for _ in range(2, n):
#         c = a + b
#         seq.append(c)
#         a, b = b, c
#     return seq


# # Minimal test suite and comparison
# if __name__ == "__main__":
#     # Functional tests
#     assert generate_fibonacci(0) == []
#     assert generate_fibonacci(1) == [0]
#     assert generate_fibonacci(2) == [0, 1]
#     assert generate_fibonacci(5) == [0, 1, 1, 2, 3]
#     # Compare against legacy-style implementation for several n
#     for n in (0, 1, 2, 5, 10, 20):
#         assert generate_fibonacci(n) == legacy_style_fibonacci(n)
#     print("All functional tests passed.")

#     # Simple performance comparison (informational)
#     for n in (1000, 5000):
#         t0 = time.perf_counter()
#         generate_fibonacci(n)
#         t1 = time.perf_counter()
#         legacy_style_fibonacci(n)
#         t2 = time.perf_counter()
#         print(f"n={n}: refactor {t1-t0:.6f}s, legacy {t2-t1:.6f}s")


"""Task 9 – Twin Primes Checker
Twin primes are pairs of primes that differ by 2 (e.g., 11 and 13, 17 and 19).
The initial code has:
•	Inefficient prime checking.
•	No functions.
•	Hardcoded inputs.
Task for Students:
•	Refactor into is_prime(n) and is_twin_prime(p1, p2).
•	Add docstrings and optimize.
•	Generate a list of twin primes in a given range using AI.
Bad Code Version:
# twin primes bad version
a=11
b=13
fa=0
for i in range(2,a):
 if a%i==0:
  fa=1
fb=0
for i in range(2,b):
 if b%i==0:
  fb=1
if fa==0 and fb==0 and abs(a-b)==2:
 print("Twin Primes")
else:
 print("Not Twin Primes")
"""


# import math
# from typing import List, Tuple
# a=11
# b=13
# fa=0
# for i in range(2,a):
#  if a%i==0:
#   fa=1
# fb=0
# for i in range(2,b):
#  if b%i==0:
#   fb=1
# if fa==0 and fb==0 and abs(a-b)==2:
#  print("Twin Primes")
# else:
#  print("Not Twin Primes")
# def is_prime(n: int) -> bool:
#     """Return True if n is a prime number (n >= 2). Uses trial division up to sqrt(n)."""
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     limit = math.isqrt(n)
#     for i in range(3, limit + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# def is_twin_prime(p1: int, p2: int) -> bool:
#     """Return True if p1 and p2 are twin primes (both prime and differ by 2)."""
#     return abs(p1 - p2) == 2 and is_prime(p1) and is_prime(p2)

# def twin_primes_in_range(start: int, end: int) -> List[Tuple[int, int]]:
#     """Generate a list of twin prime pairs (p, p+2) within the inclusive range [start, end]."""
#     if start > end:
#         start, end = end, start
#     pairs: List[Tuple[int, int]] = []
#     lo = max(2, start)
#     for p in range(lo, end - 1):
#         q = p + 2
#         if q > end:
#             break
#         if is_prime(p) and is_prime(q):
#             pairs.append((p, q))
#     return pairs

# if __name__ == "__main__":
#     # Examples / simple demonstration
#     print(is_prime(11))                # True
#     print(is_prime(13))                # True
#     print(is_twin_prime(11, 13))       # True
#     print(twin_primes_in_range(1, 100))  # [(3,5),(5,7),(11,13),...]


"""Task 10 – Refactoring the Chinese Zodiac Program
Objective
Refactor the given poorly structured Python script into a clean, modular, and reusable implementation.
The current program reads a year from the user and prints the corresponding Chinese Zodiac sign. However, the implementation contains repetitive conditional logic, lacks modular design, and does not follow clean coding principles.
Your task is to refactor the code to improve readability, maintainability, and structure.
Chinese Zodiac Cycle (Repeats Every 12 Years)
1.	Rat
2.	Ox
3.	Tiger
4.	Rabbit
5.	Dragon
6.	Snake
7.	Horse
8.	Goat (Sheep)
9.	Monkey
10.	Rooster
11.	Dog
12.	Pig
# Chinese Zodiac Program (Unstructured Version)
# This code needs refactoring.
year = int(input("Enter a year: "))
if year % 12 == 0:
    print("Monkey")
elif year % 12 == 1:
    print("Rooster")
elif year % 12 == 2:
    print("Dog")
elif year % 12 == 3:
    print("Pig")
elif year % 12 == 4:
    print("Rat")
elif year % 12 == 5:
    print("Ox")
elif year % 12 == 6:
    print("Tiger")
elif year % 12 == 7:
    print("Rabbit")
elif year % 12 == 8:
    print("Dragon")
elif year % 12 == 9:
    print("Snake")
elif year % 12 == 10:
    print("Horse")
elif year % 12 == 11:
    print("Goat")
You must:
1.	Create a reusable function: get_zodiac(year)
2.	Replace the if-elif chain with a cleaner structure (e.g., list or dictionary).
3.	Add proper docstrings.
4.	Separate input handling from logic.
5.	Improve readability and maintainability.
6.	Ensure output remains correct."""

# def get_zodiac(year: int) -> str:
#     """
#     Return the Chinese Zodiac sign for a given year.
#     The mapping is based on year % 12 and preserves the original script's mapping:
#     0: Monkey, 1: Rooster, 2: Dog, 3: Pig, 4: Rat, 5: Ox,
#     6: Tiger, 7: Rabbit, 8: Dragon, 9: Snake, 10: Horse, 11: Goat
#     Args:
#         year: The year (integer).

#     Returns:
#         The zodiac sign as a string.
#     """
#     zodiac_by_mod = [
#         "Monkey",   # 0
#         "Rooster",  # 1
#         "Dog",      # 2
#         "Pig",      # 3
#         "Rat",      # 4
#         "Ox",       # 5
#         "Tiger",    # 6
#         "Rabbit",   # 7
#         "Dragon",   # 8
#         "Snake",    # 9
#         "Horse",    # 10
#         "Goat",     # 11
#     ]
#     return zodiac_by_mod[year % 12]
# def main() -> None:
#     """Handle user input and print the corresponding Chinese Zodiac sign."""
#     try:
#         year = int(input("Enter a year: "))
#     except ValueError:
#         print("Invalid year.")
#         return
#     print(get_zodiac(year))
# if __name__ == "__main__":
#     main()

"""Task 11 – Refactoring the Harshad (Niven) Number Checker
Refactor the given poorly structured Python script into a clean, modular, and reusable implementation.
A Harshad (Niven) number is a number that is divisible by the sum of its digits.
For example:
•	18 → 1 + 8 = 9 → 18 ÷ 9 = 2 ✅ (Harshad Number)
•	19 → 1 + 9 = 10 → 19 ÷ 10 ≠ integer ❌ (Not Harshad)

Problem Statement
The current implementation:
•	Mixes logic and input handling
•	Uses redundant variables
•	Does not use reusable functions properly
•	Returns print statements instead of boolean values
•	Lacks documentation
You must refactor the code to follow clean coding principles.
# Harshad Number Checker (Unstructured Version)

num = int(input("Enter a number: "))

temp = num
sum_digits = 0

while temp > 0:
digit = temp % 10
    sum_digits = sum_digits + digit
    temp = temp // 10

if sum_digits != 0:
    if num % sum_digits == 0:
        print("True")
    else:
        print("False")
else:
    print("False")
You must:
1.	Create a reusable function: is_harshad(number)
2.	The function must:
o	Accept an integer parameter.
o	Return True if the number is divisible by the sum of its digits.
o	Return False otherwise.
3.	Separate user input from core logic.
4.	Add proper docstrings.
5.	Improve readability and maintainability.
6.	Ensure the program handles edge cases (e.g., 0, negative numbers).

"""


# def is_harshad(number: int) -> bool:
#     """Return True if number is a Harshad (Niven) number.
#     A Harshad number is divisible by the sum of its decimal digits.
#     Negative numbers use the absolute value for digit-sum calculation.
#     Zero returns False because the digit sum is 0 (division undefined).
#     """
#     digit_sum = sum(int(d) for d in str(abs(number)))
#     if digit_sum == 0:
#         return False
#     return number % digit_sum == 0
# def get_int_input(prompt: str = "Enter a number: "):
#     """Prompt the user for an integer; return the integer or None on invalid input."""
#     try:
#         return int(input(prompt))
#     except ValueError:
#         print("Invalid input.")
#         return None
# if __name__ == "__main__":
#     num = get_int_input()
#     if num is None:
#         exit(1)
#     print(is_harshad(num))


"""Task 12 – Refactoring the Factorial Trailing Zeros Program
Refactor the given poorly structured Python script into a clean, modular, and efficient implementation.
The program calculates the number of trailing zeros in n! (factorial of n).
Problem Statement
The current implementation:
•	Calculates the full factorial (inefficient for large n)
•	Mixes input handling with business logic
•	Uses print statements instead of return values
•	Lacks modular structure and documentation
You must refactor the code to improve efficiency, readability, and maintainability.
# Factorial Trailing Zeros (Unstructured Version)
n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i = i + 1
count = 0
while fact % 10 == 0:
    count = count + 1
    fact = fact // 10
print("Trailing zeros:", count)
You must:
1.	Create a reusable function: count_trailing_zeros(n)
2.	The function must:
o	Accept a non-negative integer n.
o	Return the number of trailing zeros in n!.
3.	Do NOT compute the full factorial.
4.	Use an optimized mathematical approach (count multiples of 5).
5.	Add proper docstrings.
6.	Separate user interaction from core logic.
7.	Handle edge cases (e.g., negative numbers, zero)."""


n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i = i + 1
count = 0
while fact % 10 == 0:
    count = count + 1
    fact = fact // 10
print("Trailing zeros:", count)
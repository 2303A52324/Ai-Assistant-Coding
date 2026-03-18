"""Lab 13: Code Refactoring – Improving Legacy Code with AI Suggestions
Lab Objectives:
•	Identify code smells and inefficiencies in legacy Python scripts.
•	Use AI-assisted coding tools to refactor for readability, maintainability, and performance.
•	Apply modern Python best practices while ensuring output correctness.
"""

"""Task Description #1 (Refactoring – Removing Global Variables)
• Task: Use AI to eliminate unnecessary global variables from the code.
• Instructions:
o Identify global variables used across functions.
o Refactor the code to pass values using function parameters.
o Improve modularity and testability.
• Sample Legacy Code:
rate = 0.1
def calculate_interest(amount):
    return amount * rate
print(calculate_interest(1000))
• Expected Output:
o Refactored version passing rate as a parameter or using a configuration structure.
"""
# def calculate_interest(amount, rate):
#     """Calculate interest using an explicit rate parameter."""
#     return amount * rate

# def format_currency(amount):
#     return f"${amount:,.2f}"

# def main(amount=1000, rate=0.1):
#     interest = calculate_interest(amount, rate)
#     print(format_currency(interest))

# if __name__ == "__main__":
#     main()
# rate = 0.1



"""Task Description #2 :  (Refactoring Deeply Nested Conditionals)
• Task: Use AI to refactor deeply nested if–elif–else logic into a cleaner structure.
• Focus Areas:
o Readability
o Logical simplification
o Maintainability
Legacy Code:
score = 78
if score >= 90:
    print("Excellent")
else:
    if score >= 75:
        print("Very Good")
    else:
        if score >= 60:
            print("Good")
        else:
            print("Needs Improvement")
Expected Outcome:
o Flattened logic using guard clauses or a mapping-based approach.
"""



# score = 78

# def evaluate_score(score):
#     thresholds = (
#         (90, "Excellent"),
#         (75, "Very Good"),
#         (60, "Good"),
#         (0, "Needs Improvement"),
#     )
#     for threshold, label in thresholds:
#         if score >= threshold:
#             return label

# print(evaluate_score(score))



"""Task 3 (Refactoring Repeated File Handling Code)
• Task: Use AI to refactor repeated file open/read/close logic.
• Focus Areas:
o DRY principle
o Context managers
o Function reuse
Legacy Code:
f = open("data1.txt")
print(f.read())
f.close()
f = open("data2.txt")
print(f.read())
f.close()
Expected Outcome:
o Reusable function using with open() and parameters.
"""


# def read_and_print(path):
#     with open(path, "r", encoding="utf-8") as f:
#         print(f.read())
# for filename in ("Task-10-3.py", "Task-1.py"):
#     read_and_print(filename)

"""Task 4 (Optimizing Search Logic)
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
o Use of sets or dictionaries with complexity justification.
"""

# def is_allowed_user(name: str, users_set: set) -> bool:
#     # Set membership is average O(1) vs O(n) for lists
#     return name in users_set

# if __name__ == "__main__":
#     USERS = {"admin", "guest", "editor", "viewer"}  # use a set for fast lookups
#     name = input("Enter username: ").strip()
#     print("Access Granted" if is_allowed_user(name, USERS) else "Access Denied")


"""Task 5 (Refactoring Procedural Code into OOP Design)
• Task: Use AI to refactor procedural code into a class-based design.
• Focus Areas:
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
#     def __init__(self, salary: float, tax_rate: float = 0.2):
#         self.salary = float(salary)
#         self.tax_rate = float(tax_rate)
#     def calculate_tax(self) -> float:
#         return self.salary * self.tax_rate
#     def net_salary(self) -> float:
#         return self.salary - self.calculate_tax()
#     def formatted_net(self) -> str:
#         return f"${self.net_salary():,.2f}"
# if __name__ == "__main__":
#     calc = EmployeeSalaryCalculator(50000)
#     print(calc.formatted_net())


"""Task 6 (Refactoring for Performance Optimization)
• Task: Use AI to refactor a performance-heavy loop handling large data.
• Focus Areas:
o Algorithmic optimization
o Use of built-in functions
Legacy Code:
total = 0
for i in range(1, 1000000):
    if i % 2 == 0:
        total += i
print(total)
Expected Outcome:
o Optimized logic using mathematical formulas or comprehensions, with time comparison.
"""
# import time
# N = 1_000_000
# def original_loop(n):
#     total = 0
#     for i in range(1, n):
#         if i % 2 == 0:
#             total += i
#     return total
# def comprehension(n):
#     return sum(range(2, n, 2))
# def formula(n):
#     m = (n - 1) // 2  # number of even terms in range(1, n)
#     return m * (m + 1)  # sum of first m evens = m(m+1)
# if __name__ == "__main__":
#     results = {}
#     for fn in (original_loop, comprehension, formula):
#         t0 = time.perf_counter()
#         results[fn.__name__] = (fn(N), time.perf_counter() - t0)
#     # print values and timings
#     for name, (val, dt) in results.items():
#         print(f"{name:15s}: {val} (t={dt:.6f}s)")
#     # sanity check
#     vals = {v for v, _ in results.values()}
#     assert len(vals) == 1, "Results differ!"

"""Task 7 (Removing Hidden Side Effects)
• Task: Refactor code that modifies shared mutable state.
• Focus Areas:
o Functional-style refactoring
o Predictability
Legacy Code:
data = []
def add_item(x):
    data.append(x)
add_item(10)
add_item(20)
print(data)

Expected Outcome:
o Refactored function returning values instead of mutating globals.
"""


# from typing import Iterable, List
# def add_item(data: Iterable[int], x: int) -> List[int]:
#     """Return a new list with x appended (no mutation)."""
#     return list(data) + [x]
# if __name__ == "__main__":
#     data = []
#     data = add_item(data, 10)
#     data = add_item(data, 20)
#     print(data)


"""Task 8 (Refactoring Complex Input Validation Logic)
• Task: Use AI to simplify and modularize complex validation rules.
• Focus Areas:
o Readability
o Testability
Legacy Code:
password = input("Enter password: ")
if len(password) >= 8:
    if any(c.isdigit() for c in password):
        if any(c.isupper() for c in password):
            print("Valid Password")
        else:
            print("Must contain uppercase")
    else:
        print("Must contain digit")
else:
    print("Password too short")
Expected Outcome:
o Separate validation functions with clear responsibility
"""


# def is_long_enough(password: str, min_len: int = 8) -> bool:
#     return len(password) >= min_len
# def has_digit(password: str) -> bool:
#     return any(c.isdigit() for c in password)
# def has_upper(password: str) -> bool:
#     return any(c.isupper() for c in password)
# def validate_password(password: str) -> tuple[bool, list[str]]:
#     checks = (
#         (is_long_enough, "Password too short (min 8)"),
#         (has_digit, "Must contain digit"),
#         (has_upper, "Must contain uppercase"),
#     )
#     errors = [msg for check, msg in checks if not check(password)]
#     return (not errors, errors)
# if __name__ == "__main__":
#     password = input("Enter password: ")
#     valid, errors = validate_password(password)
#     if valid:
#         print("Valid Password")
#     else:
#         for err in errors:
#             print(err)


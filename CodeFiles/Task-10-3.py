# 25/02/26

"""Problem Statement 1: AI-Assisted Bug Detection
Scenario: A junior developer wrote the following Python function to calculate factorials:

def factorial(n):
    result = 1
    for i in range(1, n):
        result = result * i
    return result
Instructions:
1.	Run the code and test it with factorial(5).
2.	Use an AI assistant to:
o	Identify the logical bug in the code.
o	Explain why the bug occurs (e.g., off-by-one error).
o	Provide a corrected version.
3.	Compare the AI’s corrected code with your own manual fix.
4.	Write a brief comparison: Did AI miss any edge cases (e.g., negative numbers, zero)?
Expected Output:
Corrected function should return 120 for factorial(5).
"""
"""Prompt: Compare the code anf fix the bug logic and give the correct logic 
code with brief description of what was the bug mistake"""
# def factorial(n):
#     result = 1
#     for i in range(1, n):
#         result = result * i
#     return result
# print("Before fixing Errors: ",factorial(5))  

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):  # Changed: n + 1 to include n
#         result = result * i
#     return result
# print("After fixing Errors: ",factorial(5))  # Output: 120




"""Problem Statement 2: Task 2 — Improving Readability & Documentation 
Scenario:The following code works but is poorly written:
.
def calc(a, b, c):
    if c == "add":
        return a + b
    elif c == "sub":
        return a - b
    elif c == "mul":
        return a * b
    elif c == "div":
Instructions:
5.	Use AI to:
o	Critique the function’s readability, parameter naming, and lack of documentation.
o	Rewrite the function with:
1.	Descriptive function and parameter names.
2.	A complete docstring (description, parameters, return value, examples).
3.	Exception handling for division by zero.
4.	Consideration of input validation.
6.	Compare the original and AI-improved versions.
7.	Test both with valid and invalid inputs (e.g., division by zero, non-string operation).
Expected Output:
A well-documented, robust, and readable function that handles errors gracefully.
"""

"""Prompt: Review the following Python function for readability and documentation:
    1. Critique its readability, parameter naming, and missing documentation.
2. Rewrite it with:
   - Descriptive function and parameter names
   - A complete docstring (description, parameters, return, examples)
   - Input validation
   - Exception handling (including division by zero)
3. Compare the original and improved versions.
4. Provide test cases for valid and invalid inputs."""

# def calc(a, b, c):
#     if c == "add":
#         return a + b
#     elif c == "sub":
#         return a - b
#     elif c == "mul":
#         return a * b
#     elif c == "div":
#         return a / b
# print("Before fixing Errors: ",calc(10, 3, "div"))  # Output: 2.0


# # ...existing code...
# def calculate(operand1: float, operand2: float, operation: str) -> float:
#     """
#     Perform a basic arithmetic operation on two numeric operands.

#     Parameters
#     ----------
#     operand1 : int | float
#         The first numeric operand.
#     operand2 : int | float
#         The second numeric operand.
#     operation : str
#         One of: "add", "sub", "mul", "div" (case-insensitive).

#     Returns
#     -------
#     float
#         The result of the operation.

#     Raises
#     ------
#     TypeError
#         If operands are not numbers or operation is not a string.
#     ValueError
#         If an unsupported operation is requested.
#     ZeroDivisionError
#         If division by zero is attempted.

#     Examples
#     --------
#     >>> calculate(2, 3, "add")
#     5
#     >>> calculate(10, 2, "div")
#     5.0
#     """
#     # Input validation
#     if not isinstance(operation, str):
#         raise TypeError("operation must be a string")
#     if not isinstance(operand1, (int, float)) or not isinstance(operand2, (int, float)):
#         raise TypeError("operands must be int or float")

#     op = operation.strip().lower()
#     if op == "add":
#         return operand1 + operand2
#     elif op == "sub":
#         return operand1 - operand2
#     elif op == "mul":
#         return operand1 * operand2
#     elif op == "div":
#         if operand2 == 0:
#             raise ZeroDivisionError("division by zero")
#         return operand1 / operand2
#     else:
#         raise ValueError(f"Unsupported operation: {operation!r}")
# # ...existing code...
# # Valid
# print(calculate(5, 3, "add"))   # 8
# print(calculate(5, 3, "sub"))   # 2
# print(calculate(5, 3, "mul"))   # 15
# print(calculate(6, 3, "div"))   # 2.0

# # Invalid
# try: calculate(1, 0, "div")
# except Exception as e: print(type(e).__name__, e)   # ZeroDivisionError

# try: calculate("a", 2, "add")
# except Exception as e: print(type(e).__name__, e)   # TypeError

# try: calculate(1, 2, "pow")
# except Exception as e: print(type(e).__name__, e)   # ValueError


"""Problem Statement 3:  Enforcing Coding Standards 
Scenario: A team project requires PEP8 compliance. A developer submits:
def Checkprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
Instructions:
8.	Verify the function works correctly for sample inputs.
9.	Use an AI tool (e.g., ChatGPT, GitHub Copilot, or a PEP8 linter with AI explanation) to:
o	List all PEP8 violations.
o	Refactor the code (function name, spacing, indentation, naming).
10.	Apply the AI-suggested changes and verify functionality is preserved.
11.	Write a short note on how automated AI reviews could streamline code reviews in large teams.
Expected Output:

"""

# def Checkprime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# print("Before Fixing:",Checkprime(12))  # True

# # ...existing code...
# def is_prime(n: int) -> bool:
#     """
#     Return True if n is a prime number, False otherwise.

#     Parameters
#     ----------
#     n : int
#         Integer to test for primality.

#     Returns
#     -------
#     bool
#         True if n is prime, False otherwise.
#     """
#     if not isinstance(n, int):
#         raise TypeError("n must be an integer")
#     if n < 2:
#         return False
#     if n % 2 == 0:
#         return n == 2
#     limit = int(n ** 0.5) + 1
#     for i in range(3, limit, 2):
#         if n % i == 0:
#             return False
#     return True

# if __name__ == "__main__":
#     # Sample checks
#     print("After Fixing:")
#     print(is_prime(2))   # True
#     print(is_prime(3))   # True
#     print(is_prime(4))   # False
#     print(is_prime(12))  # False
#     print(is_prime(17))  # True
#     print(is_prime(1))   # False
#     print(is_prime(-5))  # False
# # ...existing code...


"""Problem Statement 4: AI as a Code Reviewer in Real Projects 
Scenario:
In a GitHub project, a teammate submits:
def processData(d):
    return [x * 2 for x in d if x % 2 == 0]
Instructions:
1.	Manually review the function for:
o	Readability and naming.
o	Reusability and modularity.
o	Edge cases (non-list input, empty list, non-integer elements).
2.	Use AI to generate a code review covering:
a.	Better naming and function purpose clarity.
b.	Input validation and type hints.

c.	Suggestions for generalization (e.g., configurable multiplier).
3.	Refactor the function based on AI feedback.
4.	Write a short reflection on whether AI should be a standalone reviewer or an assistant.
Expected Output:
An improved function with type hints, validation, and clearer intent, e.g.:
from typing import List, Union

def double_even_numbers(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    return [num * 2 for num in numbers if isinstance(num, (int, float)) and num % 2 == 0]
"""

"""Prompt: Act as a professional Python code reviewer.
Review the following function:
def processData(d):
    return [x * 2 for x in d if x % 2 == 0]
1. Critique its readability, naming, reusability, and edge cases.
2. Suggest improvements including:
   - Better function and variable names
   - Clear purpose
   - Type hints
   - Input validation
   - Configurable multiplier instead of hardcoded 2
3. Refactor the function based on your suggestions.
4. Write a short reflection on whether AI should act as a standalone reviewer or an assistant."""


# def processData(d):
#     return [x * 2 for x in d if x % 2 == 0]
# print("Before Fixing:",processData([1, 2, 3, 4, 5]))  # [4, 8]

# # ...existing code...
# from typing import Iterable, Union, List
# Number = Union[int, float]
# def scale_even_numbers(data: Iterable[Number], multiplier: Number = 2) -> List[Number]:
#     """
#     Return a new list containing each even numeric element from `data` multiplied by `multiplier`.

#     Parameters
#     ----------
#     data : Iterable[int | float]
#         Iterable of numeric values.
#     multiplier : int | float, optional
#         Value to multiply each even element by (default 2).

#     Returns
#     -------
#     list[int | float]
#         List of scaled even numbers.

#     Raises
#     ------
#     TypeError
#         If `data` is not iterable or contains non-numeric elements.
#     """
#     try:
#         iterator = iter(data)
#     except TypeError:
#         raise TypeError("data must be an iterable of numbers")

#     result: List[Number] = []
#     for x in iterator:
#         if not isinstance(x, (int, float)) or isinstance(x, bool):
#             raise TypeError("all elements in data must be int or float")
#         if int(x) == x and x % 2 == 0:  # treat whole-number floats as integers for evenness
#             result.append(x * multiplier)
#     return result

# # Example usage
# if __name__ == "__main__":
#     print("After Fixing:", scale_even_numbers([1, 2, 3, 4, 5]))  # [4, 8]
# # ...existing code...


"""Problem Statement 5: — AI-Assisted Performance Optimization
Scenario: You are given a function that processes a list of integers, but it runs slowly on large datasets:
def sum_of_squares(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
    return total
Instructions:
1.	Test the function with a large list (e.g., range(1000000)).
2.	Use AI to:
o	Analyze time complexity.
o	Suggest performance improvements (e.g., using built-in functions, vectorization with NumPy if applicable).
o	Provide an optimized version.
3.	Compare execution time before and after optimization.
4.	Discuss trade-offs between readability and performance.
Expected Output:
An optimized function, such as:
def sum_of_squares_optimized(numbers):
    return sum(x * x for x in numbers)
"""

"""Prompt: Act as a Python performance optimization expert.
Given the function:
def sum_of_squares(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
    return total
1. Analyze its time complexity.
2. Suggest performance improvements (e.g., built-in functions or NumPy if appropriate).
3. Provide an optimized version.
4. Compare execution time before and after optimization using a large dataset (e.g., range(1000000)).
5. Briefly discuss trade-offs between readability and performance.
Expected Output:
An optimized function, such as:
def sum_of_squares_optimized(numbers):
    return sum(x * x for x in numbers)"""

# def sum_of_squares(numbers):
#     total = 0
#     for num in numbers:
#         total += num ** 2
#     return total
# print("Before Optimization:", sum_of_squares(range(1000000)))  # 333333166666500000


# # ...existing code...
# def sum_of_squares(numbers):
#     total = 0
#     for num in numbers:
#         total += num ** 2
#     return total

# def sum_of_squares_optimized(numbers):
#     """Use built-in sum with generator to reduce Python-level overhead."""
#     return sum(x * x for x in numbers)

# def sum_of_squares_numpy(numbers):
#     """NumPy vectorized version (best for large numeric arrays)."""
#     import numpy as np
#     arr = np.asarray(numbers)
#     return np.dot(arr, arr)  # equivalent to (arr**2).sum()

# if __name__ == "__main__":
#     import time
#     N = 1_000_000
#     data = range(N)

#     t0 = time.perf_counter()
#     _ = sum_of_squares(data)
#     t1 = time.perf_counter()
#     print("original:", t1 - t0, "s")

#     t0 = time.perf_counter()
#     _ = sum_of_squares_optimized(data)
#     t1 = time.perf_counter()
#     print("optimized (sum generator):", t1 - t0, "s")

#     try:
#         import numpy as np
#         arr = np.arange(N)
#         t0 = time.perf_counter()
#         _ = sum_of_squares_numpy(arr)
#         t1 = time.perf_counter()
#         print("numpy (vectorized):", t1 - t0, "s")
#     except Exception:
#         print("NumPy not available")
# # ...existing code...
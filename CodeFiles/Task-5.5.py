"""AI-ASSISTED CODING"""
"""30/1/26 """
"""Lab 5: Ethical Foundations – Responsible AI Coding Practices"""
"""Task-5.5"""


"""Task-1"""

"""2303A52324"""
# import math
# # Naïve method
# def is_prime_naive(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# # Optimized method (check up to sqrt(n))
# def is_prime_sqrt(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0:
#         return n == 2
#     r = math.isqrt(n)
#     for i in range(3, r + 1, 2):
#         if n % i == 0:
#             return False
#     return True
# # Example quick test
# if __name__ == "__main__":
#     test_values = [1, 2, 3, 4, 17, 18, 19, 97, 100, 101]
#     print("Naive results:", {v: is_prime_naive(v) for v in test_values})
#     print("Sqrt  results:", {v: is_prime_sqrt(v) for v in test_values})

# Naïve method
# Steps:
# 1. If n <= 1 it's not prime.
# 2. Try every divisor i from 2 to n-1.
# 3. If any i divides n evenly, n is composite; otherwise it's prime.
# Time complexity: O(n)

# Optimized method (check up to sqrt(n))
# Steps:
# 1. Handle n <= 1 (not prime) and small n (2,3).
# 2. If n is even and not 2, it's composite.
# 3. Compute r = floor(sqrt(n)) and test odd divisors 3..r.
# 4. If none divide n, it's prime.
# Time complexity: O(sqrt(n))    



"""Task-2"""

"""2303A52324"""
"""Recursive function to calculate Fibonacci numbers"""
# def fibonacci(n):
#     # Recursion is a programming technique where a function calls itself to solve smaller instances of the same problem.
#     # In this function, we will calculate the nth Fibonacci number using recursion.

#     # Base Cases:
#     # The first two Fibonacci numbers are defined as:
#     if n == 0:
#         return 0  # The 0th Fibonacci number is 0
#     elif n == 1:
#         return 1  # The 1st Fibonacci number is 1
#     # Recursive Case:
#     # For n greater than 1, the nth Fibonacci number is the sum of the (n-1)th and (n-2)th Fibonacci numbers.
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#         # Here, the function calls itself twice with smaller values (n-1 and n-2).
# # Example usage
# n = int(input("Enter a positive integer to find the nth Fibonacci number: "))
# fib_number = fibonacci(n)
# print(f"The {n}th Fibonacci number is: {fib_number}")



"""Task-3"""

"""2303A52324"""    
# def divide_numbers(a, b):
#     """Divide two numbers with error handling."""
#     try:
#         result = a / b
#     except ZeroDivisionError:
#         return "Error: Cannot divide by zero."
#     except NameError:
#         return "Error: One of the variables is not defined."
#     except ValueError:
#         return "Error: Invalid value provided."
#     except TypeError:
#         return "Error: Both inputs must be numbers."
#     except Exception as e:
#         return f"An unexpected error occurred: {e}"
#     else:
#         return result
# # Example usage
# print(divide_numbers(10, 2))  # Valid case
# print(divide_numbers(10, 0))  # Division by zero
# print(divide_numbers(10, 'a'))  # Invalid type
# # Value error example (not directly applicable in this context, but included for completeness)
# print(divide_numbers(10, -5))  # This will not raise ValueError but included for demonstration
# # Name error example
# print(divide_numbers(10, None))  # This will not raise NameError but included for demonstration
# # Explanation of error handling and validation
# explanation_errors = """
# | Exception Type        | Explanation                                      | Runtime Behavior Example               |
# |-----------------------|--------------------------------------------------|---------------------------------------|
# | ZeroDivisionError     | Raised when attempting to divide by zero.        | divide_numbers(10, 0) returns "Error: Cannot divide by zero." |
# | TypeError             | Raised when inputs are of incorrect type.        | divide_numbers(10, 'a') returns "Error: Both inputs must be numbers." |
# | NameError             | Raised when a variable is not defined.           | divide_numbers(10, None) returns "Error: One of the variables is not defined." |
# | ValueError            | Raised when an invalid value is passed.          | divide_numbers(10, -5) returns "Error: Invalid value provided." |
# | General Exception     | Catches any other unexpected errors.             | If an unexpected error occurs, it returns a message with the error details. |
# """
# print(explanation_errors)



"""Task-4"""

"""2303A52324"""
# import hashlib
# import getpass
# # Simple login system with secure password handling
# users_db = {
#     "user1": hashlib.sha256("password123".encode()).hexdigest(),
#     "user2": hashlib.sha256("mysecurepassword".encode()).hexdigest()
# }
# def hash_password(password):
#     """Hash a password using SHA-256."""
#     return hashlib.sha256(password.encode()).hexdigest()
# def verify_login(username, password):
#     """Verify user login credentials."""
#     if username in users_db:
#         hashed_input_password = hash_password(password)
#         if users_db[username] == hashed_input_password:
#             return True
#     return False
# # Example usage
# username = input("Enter username: ")
# password = getpass.getpass("Enter password: ")
# if verify_login(username, password):
#     print("Login successful!")
# else:
#     print("Invalid username or password.")



# Analysis of Password Handling Practices:
# 1. Plain-text Password Storage:
#    - The generated code does not store passwords in plain text; instead, it uses SHA-256 hashing.
#    - This is a good practice as it prevents exposure of actual passwords if the database is
#      compromised.
# 2. Lack of Hashing or Salting:
#    - While the code uses hashing, it does not implement salting.
#    - Salting adds random data to passwords before hashing, making it more secure against
#      rainbow table attacks. The absence of salting is a security flaw.
# 3. Weak Input Validation:
#    - The code does not validate the username and password inputs for length, complexity,
#      or format.
#    - Weak input validation can lead to vulnerabilities such as injection attacks or
#      acceptance of weak passwords.
# 4. Vulnerability to Brute-Force Attempts:
#    - The code does not implement any mechanisms to prevent brute-force attacks, such as
#      account lockout after multiple failed attempts or rate limiting.
#    - This makes the system vulnerable to attackers trying multiple password combinations
#      to gain access.
# In summary, while the generated code demonstrates some secure practices like hashing passwords,
# it lacks critical security measures such as salting, input validation, and protection against
# brute-force attacks, which are essential for a robust authentication system in real-world applications.




"""18/2/26"""
"""Task Description #1 (Username Validator – Apply AI in Authentication Context)
•	Task: Use AI to generate at least 3 assert test cases for a function is_valid_username(username) and then implement the function using Test-Driven Development principles.
•	Requirements:
o	Username length must be between 5 and 15 characters.
o	Must contain only alphabets and digits.
o	Must not start with a digit.
o	No spaces allowed.
Example Assert Test Cases:
assert is_valid_username("User123") == True  
assert is_valid_username("12User") == False  
assert is_valid_username("Us er") == False  
Expected Output #1:
•	Username validation logic successfully passing all AI-generated test cases.
"""

"""Prompt-Generate Python code using Test-Driven Development (TDD) for a function is_valid_username(username).
First, write at least 5 assert test cases.
Then implement the code.
Requirements:
Username length must be between 5 and 15 characters.
Must contain only alphabets and digits.
Must not start with a digit.
No spaces allowed.
Return True if valid, otherwise False.
Ensure all test cases pass."""

"""python -m doctest -v Task-8-5.py"""

# # Implementation
# def is_valid_username(username):
#     # Check length between 5 and 15
#     if len(username) < 5 or len(username) > 15:
#         return False
#     # Check for spaces
#     if " " in username:
#         return False
#     # Check if starts with digit
#     if username[0].isdigit():
#         return False
#     # Check if contains only alphabets and digits
#     if not username.isalnum():
#         return False
#     return True
# # Test cases
# assert is_valid_username("User123") == True
# assert is_valid_username("12User") == False
# assert is_valid_username("Us er") == False
# assert is_valid_username("abc") == False
# assert is_valid_username("ValidUser99") == True
# assert is_valid_username("1nvalid") == False
# assert is_valid_username("toolongusernamehere") == False


"""Task Description #2 (Even–Odd & Type Classification – Apply AI for Robust Input Handling)
•	Task: Use AI to generate at least 3 assert test cases for a function classify_value(x) and implement it using conditional logic and loops.
•	Requirements:
o	If input is an integer, classify as "Even" or "Odd".
o	If input is 0, return "Zero".
o	If input is non-numeric, return "Invalid Input".
Example Assert Test Cases:
assert classify_value(8) == "Even"  
assert classify_value(7) == "Odd"  
assert classify_value("abc") == "Invalid Input"  
Expected Output #2:
Function correctly classifying values and passing all test cases.
"""

"""Prompt-Generate Python code using Test-Driven Development (TDD) for a function classify_value(x).
First, write at least 5 assert test cases.
Then implement the function using conditional logic and loops.
Requirements:
If input is an integer, return "Even" or "Odd".
If input is 0, return "Zero".
If input is non-numeric, return "Invalid Input".
Ensure all test cases pass successfully.
Provide clean and properly formatted Python code only."""


# # Implementation
# def classify_value(x):
#     # Check if input is an integer
#     if not isinstance(x, int) or isinstance(x, bool):
#         return "Invalid Input"
#     # Check if zero
#     if x == 0:
#         return "Zero"
#     # Check if even or odd
#     if x % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# # Test cases
# assert classify_value(0) == "Zero"
# assert classify_value(8) == "Even"
# assert classify_value(7) == "Odd"
# assert classify_value("abc") == "Invalid Input"
# assert classify_value(-4) == "Even"
# assert classify_value(-3) == "Odd"
# assert classify_value(15.5) == "Invalid Input"    

"""DocTest"""

# def classify_value(x):
#     """
#     Classify the input value.

#     >>> classify_value(0)
#     'Zero'
#     >>> classify_value(4)
#     'Even'
#     >>> classify_value(7)
#     'Odd'
#     >>> classify_value("hello")
#     'Invalid Input'
#     >>> classify_value(3.14)
#     'Invalid Input'
#     """
#     if x == 0:
#         return "Zero"
#     elif isinstance(x, int):
#         if x % 2 == 0:
#             return "Even"
#         else:
#             return "Odd"
#     else:
#         return "Invalid Input"
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()

"""Task Description #3 (Palindrome Checker – Apply AI for String Normalization)
•	Task: Use AI to generate at least 3 assert test cases for a function is_palindrome(text) and implement the function.
•	Requirements:
o	Ignore case, spaces, and punctuation.
o	Handle edge cases such as empty strings and single characters.
Example Assert Test Cases:
assert is_palindrome("Madam") == True  
assert is_palindrome("A man a plan a canal Panama") == True  
assert is_palindrome("Python") == False  
Expected Output #3:
Function correctly identifying palindromes and passing all AI-generated tests.
"""

"""pip install pytest"""

"""Prompt-Generate Python code using Test-Driven Development (TDD) for a function is_palindrome(text).
First, write at least 5 assert test cases.
Then implement the function.
Requirements:
Ignore case, spaces, and punctuation.
Handle edge cases like empty strings and single characters.
Return True if the text is a palindrome, otherwise False.
Ensure all test cases pass.
Provide clean and properly formatted Python code only."""

# def is_palindrome(text):
#     # Remove spaces, punctuation, and convert to lowercase
#     cleaned = ''.join(char.lower() for char in text if char.isalnum())
#     # Compare with reversed version
#     return cleaned == cleaned[::-1]

# # Test cases
# assert is_palindrome("Madam") == True
# assert is_palindrome("A man a plan a canal Panama") == True
# assert is_palindrome("Python") == False
# assert is_palindrome("") == True
# assert is_palindrome("a") == True
# assert is_palindrome("race car") == True
# assert is_palindrome("hello") == False

# print("All test cases passed!")


"""Task Description #4 (BankAccount Class – Apply AI for Object-Oriented Test-Driven Development)
•	Task: Ask AI to generate at least 3 assert-based test cases for a BankAccount class and then implement the class.
•	Methods:
o	deposit(amount)
o	withdraw(amount)
o	get_balance()
Example Assert Test Cases:
acc = BankAccount(1000)
acc.deposit(500)
assert acc.get_balance() == 1500  
acc.withdraw(300)
assert acc.get_balance() == 1200  
Expected Output #4:
•	Fully functional class that passes all AI-generated assertions.
"""

"""Prompt: Generate Python code using Test-Driven Development (TDD) for a BankAccount class.
First, write at least 5 assert-based test cases.
Then implement the class.
The class should include:
deposit(amount)
withdraw(amount)
get_balance()
Ensure:
Deposits increase balance.
Withdrawals decrease balance (handle insufficient balance properly).
Initial balance is set through the constructor.
Make sure all test cases pass.
Provide clean and properly formatted Python code only."""

# class BankAccount:
#     def __init__(self, initial_balance):
#         self.balance = initial_balance
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             return True
#         return False
#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             return True
#         return False
#     def get_balance(self):
#         return self.balance
# # Test cases
# acc = BankAccount(1000)
# assert acc.get_balance() == 1000
# acc.deposit(500)
# assert acc.get_balance() == 1500
# acc.withdraw(300)
# assert acc.get_balance() == 1200
# assert acc.withdraw(2000) == False
# assert acc.get_balance() == 1200
# assert acc.deposit(800) == True
# assert acc.get_balance() == 2000
# print("All test cases passed!")

"""Task Description #5 (Email ID Validation – Apply AI for Data Validation)
•	Task: Use AI to generate at least 3 assert test cases for a function validate_email(email) and implement the function.
•	Requirements:
o	Must contain @ and .
o	Must not start or end with special characters.
o	Should handle invalid formats gracefully.
Example Assert Test Cases:
assert validate_email("user@example.com") == True  
assert validate_email("userexample.com") == False  
assert validate_email("@gmail.com") == False  
Expected Output #5:
•	Email validation function passing all AI-generated test cases and handling edge cases correctly.
"""

"""Prompt: Generate Python code using Test-Driven Development (TDD) for a function validate_email(email).
First, write at least 5 assert test cases.
Then implement the function.
Requirements:
Email must contain @ and .
Must not start or end with special characters
Handle invalid formats gracefully
Return True if valid, otherwise False
Ensure all test cases pass successfully.
Provide clean and properly formatted Python code only."""

# def validate_email(email):
#     # Check if email is a string
#     if not isinstance(email, str):
#         return False
#     # Check if @ and . are present
#     if "@" not in email or "." not in email:
#         return False
#     # Check if starts or ends with special characters
#     if email[0] in "@." or email[-1] in "@.":
#         return False
#     # Check basic structure: local@domain.extension
#     parts = email.split("@")
#     if len(parts) != 2:
#         return False
#     local, domain = parts
#     if not local or not domain:
#         return False
#     # Check if domain has a dot
#     if "." not in domain:
#         return False
#     domain_parts = domain.split(".")
#     if len(domain_parts) < 2 or not domain_parts[-1]:
#         return False
#     # Check if local and domain contain only valid characters
#     if not all(c.isalnum() or c in "._-" for c in local):
#         return False
#     if not all(c.isalnum() or c in ".-" for c in domain):
#         return False
#     return True

# # Test cases
# assert validate_email("user@example.com") == True
# assert validate_email("userexample.com") == False
# assert validate_email("@gmail.com") == False
# assert validate_email("user@gmail") == False
# assert validate_email("user.name@example.co.uk") == True
# assert validate_email("user@.com") == True
# assert validate_email("user@example.") == False
# assert validate_email("invalid.email@") == False

# print("All test cases passed!")
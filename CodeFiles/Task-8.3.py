"""Assignment-8.3"""

"""Task-1"""
"""Prompt: You are a Python developer following Test-Driven Development (TDD).
Task: Implement Email Validation for a user registration system using a test-first approach.
Step 1:
Generate comprehensive AI-created test cases using Python's unittest framework BEFORE writing the implementation.
Test Case Requirements:
• Include multiple valid email formats.
• Include multiple invalid email formats.
• Cover edge cases.
• Tests must clearly check both True and False outcomes.
Validation Rules:
1. Email must contain exactly one '@' symbol.
2. Email must contain at least one '.' character.
3. Email must not start with special characters.
4. Email must not end with special characters.
5. Email must not allow multiple '@' symbols.
6. '@' must not be the first or last character.
7. '.' must appear after '@' in the domain part.
8. Username and domain must not be empty.
Invalid Examples to Test:
• Missing '@'
• Missing '.'
• Multiple '@'
• Starts with special character
• Ends with special character
• '@' at beginning
• '@' at end
• No username
• No domain
• Dot immediately before or after '@'
Step 2:
Implement the function:
    def is_valid_email(email):
Implementation Requirements:
• Do NOT use regular expressions.
• Use basic string methods only.
• Keep the code clean and readable.
• Ensure all AI-generated test cases pass.
Step 3:
Include a main block to execute unittest.
Output Format:
1. AI-generated unittest test cases
2. Implementation of is_valid_email(email)
3. Main block to run tests
The final output must be complete, clean, and runnable Python code.
"""

"""2303A52324"""
# import unittest
# def is_valid_email(email):
#     # Must contain exactly one '@'
#     if email.count('@') != 1:
#         return False
#     # Must contain at least one '.'
#     if '.' not in email:
#         return False
#     # Must not start or end with special characters
#     special_chars = "@."
#     if email[0] in special_chars or email[-1] in special_chars:
#         return False
#     # Split into username and domain
#     username, domain = email.split('@')
#     # Username and domain must not be empty
#     if not username or not domain:
#         return False
#     # Domain must contain '.'
#     if '.' not in domain:
#         return False
#     # Dot must not be immediately before or after '@'
#     if username.endswith('.') or domain.startswith('.'):
#         return False
#     return True
# class TestEmailValidation(unittest.TestCase):
#     def test_email_validation(self):
#         emails = [
#             "user@example.com",
#             "john.doe@gmail.com",
#             "student123@college.edu",
#             "userexample.com",          # Missing @
#             "user@examplecom",          # Missing .
#             "user@@example.com",        # Multiple @
#             "@example.com",             # Starts with @
#             "user@example.com.",        # Ends with .
#             "user@",                    # No domain
#             "user.@example.com",        # Dot before @
#             "user@.example.com"         # Dot after @
#         ]
#         for email in emails:
#             result = is_valid_email(email)
#             # Print email and validation result
#             if result:
#                 print(f"{email} --> VALID (True)")
#             else:
#                 print(f"{email} --> INVALID (False)")
#             # Assertions for testing
#             if email in ["user@example.com",
#                          "john.doe@gmail.com",
#                          "student123@college.edu"]:
#                 self.assertTrue(result)
#             else:
#                 self.assertFalse(result)
# if __name__ == "__main__":
#     unittest.main()


"""Task-2"""
"""Prompt: You are a Python developer following Test-Driven Development (TDD).

Task: Implement a grade assignment system for an online examination platform.

Step 1:
First generate comprehensive AI-created test cases using Python’s unittest framework BEFORE writing the implementation.

Grading Rules:
• 90–100 → A
• 80–89 → B
• 70–79 → C
• 60–69 → D
• Below 60 → F

Requirements:
1. Include boundary value tests:
   - 60, 70, 80, 90
   - Also test 59, 69, 79, 89, 100
2. Include invalid inputs:
   - Negative values (e.g., -5)
   - Values greater than 100 (e.g., 105)
   - Non-numeric input (e.g., "eighty")
3. Invalid inputs must be handled gracefully.
   - Return "Invalid Input" instead of crashing.
4. Use loops where appropriate to test multiple values.
5. Implement function:

       def assign_grade(score):

6. Ensure:
   - Correct grade is returned
   - Boundary values handled correctly
   - Invalid inputs handled safely
   - All test cases pass successfully

Output Format:
1. AI-generated unittest test cases
2. Implementation of assign_grade(score)
3. Main block to run tests
4. Also print each score and its assigned grade clearly
5. Final output must be complete, clean, and runnable Python code.
"""

"""2303A52324"""
# import unittest
# def assign_grade(score):
#     # Handle non-numeric input
#     if not isinstance(score, (int, float)):
#         return "Invalid Input"
#     # Handle invalid range
#     if score < 0 or score > 100:
#         return "Invalid Input"
#     # Grade assignment
#     if 90 <= score <= 100:
#         return "A"
#     elif 80 <= score <= 89:
#         return "B"
#     elif 70 <= score <= 79:
#         return "C"
#     elif 60 <= score <= 69:
#         return "D"
#     else:
#         return "F"
# class TestGradeAssignment(unittest.TestCase):
#     def test_valid_grades(self):
#         test_cases = {
#             95: "A",
#             90: "A",     # Boundary
#             85: "B",
#             80: "B",     # Boundary
#             75: "C",
#             70: "C",     # Boundary
#             65: "D",
#             60: "D",     # Boundary
#             55: "F",
#             59: "F",     # Just below boundary
#             69: "D",
#             79: "C",
#             89: "B",
#             100: "A"
#         }
#         for score, expected in test_cases.items():
#             result = assign_grade(score)
#             print(f"Score: {score} --> Grade: {result}")
#             self.assertEqual(result, expected)
#     def test_invalid_inputs(self):
#         invalid_cases = [-5, 105, "eighty"]
#         for value in invalid_cases:
#             result = assign_grade(value)
#             print(f"Score: {value} --> Grade: {result}")
#             self.assertEqual(result, "Invalid Input")
# if __name__ == "__main__":
#     unittest.main()

"""Task-3"""
"""Prompt: You are a Python developer following Test-Driven Development (TDD).

Task: Implement a sentence palindrome checker.

Function to implement:
    def is_sentence_palindrome(sentence)

Requirements:
1. First, generate AI-created test cases using Python’s unittest framework BEFORE writing the implementation.
2. Ignore:
   • Case differences
   • Spaces
   • Punctuation
3. Only consider alphanumeric characters.
4. The function must return:
   • True → if the sentence is a palindrome
   • False → if not

Test Requirements:
• Include multiple palindromic sentences.
• Include multiple non-palindromic sentences.
• Include edge cases:
   - Empty string
   - Single character
   - Only punctuation
• Example:
   "A man a plan a canal Panama" → True
   "Hello World" → False

Implementation Rules:
• Do NOT use external libraries.
• You may use string methods and loops.
• Ensure all test cases pass.
• Print each sentence and whether it is a palindrome.

Output Format:
1. AI-generated unittest test cases
2. Implementation of is_sentence_palindrome
3. Main block to run tests
4. Printed output showing each sentence and result
"""

"""2303A52324"""
# import unittest
# import string
# def is_sentence_palindrome(sentence):
#     # Remove non-alphanumeric characters and convert to lowercase
#     cleaned = ""
#     for char in sentence:
#         if char.isalnum():
#             cleaned += char.lower()
#     # Check palindrome
#     return cleaned == cleaned[::-1]
# class TestSentencePalindrome(unittest.TestCase):
#     def test_palindromes(self):
#         palindromes = [
#             "A man a plan a canal Panama",
#             "Madam",
#             "Was it a car or a cat I saw",
#             "No lemon no melon",
#             "",
#             "A"
#         ]
#         for sentence in palindromes:
#             result = is_sentence_palindrome(sentence)
#             print(f'"{sentence}" --> {result}')
#             self.assertTrue(result)
#     def test_non_palindromes(self):
#         non_palindromes = [
#             "Hello World",
#             "Python Programming",
#             "OpenAI ChatGPT",
#             "Palindrome Test"
#         ]
#         for sentence in non_palindromes:
#             result = is_sentence_palindrome(sentence)
#             print(f'"{sentence}" --> {result}')
#             self.assertFalse(result)
# if __name__ == "__main__":
#     unittest.main()


"""Task-4"""
"""Prompt: You are a Python developer following Test-Driven Development (TDD).
Task: Implement a ShoppingCart class for an e-commerce application.
Step 1:
First generate comprehensive AI-created test cases using Python's unittest framework BEFORE writing the implementation.
Class Requirements:
The ShoppingCart class must include:
1. add_item(name, price)
   - Adds an item with its price to the cart.
   - Price must be positive.
2. remove_item(name)
   - Removes an item from the cart.
   - If item does not exist, handle gracefully.
3. total_cost()
   - Returns total price of all items in the cart.
Test Case Requirements:
• Test adding multiple items.
• Test removing items.
• Test total cost calculation.
• Test removing non-existing item.
• Test empty cart total cost (should return 0).
• Test adding invalid price (negative or non-numeric).
Implementation Requirements:
• Use a dictionary or list to store items.
• Ensure clean, readable code.
• Handle empty cart scenario.
• All AI-generated test cases must pass.
• Print cart contents and total cost during testing.
Output Format:
1. AI-generated unittest test cases
2. Implementation of ShoppingCart class
3. Main block to run tests
4. Clear printed output showing operations
"""

"""2303A52324"""
# import unittest
# class ShoppingCart:
#     def __init__(self):
#         self.items = {}
#     def add_item(self, name, price):
#         if not isinstance(price, (int, float)) or price <= 0:
#             return "Invalid Price"
#         self.items[name] = price
#     def remove_item(self, name):
#         if name in self.items:
#             del self.items[name]
#         else:
#             return "Item Not Found"
#     def total_cost(self):
#         return sum(self.items.values())
# class TestShoppingCart(unittest.TestCase):
#     def test_add_and_total(self):
#         cart = ShoppingCart()
#         cart.add_item("Laptop", 50000)
#         cart.add_item("Mouse", 500)
#         print("Cart Items after adding:", cart.items)
#         print("Total Cost:", cart.total_cost())
#         self.assertEqual(cart.total_cost(), 50500)
#     def test_remove_item(self):
#         cart = ShoppingCart()
#         cart.add_item("Phone", 20000)
#         cart.add_item("Charger", 1000)
#         cart.remove_item("Charger")
#         print("Cart Items after removal:", cart.items)
#         print("Total Cost:", cart.total_cost())
#         self.assertEqual(cart.total_cost(), 20000)
#     def test_empty_cart(self):
#         cart = ShoppingCart()
#         print("Empty Cart Total:", cart.total_cost())
#         self.assertEqual(cart.total_cost(), 0)
#     def test_remove_non_existing_item(self):
#         cart = ShoppingCart()
#         result = cart.remove_item("Tablet")
#         print("Remove non-existing item:", result)
#         self.assertEqual(result, "Item Not Found")
#     def test_invalid_price(self):
#         cart = ShoppingCart()
#         result = cart.add_item("Headphones", -500)
#         print("Invalid Price Add Attempt:", result)
#         self.assertEqual(result, "Invalid Price")
# if __name__ == "__main__":
#     unittest.main()


"""Task-5"""
"""Prompt: You are a Python developer following Test-Driven Development (TDD).
Task: Implement a date format conversion function.
Function to implement:
    def convert_date_format(date_str)
Requirements:
1. First generate AI-created test cases using Python’s unittest framework BEFORE writing the implementation.
2. Input format must strictly be "YYYY-MM-DD".
3. Output format must be "DD-MM-YYYY".
4. Example:
   "2023-10-15" → "15-10-2023"
Test Case Requirements:
• Include multiple valid date inputs.
• Include boundary cases like:
   - "2000-01-01"
   - "1999-12-31"
• Include invalid inputs:
   - Incorrect format (e.g., "15-10-2023")
   - Missing parts
   - Non-string input
   - Invalid month/day values
• Invalid inputs must be handled gracefully.
   - Return "Invalid Date Format"
Implementation Requirements:
• Use string methods (do not use datetime module).
• Validate format structure (YYYY-MM-DD).
• Ensure month is 01–12 and day is 01–31.
• Return converted format if valid.
• All AI-generated test cases must pass.
• Print input date and converted result.
Output Format:
1. AI-generated unittest test cases
2. Implementation of convert_date_format(date_str)
3. Main block to run tests
4. Printed output showing conversion results
"""

"""2303A52324"""
# import unittest
# def convert_date_format(date_str):
#     # Check if input is string
#     if not isinstance(date_str, str):
#         return "Invalid Date Format"
#     # Check format length
#     if len(date_str) != 10:
#         return "Invalid Date Format"
#     # Check structure YYYY-MM-DD
#     parts = date_str.split("-")
#     if len(parts) != 3:
#         return "Invalid Date Format"
#     year, month, day = parts
#     # Ensure numeric values
#     if not (year.isdigit() and month.isdigit() and day.isdigit()):
#         return "Invalid Date Format"
#     # Validate month and day range
#     month = int(month)
#     day = int(day)
#     if not (1 <= month <= 12 and 1 <= day <= 31):
#         return "Invalid Date Format"
#     # Return converted format
#     return f"{day:02d}-{month:02d}-{year}"
# class TestDateConversion(unittest.TestCase):
#     def test_valid_dates(self):
#         valid_dates = {
#             "2023-10-15": "15-10-2023",
#             "2000-01-01": "01-01-2000",
#             "1999-12-31": "31-12-1999"
#         }
#         for input_date, expected in valid_dates.items():
#             result = convert_date_format(input_date)
#             print(f"{input_date} --> {result}")
#             self.assertEqual(result, expected)
#     def test_invalid_dates(self):
#         invalid_dates = [
#             "15-10-2023",      # Wrong format
#             "2023/10/15",      # Wrong separator
#             "2023-13-01",      # Invalid month
#             "2023-10-40",      # Invalid day
#             "20231015",        # Missing separators
#             20231015           # Non-string input
#         ]
#         for date in invalid_dates:
#             result = convert_date_format(date)
#             print(f"{date} --> {result}")
#             self.assertEqual(result, "Invalid Date Format")
# if __name__ == "__main__":
#     unittest.main()

# Generate a Docstring Inline comments Google-style documentation to the reversing a string function.
# def reverse_string(s):
#     """
#     Reverses the given string.

#     Args:
#         s (str): The string to be reversed.

#     Returns:
#         str: The reversed string.
#     """
#     # Initialize an empty string to store the reversed result
#     reversed_str = ""
    
#     # Iterate through the input string in reverse order
#     for char in s:
#         reversed_str = char + reversed_str  # Prepend the current character to the result
    
#     return reversed_str  # Return the final reversed string
# # Example usage
# input_string = "Hello, World!"
# reversed_string = reverse_string(input_string)
# print(f"Original string: {input_string}")
# print(f"Reversed string: {reversed_string}")



# generate a 1.	Document the function using docstring, inline comments, and Google style
# .2.	Compare documentation styles for security-related code. for Password Strength Checker function
# def check_password_strength(password):
#     """
#     Checks the strength of a given password.

#     Args:
#         password (str): The password to be evaluated.

#     Returns:
#         str: A message indicating the strength of the password.
#     """
#     # Initialize variables to track the presence of different character types
#     has_upper = False
#     has_lower = False
#     has_digit = False
#     has_special = False

#     # Check the length of the password
#     if len(password) < 8:
#         return "Password is too short. It should be at least 8 characters long."

#     # Iterate through each character in the password to check for different types
#     for char in password:
#         if char.isupper():
#             has_upper = True  # Found an uppercase letter
#         elif char.islower():
#             has_lower = True  # Found a lowercase letter
#         elif char.isdigit():
#             has_digit = True  # Found a digit
#         elif not char.isalnum():
#             has_special = True  # Found a special character

#     # Determine the strength of the password based on the presence of character types
#     if has_upper and has_lower and has_digit and has_special:
#         return "Password is strong."
#     elif (has_upper and has_lower and has_digit) or (has_upper and has_lower and has_special) or (has_upper and has_digit and has_special) or (has_lower and has_digit and has_special):
#         return "Password is medium."
#     else:
#         return "Password is weak."
# # Example usage
# password = "P@ssw0rd"
# strength = check_password_strength(password)
# print(f"Password: {password}")
# print(f"Strength: {strength}")




# Generate a 1.	Create a module math_utils.py with functions:,square(n),cube(n),factorial(n),
# Generate docstrings automatically 
# math_utils.py
# def square(n):
#     """
#     Returns the square of a number.

#     Args:
#         n (int or float): The number to be squared.

#     Returns:
#         int or float: The square of the input number.
#     """
#     return n * n

# def cube(n):
#     """
#     Returns the cube of a number.

#     Args:
#         n (int or float): The number to be cubed.

#     Returns:
#         int or float: The cube of the input number.
#     """
#     return n * n * n

# def factorial(n):
#     """
#     Returns the factorial of a number.

#     Args:
#         n (int): The number to calculate factorial for.

#     Returns:
#         int: The factorial of the input number.
#     """
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# # Example usage
# if __name__ == "__main__":
#     num = 5
#     print(f"Square of {num}: {square(num)}")
#     print(f"Cube of {num}: {cube(num)}")
#     print(f"Factorial of {num}: {factorial(num)}")




# Generate 1.Create a module attendance.py with functions:mark_present(student),mark_absent(student),
# get_attendance(student) 3.Generate and view documentation 
# attendance.py
# class Attendance:
#     def __init__(self):
#         """
#         Initializes the Attendance class with an empty attendance record.
#         """
#         self.attendance_record = {}

#     def mark_present(self, student):
#         """
#         Marks a student as present.

#         Args:
#             student (str): The name of the student to be marked present.
#         """
#         self.attendance_record[student] = "Present"

#     def mark_absent(self, student):
#         """
#         Marks a student as absent.

#         Args:
#             student (str): The name of the student to be marked absent.
#         """
#         self.attendance_record[student] = "Absent"

#     def get_attendance(self, student):
#         """
#         Retrieves the attendance status of a student.

#         Args:
#             student (str): The name of the student whose attendance status is to be retrieved.

#         Returns:
#             str: The attendance status of the student ("Present", "Absent", or "Not Recorded").
#         """
#         return self.attendance_record.get(student, "Not Recorded")
# # Example usage
# if __name__ == "__main__":
#     attendance = Attendance()
#     attendance.mark_present("Alice")
#     attendance.mark_absent("Bob")
    
#     print(f"Alice's attendance: {attendance.get_attendance('Alice')}")
#     print(f"Bob's attendance: {attendance.get_attendance('Bob')}")
#     print(f"Charlie's attendance: {attendance.get_attendance('Charlie')}")



# Generate a code with def read_file(filename):,with open(filename, 'r') as f:,return f.read() 
# generate documentation using all three formats.2.	Identify which style best explains exception handling.

# def read_file(filename):
#     """
#     Reads the content of a file.

#     Args:
#         filename (str): The name of the file to be read.

#     Returns:
#         str: The content of the file.

#     Raises:
#         FileNotFoundError: If the specified file does not exist.
#         IOError: If an error occurs while reading the file.
#     """
#     try:
#         with open(filename, 'r') as f:
#             return f.read()  # Return the content of the file
#     except FileNotFoundError:
#         return f"Error: The file '{filename}' was not found."
#     except IOError as e:
#         return f"Error: An I/O error occurred while reading the file. Details: {e}"
# # Example usage
# if __name__ == "__main__":
#     filename = "example.txt"
#     content = read_file(filename)
#     print(content)

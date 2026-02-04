"""4/2/26"""

"""Task-1
"""

# class Student:
#     def __init__(self, name, roll_number, branch):
#         self.name = name
#         self.roll_number = roll_number
#         self.branch = branch
#     def display_details(self):
#         print("\n--- Student Details ---")
#         print("Name       :", self.name)
#         print("Roll No    :", self.roll_number)
#         print("Branch     :", self.branch)
# # Dynamic input from user
# name = input("Enter student name: ")
# roll_number = input("Enter roll number: ")
# branch = input("Enter branch: ")
# # Object creation
# student1 = Student(name, roll_number, branch)
# # Display details
# student1.display_details()


"""Task-2"""

"""For Loop"""
# def print_multiples_for(num):
#     print(f"\nFirst 10 multiples of {num} (using for loop):")
#     for i in range(1, 11):
#         print(num * i)
# # Dynamic input
# number = int(input("Enter a number: "))
# # Function call
# print_multiples_for(number)


"""While Loop"""
# def print_multiples_while(num):
#     print(f"\nFirst 10 multiples of {num} (using while loop):")
#     i = 1
#     while i <= 10:
#         print(num * i)
#         i += 1
# # Dynamic input
# number = int(input("Enter a number: "))
# # Function call
# print_multiples_while(number)


"""Task-3"""

"""2303A52324"""
"""If--Elif-Else Statements"""
# def classify_age(age):
#     if age < 0:
#         return "Invalid age"
#     elif age <= 12:
#         return "Child"
#     elif age <= 19:
#         return "Teenager"
#     elif age <= 59:
#         return "Adult"
#     else:
#         return "Senior Citizen"
# # Dynamic input
# age = int(input("Enter age: "))
# # Classification
# result = classify_age(age)
# print("Age Group:", result)


"""2303A52324"""
"""Multiple Elif Statements"""
# def classify_age_simple(age):
#     if age < 0:
#         return "Invalid age"
#     categories = {
#         (0, 12): "Child",
#         (13, 19): "Teenager",
#         (20, 59): "Adult",
#         (60, 150): "Senior Citizen"
#     }
#     for age_range, group in categories.items():
#         if age_range[0] <= age <= age_range[1]:
#             return group
# # Dynamic input
# age = int(input("Enter age: "))
# # Classification
# print("Age Group:", classify_age_simple(age))


"""Task-4"""

"""2303A52324"""
"""For Loop"""
# def sum_to_n_for(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total
# # Dynamic input
# n = int(input("Enter a positive integer: "))
# if n > 0:
#     print("Sum of first", n, "natural numbers (for loop):", sum_to_n_for(n))
# else:
#     print("Invalid input. Please enter a positive number.")


"""2303A52324"""
"""While Loop"""
# def sum_to_n_while(n):
#     total = 0
#     i = 1
#     while i <= n:
#         total += i
#         i += 1
#     return total
# # Dynamic input
# n = int(input("Enter a positive integer: "))
# if n > 0:
#     print("Sum of first", n, "natural numbers (while loop):", sum_to_n_while(n))
# else:
#     print("Invalid input. Please enter a positive number.")


"""2303A52324"""
"""Mathematical Formula"""
# def sum_to_n_formula(n):
#     return n * (n + 1) // 2
# # Dynamic input
# n = int(input("Enter a positive integer: "))
# if n > 0:
#     print("Sum of first", n, "natural numbers (formula):", sum_to_n_formula(n))
# else:
#     print("Invalid input. Please enter a positive number.")


"""Task-5"""

"""2303A52324"""
# class BankAccount:
#     def __init__(self, holder_name, initial_balance):
#         # Initialize account holder name and balance
#         self.holder_name = holder_name
#         self.balance = initial_balance
#     def deposit(self, amount):
#         # Add money to the account if amount is valid
#         if amount > 0:
#             self.balance += amount
#             print(f"₹{amount} deposited successfully.")
#         else:
#             print("Deposit amount must be positive.")
#     def withdraw(self, amount):
#         # Withdraw money if sufficient balance is available
#         if amount <= 0:
#             print("Withdrawal amount must be positive.")
#         elif amount > self.balance:
#             print("Insufficient balance.")
#         else:
#             self.balance -= amount
#             print(f"₹{amount} withdrawn successfully.")
#     def check_balance(self):
#         # Display the current balance
#         print(f"Current Balance: ₹{self.balance}")
# # Dynamic input from user
# name = input("Enter account holder name: ")
# initial_balance = float(input("Enter initial balance: "))
# # Create BankAccount object
# account = BankAccount(name, initial_balance)
# # Perform operations
# account.check_balance()
# deposit_amount = float(input("Enter amount to deposit: "))
# account.deposit(deposit_amount)
# withdraw_amount = float(input("Enter amount to withdraw: "))
# account.withdraw(withdraw_amount)
# # Final balance
# account.check_balance()


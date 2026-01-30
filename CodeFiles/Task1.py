# def next_prime(n):
#     """Return the next prime number greater than n."""
#     candidate = n + 1
#     while not is_prime(candidate):
#         candidate += 1
#     return candidate

# def is_prime(num):
#     """Check if a number is prime."""
#     if num < 2:
#         return False
#     if num == 2:
#         return True
#     if num % 2 == 0:
#         return False
#     for i in range(3, int(num**0.5) + 1, 2):
#         if num % i == 0:
#             return False
#     return True

# # Get input and print next prime
# user_input = int(input("Enter a number: "))
# result = next_prime(user_input)
# print(f"The next prime after {user_input} is {result}")

# Print multiplication tables from 100 to 1 in structured manner
# for num in range(100, 0, -1):
#     print(f"\n--- Table of {num} ---")
#     for i in range(1, 11):
#         print(f"{num} × {i} = {num * i}")

# Print multiplication tables from 100 to 1 in structured manner
# for num in range(100, 0, -1):
#     print(f"\n--- Table of {num} ---")
#     for i in range(1, 21):
#         print(f"{num} × {i} = {num * i}")
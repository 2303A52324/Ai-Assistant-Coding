"""Task-1"""
# def is_leap_year(year: int) -> bool:
#     """Return True if year is a leap year (Gregorian rules)."""
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
# if __name__ == "__main__":
#     while True:
#         s = input("Enter a year (or press Enter to quit): ").strip()
#         if s == "":
#             break
#         try:
#             y = int(s)
#         except ValueError:
#             print("Please enter a valid integer year.")
#             continue
#         if is_leap_year(y):
#             print(f"{y} is a leap year.")
#         else:
#             print(f"{y} is not a leap year.")



"""Task-2"""


# def gcd(a: int, b: int) -> int:
#     """Return the greatest common divisor of integers a and b using the Euclidean algorithm."""
#     if not isinstance(a, int) or not isinstance(b, int):
#         raise TypeError("a and b must be integers")
#     a, b = abs(a), abs(b)
#     if a == 0:
#         return b
#     if b == 0:
#         return a
#     while b:
#         a, b = b, a % b
#     return a

# if __name__ == "__main__":
#     # Example usage:
#     print("GCD: ",gcd(12, 18))  # Output: 6



"""Task-3"""
# def gcd(a: int, b: int) -> int:
#     if not isinstance(a, int) or not isinstance(b, int):
#         raise TypeError("a and b must be integers")
#     a, b = abs(a), abs(b)
#     while b:
#         a, b = b, a % b
#     return a

# def lcm(a: int, b: int) -> int:
#     if not isinstance(a, int) or not isinstance(b, int):
#         raise TypeError("a and b must be integers")
#     if a == 0 or b == 0:
#         return 0
#     return abs(a // gcd(a, b) * b)

# if __name__ == "__main__":
#     print("Lcm of 4,6: ",lcm(4, 6))   # 12
#     print("Lcm of 5,10: ",lcm(5, 10))  # 10
#     print("Lcm of 7,3: ",lcm(7, 3))   # 21


"""Task-4"""
# def binary_to_decimal(binary_str: str) -> int:
#     """Convert a binary string to its decimal integer equivalent.
#     Accepts optional leading sign (+/-) and optional 0b/0B prefix.
#     Raises TypeError if input is not a str and ValueError for invalid binary.
#     """
#     if not isinstance(binary_str, str):
#         raise TypeError("binary_str must be a string")
#     s = binary_str.strip()
#     if not s:
#         raise ValueError("empty binary string")
#     sign = 1
#     if s[0] in "+-":
#         sign = -1 if s[0] == "-" else 1
#         s = s[1:]
#         if not s:
#             raise ValueError("invalid binary string")
#     if s.startswith(("0b", "0B")):
#         s = s[2:]
#     if not s:
#         raise ValueError("empty binary string")
#     if any(c not in "01" for c in s):
#         raise ValueError("invalid binary string")
#     result = 0
#     for ch in s:
#         result = (result << 1) + int(ch)
#     return sign * result

# if __name__ == "__main__":
#     print(binary_to_decimal("1011"))     # 11
#     print(binary_to_decimal("-0b1011"))  # -11
#     print(binary_to_decimal("0"))        # 0


"""Task-5"""

# def decimal_to_binary(n: int) -> str:
#     """Convert a non-negative integer to its binary representation as a string."""
#     if not isinstance(n, int):
#         raise TypeError("n must be an integer")
#     if n < 0:
#         raise ValueError("n must be non-negative")
#     if n == 0:
#         return "0"
#     bits = []
#     while n:
#         bits.append(str(n & 1))
#         n >>= 1
#     return "".join(reversed(bits))

# if __name__ == "__main__":
#     print(decimal_to_binary(10))  # 1010


"""Task-6"""

# def is_harshad(n: int) -> bool:
#     """Return True if n is a Harshad (Niven) number: divisible by the sum of its digits."""
#     if not isinstance(n, int):
#         raise TypeError("n must be an integer")
#     if n <= 0:
#         raise ValueError("n must be a positive integer")
#     digit_sum = sum(int(d) for d in str(abs(n)))
#     if digit_sum == 0:
#         return False
#     return n % digit_sum == 0

# if __name__ == "__main__":
#     for val in (18, 21, 19):
#         print(f"{val}: {'Harshad Number' if is_harshad(val) else 'Not a Harshad Number'}")
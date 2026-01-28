
"""Task-1"""

# def is_leap_year(year: int) -> bool:
#     """
#     Return True if year is a leap year, False otherwise.
#     Leap year rules:
#       - divisible by 4
#       - except years divisible by 100, unless also divisible by 400
#     """
#     return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)


# def check_leap_from_input() -> None:
#     """Read a year from stdin and print whether it's a leap year."""
#     try:
#         year = int(input("Enter year: ").strip())
#     except ValueError:
#         print("Invalid input. Please enter an integer year.")
#         return

#     if is_leap_year(year):
#         print(f"{year} is a leap year.")
#     else:
#         print(f"{year} is not a leap year.")


# if __name__ == "__main__":
#     # Example usage
#     # Sample Input: 2000
#     # Sample Output: 2000 is a leap year.
#     check_leap_from_input()


"""Task-2"""

# def cm_to_inches(cm: float, ndigits: int = 2) -> float:
#     """
#     Convert centimeters to inches. Returns the value rounded to ndigits.
#     1 inch = 2.54 cm
#     """
#     return round(cm / 2.54, ndigits)


# def parse_cm_input(s: str) -> float:
#     """Parse input like '10', '10 cm', or '  10.5 CM ' into a float centimeters value."""
#     s = s.strip().lower().replace("cm", "").strip()
#     return float(s)


# if __name__ == "__main__":
#     # Interactive example
#     try:
#         user = input("Enter length in centimeters (e.g. '10 cm'): ")
#         cm_value = parse_cm_input(user)
#         inches = cm_to_inches(cm_value)
#         print(f"{cm_value} cm = {inches:.2f} inches")
#     except Exception as e:
#         print("Invalid input. Please enter a numeric value, optionally followed by 'cm'.")

#     # Sample test cases with outputs
#     print("\nSample conversions:")
#     samples = [10, 0, 2.54, 30.48]
#     for s in samples:
#         print(f"{s} cm -> {cm_to_inches(s):.2f} inches")


"""Task-3"""

# def format_name(full_name: str) -> str:
#     """
#     Format a full name into "Last, First".
#     - Uses the first token as First and the last token as Last.
#     - Returns empty string for empty input, single name returned as-is.
#     """
#     parts = full_name.strip().split()
#     if not parts:
#         return ""
#     if len(parts) == 1:
#         return parts[0]
#     return f"{parts[-1]}, {parts[0]}"
# if __name__ == "__main__":
#     # Interactive usage
#     name = input("Enter full name: ")
#     print(format_name(name))

#     # Sample inputs and outputs
#     samples = ["John Smith", "Anita Rao", "Rahul Verma", "Madonna", "  Alice   Bob   Carol  "]
#     print("\nSamples:")
#     for s in samples:
#         print(f"Input: {s!r} -> Output: {format_name(s)}")


"""Task-4"""

# def count_vowels(s: str) -> int:
#     """Return the number of vowels (a, e, i, o, u) in the given string (case-insensitive)."""
#     vowels = set("aeiouAEIOU")
#     return sum(1 for ch in s if ch in vowels)


# if __name__ == "__main__":
#     # Interactive usage
#     user_input = input("Enter a string: ")
#     total = count_vowels(user_input)
#     print(f"Vowel count: {total}")

#     # Sample input/output
#     # Sample Input: Hello World
#     # Sample Output: Vowel count: 3

#     # Additional sample runs
#     samples = ["Hello World", "AEIOU", "bcdfg", "The quick brown fox"]
#     for s in samples:
#         print(f"Input: {s!r} -> Vowel count: {count_vowels(s)}")


# import re
# def count_vowels(text: str) -> int:
#     """Return the number of vowels (a, e, i, o, u) in text (case-insensitive)."""
#     return len(re.findall(r"[aeiouAEIOU]", text))

# if __name__ == "__main__":
#     # Read a string from stdin and print the vowel count
#     s = input("Input: ")
#     print("Output:", count_vowels(s))

#     # Sample inputs and outputs
#     samples = ["hello", "Education", "sky"]
#     print("\nSamples:")
#     for sample in samples:
#         print(f"Input: {sample!r} -> Output: {count_vowels(sample)}")



# Comparison of two vowel-counting implementations (set-based vs regex-based)
# rows = [
#     ("Criterion", "Set-based (zero-shot)", "Regex-based (few-shot)"),
#     ("Accuracy", "Equivalent for ASCII vowels; both count a,e,i,o,u correctly", "Equivalent for ASCII vowels; both count a,e,i,o,u correctly"),
#     ("Readability", "Very clear: explicit set and iteration; easy for newcomers", "More concise but requires regex familiarity; pattern may be opaque to some"),
#     ("Logical clarity", "Intent obvious, minimal dependencies, easy to modify", "Intent clear if you know regex; flexible for patterns but less explicit"),
#     ("Performance", "Fast and low overhead for short strings", "Comparable for typical inputs; regex has compilation overhead but negligible amortized"),
#     ("Extensibility", "Easier to adapt for Unicode or custom rules programmatically", "Easier to extend via patterns (e.g., Unicode classes) but needs careful regex design"),
# ]

# # Print table
# col_widths = [max(len(str(r[i])) for r in rows) + 2 for i in range(3)]
# for r in rows:
#     print(r[0].ljust(col_widths[0]) + r[1].ljust(col_widths[1]) + r[2].ljust(col_widths[2]))

# # Conclusion
# print("\nConclusion: For most uses, the set-based (zero-shot) approach is preferable for readability and logical clarity while matching the regex version in accuracy. Use the regex (few-shot) approach when you need compact code or advanced pattern matching (e.g., Unicode classes).")


"""Task-5"""

# def count_lines(filename: str) -> int:
#     """
#     Return the number of lines in the given text file.

#     Logic: open the file and iterate over the file object (which yields one line at a time)
#     and sum 1 for each yielded line. This avoids loading the whole file into memory.
#     """
#     with open(filename, "r", encoding="utf-8") as f:
#         return sum(1 for _ in f)
# if __name__ == "__main__":
#     # Sample file 1 (Example 1)
#     sample1 = "sample1.txt"
#     with open(sample1, "w", encoding="utf-8") as f:
#         f.write("Hello\nWelcome to Python\nFile handling is easy\n")

#     # Sample file 2 (Example 2)
#     sample2 = "sample2.txt"
#     with open(sample2, "w", encoding="utf-8") as f:
#         f.write("AI\nPrompt Engineering\nFew-shot Learning\n")

#     # Run and print outputs
#     print("Sample 1 file content:")
#     print("Hello\nWelcome to Python\nFile handling is easy\n")
#     print("Output:")
#     print(f"Number of lines: {count_lines(sample1)}\n")

#     print("Sample 2 file content:")
#     print("AI\nPrompt Engineering\nFew-shot Learning\n")
#     print("Output:")
#     print(f"Number of lines: {count_lines(sample2)}")

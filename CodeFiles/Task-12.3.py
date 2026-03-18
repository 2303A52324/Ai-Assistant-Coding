"""Task 1: Sorting Student Records for Placement Drive
Scenario
SR University’s Training and Placement Cell needs to shortlist candidates efficiently during campus placements. Student records must be sorted by CGPA in descending order.
Tasks
1.	Use GitHub Copilot to generate a program that stores student records (Name, Roll Number, CGPA).
2.	Implement the following sorting algorithms using AI assistance:
o	Quick Sort
o	Merge Sort
3.	Measure and compare runtime performance for large datasets.
4.	Write a function to display the top 10 students based on CGPA.
Expected Outcome
•	Correctly sorted student records.
•	Performance comparison between Quick Sort and Merge Sort.
•	Clear output of top-performing students.
"""

# import random
# import time
# # Student class
# class Student:
#     def __init__(self, name, roll, cgpa):
#         self.name = name
#         self.roll = roll
#         self.cgpa = cgpa
#     def __repr__(self):
#         return f"{self.name} | {self.roll} | CGPA: {self.cgpa:.2f}"
# # Generate random students
# def generate_students(n):
#     students = []
#     for i in range(n):
#         name = "Student_" + str(i + 1)
#         roll = "SRU" + str(1000 + i)
#         cgpa = round(random.uniform(5.0, 10.0), 2)
#         students.append(Student(name, roll, cgpa))
#     return students
# # Quick Sort
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2].cgpa
#     left = [x for x in arr if x.cgpa > pivot]
#     middle = [x for x in arr if x.cgpa == pivot]
#     right = [x for x in arr if x.cgpa < pivot]
#     return quick_sort(left) + middle + quick_sort(right)
# # Merge Sort
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     return merge(left, right)
# def merge(left, right):
#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i].cgpa >= right[j].cgpa:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
# # Display top students
# def display_top_students(students, n=10):
#     print("\nTop", n, "Students Based on CGPA\n")
#     print("Name | Roll No | CGPA")
#     print("-" * 30)
#     for student in students[:n]:
#         print(student)
# # Main Program
# def main():
#     n = 10000  # dataset size
#     students = generate_students(n)
#     # Copy data for both sorts
#     students_qs = students.copy()
#     students_ms = students.copy()
#     # Quick Sort timing
#     start = time.time()
#     sorted_qs = quick_sort(students_qs)
#     end = time.time()
#     quick_time = end - start
#     # Merge Sort timing
#     start = time.time()
#     sorted_ms = merge_sort(students_ms)
#     end = time.time()
#     merge_time = end - start
#     # Results
#     print("Runtime Performance Comparison\n")
#     print("Quick Sort Time :", quick_time)
#     print("Merge Sort Time :", merge_time)
#     # Display top 10
#     display_top_students(sorted_qs, 10)
# if __name__ == "__main__":
#     main()



"""Task 2: Implementing Bubble Sort with AI Comments
•	Task: Write a Python implementation of Bubble Sort.
•	Instructions:
•	Students implement Bubble Sort normally.
•	Ask AI to generate inline comments explaining key logic (like swapping, passes, and termination).
•	Request AI to provide time complexity analysis.
•	Expected Output:
•	A Bubble Sort implementation with AI-generated explanatory comments and complexity analysis.
"""


# # Bubble Sort Implementation with Detailed Comments
# def bubble_sort(arr):
#     n = len(arr)
#     # Outer loop represents the number of passes
#     # After each pass, the largest unsorted element "bubbles up"
#     # to its correct position at the end of the list
#     for i in range(n):
#         # This flag checks if any swap happens during a pass
#         # If no swaps occur, the list is already sorted
#         swapped = False
#         # Inner loop performs pairwise comparisons
#         # n-i-1 because the last i elements are already sorted
#         for j in range(0, n - i - 1):
#             # Compare adjacent elements
#             if arr[j] > arr[j + 1]:
#                 # Swap elements if they are in the wrong order
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 # Mark that a swap has occurred
#                 swapped = True
#         # If no swapping happened in this pass,
#         # the array is already sorted so we stop early
#         if not swapped:
#             break
#     return arr
# # Example list
# numbers = [64, 34, 25, 12, 22, 11, 90]
# print("Original List:", numbers)
# # Perform Bubble Sort
# sorted_list = bubble_sort(numbers)
# print("Sorted List:", sorted_list)


"""Task 3: Quick Sort and Merge Sort Comparison
•	Task: Implement Quick Sort and Merge Sort using recursion.
•	Instructions:
•	Provide AI with partially completed functions for recursion.
•	Ask AI to complete the missing logic and add docstrings.
•	Compare both algorithms on random, sorted, and reverse-sorted lists.
•	Expected Output:
•	Working Quick Sort and Merge Sort implementations.
•	AI-generated explanation of average, best, and worst-case complexities.
"""

# import random
# import time
# def quick_sort(arr):
#     """
#     Quick Sort using recursion.

#     Parameters:
#     arr (list): List of numbers to be sorted

#     Returns:
#     list: Sorted list in ascending order
#     """
#     # Base case: if list has 0 or 1 element it is already sorted
#     if len(arr) <= 1:
#         return arr
#     # Choose pivot element
#     pivot = arr[len(arr) // 2]
#     # Partition the list into three parts
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     # Recursively sort left and right parts
#     return quick_sort(left) + middle + quick_sort(right)
# def merge_sort(arr):
#     """
#     Merge Sort using recursion.

#     Parameters:
#     arr (list): List of numbers to be sorted

#     Returns:
#     list: Sorted list in ascending order
#     """
#     # Base case
#     if len(arr) <= 1:
#         return arr
#     # Divide the array into two halves
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     # Merge sorted halves
#     return merge(left, right)
# def merge(left, right):
#     """
#     Merge two sorted lists into one sorted list.
#     """
#     result = []
#     i = j = 0
#     # Compare elements from both lists and merge
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     # Append remaining elements
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
# # Generate datasets
# n = 10000
# random_list = [random.randint(1, 10000) for _ in range(n)]
# sorted_list = sorted(random_list)
# reverse_list = sorted(random_list, reverse=True)
# def test_sorting(data, name):
#     print("\nDataset:", name)
#     start = time.time()
#     quick_sort(data.copy())
#     quick_time = time.time() - start
#     start = time.time()
#     merge_sort(data.copy())
#     merge_time = time.time() - start
#     print("Quick Sort Time :", quick_time)
#     print("Merge Sort Time :", merge_time)
# # Run comparisons
# test_sorting(random_list, "Random List")
# test_sorting(sorted_list, "Sorted List")
# test_sorting(reverse_list, "Reverse Sorted List")



"""Task 4 (Real-Time Application – Inventory Management System)
Scenario: A retail store’s inventory system contains thousands of products, each with attributes like product ID, name, price, and stock quantity. Store staff need to:
1.	Quickly search for a product by ID or name.
2.	Sort products by price or quantity for stock analysis.
Task:
•	Use AI to suggest the most efficient search and sort algorithms for this use case.
•	Implement the recommended algorithms in Python.
•	Justify the choice based on dataset size, update frequency, and performance requirements.
Expected Output:
•	A table mapping operation → recommended algorithm → justification.
•	Working Python functions for searching and sorting the inventory.
"""

# # Product class
# class Product:
#     def __init__(self, pid, name, price, quantity):
#         self.pid = pid
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def __repr__(self):
#         return f"{self.pid} | {self.name} | Price:{self.price} | Qty:{self.quantity}"
# # Binary Search (Search by Product ID)
# def binary_search(products, target_id):
#     low = 0
#     high = len(products) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if products[mid].pid == target_id:
#             return products[mid]
#         elif products[mid].pid < target_id:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return None
# # Linear Search (Search by Name)
# def linear_search(products, name):
#     for product in products:
#         if product.name.lower() == name.lower():
#             return product
#     return None
# # Quick Sort by Price
# def quick_sort_price(products):
#     if len(products) <= 1:
#         return products
#     pivot = products[len(products)//2].price
#     left = [p for p in products if p.price < pivot]
#     middle = [p for p in products if p.price == pivot]
#     right = [p for p in products if p.price > pivot]
#     return quick_sort_price(left) + middle + quick_sort_price(right)
# # Merge Sort by Quantity
# def merge_sort_quantity(products):
#     if len(products) <= 1:
#         return products
#     mid = len(products)//2
#     left = merge_sort_quantity(products[:mid])
#     right = merge_sort_quantity(products[mid:])
#     return merge(left, right)
# def merge(left, right):
#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i].quantity <= right[j].quantity:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
# # Sample inventory dataset
# inventory = [
#     Product(101, "Laptop", 75000, 15),
#     Product(102, "Mouse", 500, 150),
#     Product(103, "Keyboard", 1200, 80),
#     Product(104, "Monitor", 12000, 40),
#     Product(105, "Printer", 8000, 20),
# ]
# # Sort inventory by Product ID for binary search
# inventory.sort(key=lambda x: x.pid)
# # Search operations
# print("Search by Product ID:")
# print(binary_search(inventory, 103))
# print("\nSearch by Product Name:")
# print(linear_search(inventory, "Monitor"))
# # Sorting operations
# print("\nProducts Sorted by Price:")
# sorted_price = quick_sort_price(inventory)
# for p in sorted_price:
#     print(p)
# print("\nProducts Sorted by Quantity:")
# sorted_quantity = merge_sort_quantity(inventory)
# for p in sorted_quantity:
#     print(p)

"""Task 5: Real-Time Stock Data Sorting & Searching
Scenario:
An AI-powered FinTech Lab at SR University is building a tool for analyzing stock price movements. 
The requirement is to quickly sort stocks by daily gain/loss and search for specific stock symbols efficiently.
•	Use GitHub Copilot to fetch or simulate stock price data (Stock Symbol, Opening Price, Closing Price).
•	Implement sorting algorithms to rank stocks by percentage change.
•	Implement a search function that retrieves stock data instantly when a stock symbol is entered.
•	Optimize sorting with Heap Sort and searching with Hash Maps.
•	Compare performance with standard library functions (sorted(), dict lookups) and analyze trade-offs.
"""


# import random
# import time
# # Stock class
# class Stock:
#     def __init__(self, symbol, open_price, close_price):
#         self.symbol = symbol
#         self.open_price = open_price
#         self.close_price = close_price
#         self.change = ((close_price - open_price) / open_price) * 100
#     def __repr__(self):
#         return f"{self.symbol} | Open:{self.open_price:.2f} Close:{self.close_price:.2f} Change:{self.change:.2f}%"
# # Generate simulated stock data
# def generate_stocks(n):
#     symbols = [f"STK{i}" for i in range(n)]
#     stocks = []
#     for s in symbols:
#         open_price = random.uniform(100, 500)
#         close_price = random.uniform(100, 500)
#         stocks.append(Stock(s, open_price, close_price))
#     return stocks
# # Heapify function for Heap Sort
# def heapify(arr, n, i):
#     largest = i
#     left = 2*i + 1
#     right = 2*i + 2
#     if left < n and arr[left].change > arr[largest].change:
#         largest = left
#     if right < n and arr[right].change > arr[largest].change:
#         largest = right
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, n, largest)
# # Heap Sort
# def heap_sort(arr):
#     n = len(arr)
#     # Build max heap
#     for i in range(n//2 - 1, -1, -1):
#         heapify(arr, n, i)
#     # Extract elements
#     for i in range(n-1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#         heapify(arr, i, 0)
#     arr.reverse()  # highest change first
#     return arr
# # Create hashmap for stock search
# def create_stock_map(stocks):
#     stock_map = {}
#     for stock in stocks:
#         stock_map[stock.symbol] = stock
#     return stock_map
# # Search stock
# def search_stock(stock_map, symbol):
#     return stock_map.get(symbol, "Stock Not Found")
# # Main program
# stocks = generate_stocks(30)
# # Hash map creation
# stock_map = create_stock_map(stocks)
# # Heap Sort timing
# heap_data = stocks.copy()
# start = time.time()
# heap_sorted = heap_sort(heap_data)
# heap_time = time.time() - start
# # Python sorted() timing
# start = time.time()
# python_sorted = sorted(stocks, key=lambda x: x.change, reverse=True)
# python_time = time.time() - start
# print("Top 10 Stocks by Percentage Gain/Loss\n")
# for s in heap_sorted[:10]:
#     print(s)
# # Search example
# print("\nSearch Stock:")
# print(search_stock(stock_map, "STK10"))
# # Performance comparison
# print("\nPerformance Comparison")
# print("Heap Sort Time:", heap_time)
# print("Python sorted() Time:", python_time)
# print("Hash Map Search Time: O(1) average")
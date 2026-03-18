"""Task Description #1 (Sorting – Merge Sort Implementation)
•	Task: Use AI to generate a Python program that implements the Merge Sort algorithm.
•	Instructions:
o	Prompt AI to create a function merge_sort(arr) that sorts a list in ascending order.
o	Ask AI to include time complexity and space complexity in the function docstring.
o	Verify the generated code with test cases.
•	Expected Output:
o	A functional Python script implementing Merge Sort with proper documentation.
"""


# def merge_sort(arr):
#     """
#     Sorts a list using the Merge Sort algorithm.

#     Parameters:
#     arr (list): The list of elements to be sorted.

#     Returns:
#     list: A new list containing the sorted elements in ascending order.

#     Time Complexity:
#     - Best Case: O(n log n)
#     - Average Case: O(n log n)
#     - Worst Case: O(n log n)

#     Space Complexity:
#     - O(n) auxiliary space for merging.
#     """
#     # Base case: A list of size 0 or 1 is already sorted
#     if len(arr) <= 1:
#         return arr
#     # Divide the list into two halves
#     mid = len(arr) // 2
#     left_half = merge_sort(arr[:mid])
#     right_half = merge_sort(arr[mid:])
#     # Merge the sorted halves
#     return merge(left_half, right_half)
# def merge(left, right):
#     """Helper function to merge two sorted lists."""
#     merged = []
#     i = j = 0
#     # Compare elements and merge them in sorted order
#     while i < len(left) and j < len(right):

#         if left[i] <= right[j]:
#             merged.append(left[i])
#             i += 1
#         else:
#             merged.append(right[j])
#             j += 1
#     # Add remaining elements if any
#     merged.extend(left[i:])
#     merged.extend(right[j:])
#     return merged
# # Test Cases
# if __name__ == "__main__":
#     test1 = [38, 27, 43, 3, 9, 82, 10]
#     test2 = [5, 2, 9, 1, 5, 6]
#     test3 = [1, 2, 3, 4, 5]
#     print("Original List:", test1)
#     print("Sorted List:", merge_sort(test1))
#     print("\nOriginal List:", test2)
#     print("Sorted List:", merge_sort(test2))
#     print("\nOriginal List:", test3)
#     print("Sorted List:", merge_sort(test3))


"""Task Description #2 (Searching – Binary Search with AI Optimization)
•	Task: Use AI to create a binary search function that finds a target element in a sorted list.
•	Instructions:
o	Prompt AI to create a function binary_search(arr, target) returning the index of the target or -1 if not found.
o	Include docstrings explaining best, average, and worst-case complexities.
o	Test with various inputs.
•	Expected Output:
o	Python code implementing binary search with AI-generated comments and docstrings.
"""


# def binary_search(arr, target):
#     """
#     Performs Binary Search on a sorted list.
#     Parameters:
#     arr (list): A sorted list of elements.
#     target (int/float): The value to search for.
#     Returns:
#     int: Index of the target element if found, otherwise -1.
#     Time Complexity:
#     Best Case: O(1)      -> Target found at the middle element immediately.
#     Average Case: O(log n)
#     Worst Case: O(log n) -> Search space halves every iteration.
#     Space Complexity:
#     O(1) for the iterative implementation.
#     """
#     # Initialize the search boundaries
#     left = 0
#     right = len(arr) - 1
#     # Continue searching while the search range is valid
#     while left <= right:
#         # Find the middle index
#         mid = (left + right) // 2
#         # Check if the middle element is the target
#         if arr[mid] == target:
#             return mid
#         # If target is greater, search the right half
#         elif arr[mid] < target:
#             left = mid + 1
#         # If target is smaller, search the left half
#         else:
#             right = mid - 1
#     # Target not found
#     return -1
# # Test Cases
# if __name__ == "__main__":
#     arr = [2, 5, 7, 10, 14, 18, 21, 30]
#     target1 = 14
#     target2 = 9
#     print("Array:", arr)
#     result1 = binary_search(arr, target1)
#     if result1 != -1:
#         print(f"Element {target1} found at index {result1}")
#     else:
#         print(f"Element {target1} not found")
#     result2 = binary_search(arr, target2)
#     if result2 != -1:
#         print(f"Element {target2} found at index {result2}")
#     else:
#         print(f"Element {target2} not found")


"""Task Description #3: Smart Healthcare Appointment Scheduling System
A healthcare platform maintains appointment records containing appointment ID, patient name, doctor name, appointment time, and consultation fee. The system needs to:
1.	Search appointments using appointment ID.
2.	Sort appointments based on time or consultation fee.
Student Task
•	Use AI to recommend suitable searching and sorting algorithms.
•	Justify the selected algorithms.
•	Implement the algorithms in Python.
"""


# # Appointment class
# class Appointment:
#     def __init__(self, aid, patient, doctor, time, fee):
#         self.aid = aid
#         self.patient = patient
#         self.doctor = doctor
#         self.time = time
#         self.fee = fee
#     def __repr__(self):
#         return f"{self.aid} | {self.patient} | {self.doctor} | Time:{self.time} | Fee:{self.fee}"
# # Binary Search by Appointment ID
# def binary_search(appointments, target_id):
#     low = 0
#     high = len(appointments) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if appointments[mid].aid == target_id:
#             return appointments[mid]
#         elif appointments[mid].aid < target_id:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return None
# # Merge Sort by Appointment Time
# def merge_sort_time(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort_time(arr[:mid])
#     right = merge_sort_time(arr[mid:])
#     return merge(left, right)
# def merge(left, right):
#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):

#         if left[i].time <= right[j].time:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
# # Quick Sort by Consultation Fee
# def quick_sort_fee(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr)//2].fee
#     left = [x for x in arr if x.fee < pivot]
#     middle = [x for x in arr if x.fee == pivot]
#     right = [x for x in arr if x.fee > pivot]
#     return quick_sort_fee(left) + middle + quick_sort_fee(right)
# # Sample appointment records
# appointments = [
#     Appointment(101, "Alice", "Dr. Smith", "09:00", 500),
#     Appointment(102, "Bob", "Dr. John", "10:30", 700),
#     Appointment(103, "Charlie", "Dr. Lee", "08:45", 400),
#     Appointment(104, "David", "Dr. Smith", "11:15", 600),
#     Appointment(105, "Eva", "Dr. Brown", "09:30", 450)
# ]
# # Sort appointments by ID for binary search
# appointments.sort(key=lambda x: x.aid)
# # Searching example
# print("Search Appointment by ID:")
# result = binary_search(appointments, 103)
# print(result)
# # Sorting by time
# print("\nAppointments Sorted by Time:")
# sorted_time = merge_sort_time(appointments)
# for a in sorted_time:
#     print(a)
# # Sorting by consultation fee
# print("\nAppointments Sorted by Fee:")
# sorted_fee = quick_sort_fee(appointments)
# for a in sorted_fee:
#     print(a)


"""Task Description #4: Railway Ticket Reservation System
Scenario
A railway reservation system stores booking details such as ticket ID, passenger name, train number, seat number, and travel date. The system must:
1.	Search tickets using ticket ID.
2.	Sort bookings based on travel date or seat number.
Student Task
•	Identify efficient algorithms using AI assistance.
•	Justify the algorithm choices.
•	Implement searching and sorting in Python
"""

# # Ticket class
# class Ticket:
#     def __init__(self, tid, passenger, train_no, seat_no, date):
#         self.tid = tid
#         self.passenger = passenger
#         self.train_no = train_no
#         self.seat_no = seat_no
#         self.date = date
#     def __repr__(self):
#         return f"{self.tid} | {self.passenger} | Train:{self.train_no} | Seat:{self.seat_no} | Date:{self.date}"
# # Binary Search by Ticket ID
# def binary_search(tickets, target_id):
#     low = 0
#     high = len(tickets) - 1
#     while low <= high:
#         mid = (low + high) // 2

#         if tickets[mid].tid == target_id:
#             return tickets[mid]
#         elif tickets[mid].tid < target_id:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return None
# # Merge Sort by Travel Date
# def merge_sort_date(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort_date(arr[:mid])
#     right = merge_sort_date(arr[mid:])
#     return merge(left, right)
# def merge(left, right):
#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i].date <= right[j].date:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
# # Quick Sort by Seat Number
# def quick_sort_seat(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr)//2].seat_no
#     left = [x for x in arr if x.seat_no < pivot]
#     middle = [x for x in arr if x.seat_no == pivot]
#     right = [x for x in arr if x.seat_no > pivot]
#     return quick_sort_seat(left) + middle + quick_sort_seat(right)
# # Sample ticket records
# tickets = [
#     Ticket(201, "Rahul", "12627", 45, "2026-03-15"),
#     Ticket(202, "Anita", "12628", 12, "2026-03-12"),
#     Ticket(203, "Kiran", "12005", 30, "2026-03-18"),
#     Ticket(204, "Meena", "12627", 5, "2026-03-11"),
#     Ticket(205, "Arjun", "12005", 21, "2026-03-14")
# ]
# # Sort tickets by ID for binary search
# tickets.sort(key=lambda x: x.tid)
# # Search ticket
# print("Search Ticket by ID:")
# print(binary_search(tickets, 203))
# # Sort by travel date
# print("\nTickets Sorted by Travel Date:")
# sorted_date = merge_sort_date(tickets)
# for t in sorted_date:
#     print(t)
# # Sort by seat number
# print("\nTickets Sorted by Seat Number:")
# sorted_seat = quick_sort_seat(tickets)
# for t in sorted_seat:
#     print(t)



"""Task Description #5: Smart Hostel Room Allocation System
A hostel management system stores student room allocation details including student ID, room number, floor, and allocation date. The system needs to:
1.	Search allocation details using student ID.
2.	Sort records based on room number or allocation date.
Student Task
•	Use AI to suggest optimized algorithms.
•	Justify the selections.
•	Implement the solution in Python.
"""

# from datetime import datetime
# # Hostel allocation records
# records = [
#     {"student_id": 101, "room": 205, "floor": 2, "date": "2024-07-01"},
#     {"student_id": 103, "room": 101, "floor": 1, "date": "2024-06-20"},
#     {"student_id": 102, "room": 303, "floor": 3, "date": "2024-07-10"},
#     {"student_id": 104, "room": 202, "floor": 2, "date": "2024-06-15"}
# ]
# # Convert date string to datetime
# for r in records:
#     r["date"] = datetime.strptime(r["date"], "%Y-%m-%d")
# # -------- Binary Search --------
# def binary_search(data, target):
#     low = 0
#     high = len(data) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if data[mid]["student_id"] == target:
#             return data[mid]
#         elif data[mid]["student_id"] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return None
# # -------- Sorting Functions --------
# def sort_by_room(data):
#     return sorted(data, key=lambda x: x["room"])
# def sort_by_date(data):
#     return sorted(data, key=lambda x: x["date"])
# # -------- Main Program --------
# print("Original Records")
# for r in records:
#     print(r)
# # Sort by student ID for searching
# records.sort(key=lambda x: x["student_id"])
# print("\nRecords Sorted by Student ID (for Binary Search)")
# for r in records:
#     print(r)
# # Search student
# student_id = int(input("\nEnter Student ID to search: "))
# result = binary_search(records, student_id)
# if result:
#     print("\nStudent Allocation Found:")
#     print(result)
# else:
#     print("\nStudent not found")
# # Sort by room number
# print("\nSorted by Room Number:")
# for r in sort_by_room(records):
#     print(r)
# # Sort by allocation date
# print("\nSorted by Allocation Date:")
# for r in sort_by_date(records):
#     print(r)


"""Task Description #6: Online Movie Streaming Platform
A streaming service maintains movie records with movie ID, title, genre, rating, and release year. The platform needs to:
1.	Search movies by movie ID.
2.	Sort movies based on rating or release year.
Student Task
•	Recommend searching and sorting algorithms using AI.
•	Justify the chosen algorithms.
•	Implement Python functions.
"""

# # Movie records
# movies = [
#     {"movie_id": 101, "title": "Inception", "genre": "Sci-Fi", "rating": 8.8, "year": 2010},
#     {"movie_id": 105, "title": "Avengers Endgame", "genre": "Action", "rating": 8.4, "year": 2019},
#     {"movie_id": 103, "title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6, "year": 2014},
#     {"movie_id": 102, "title": "Joker", "genre": "Drama", "rating": 8.5, "year": 2019},
#     {"movie_id": 104, "title": "The Dark Knight", "genre": "Action", "rating": 9.0, "year": 2008}
# ]
# # Binary Search for Movie ID
# def search_movie(movies, target):
#     low = 0
#     high = len(movies) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if movies[mid]["movie_id"] == target:
#             return movies[mid]
#         elif movies[mid]["movie_id"] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return None
# # Sort movies by rating
# def sort_by_rating(movies):
#     return sorted(movies, key=lambda x: x["rating"], reverse=True)
# # Sort movies by release year
# def sort_by_year(movies):
#     return sorted(movies, key=lambda x: x["year"])
# # Main Program
# print("Movie Records")
# for m in movies:
#     print(m)
# # Sort by movie_id before binary search
# movies.sort(key=lambda x: x["movie_id"])
# movie_id = int(input("\nEnter Movie ID to search: "))
# result = search_movie(movies, movie_id)
# if result:
#     print("\nMovie Found:")
#     print(result)
# else:
#     print("\nMovie not found")
# print("\nMovies Sorted by Rating:")
# for m in sort_by_rating(movies):
#     print(m)
# print("\nMovies Sorted by Release Year:")
# for m in sort_by_year(movies):
#     print(m)


"""Task Description #7: Smart Agriculture Crop Monitoring System
An agriculture monitoring system stores crop data with crop ID, crop name, soil moisture level, temperature, and yield estimate. Farmers need to:
1.	Search crop details using crop ID.
2.	Sort crops based on moisture level or yield estimate.
Student Task
•	Use AI-assisted reasoning to select algorithms.
•	Justify algorithm suitability.
•	Implement searching and sorting in Python.
"""


# # Crop monitoring records
# crops = [
#     {"crop_id": 101, "name": "Wheat", "moisture": 45, "temperature": 28, "yield": 3.5},
#     {"crop_id": 105, "name": "Rice", "moisture": 70, "temperature": 30, "yield": 4.2},
#     {"crop_id": 103, "name": "Corn", "moisture": 55, "temperature": 27, "yield": 3.8},
#     {"crop_id": 102, "name": "Barley", "moisture": 40, "temperature": 26, "yield": 2.9},
#     {"crop_id": 104, "name": "Soybean", "moisture": 60, "temperature": 29, "yield": 3.6}
# ]
# # -------- Binary Search --------
# def search_crop(crops, target):
#     low = 0
#     high = len(crops) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if crops[mid]["crop_id"] == target:
#             return crops[mid]
#         elif crops[mid]["crop_id"] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return None
# # -------- Sorting Functions --------
# def sort_by_moisture(crops):
#     return sorted(crops, key=lambda x: x["moisture"])
# def sort_by_yield(crops):
#     return sorted(crops, key=lambda x: x["yield"], reverse=True)
# # -------- Main Program --------
# print("Crop Records:")
# for c in crops:
#     print(c)
# # Sort by crop ID for searching
# crops.sort(key=lambda x: x["crop_id"])
# crop_id = int(input("\nEnter Crop ID to search: "))
# result = search_crop(crops, crop_id)
# if result:
#     print("\nCrop Found:")
#     print(result)
# else:
#     print("\nCrop not found")
# print("\nCrops Sorted by Soil Moisture Level:")
# for c in sort_by_moisture(crops):
#     print(c)
# print("\nCrops Sorted by Yield Estimate:")
# for c in sort_by_yield(crops):
#     print(c)


"""Task Description #8: Airport Flight Management System
An airport system stores flight information including flight ID, airline name, departure time, arrival time, and status. The system must:
1.	Search flight details using flight ID.
2.	Sort flights based on departure time or arrival time.
Student Task
•	Use AI to recommend algorithms.
•	Justify the algorithm selection.
•	Implement searching and sorting logic in Python."""


# # Flight records
# flights = [
#     {"flight_id": 101, "airline": "IndiGo", "departure": "10:30", "arrival": "12:45", "status": "On Time"},
#     {"flight_id": 105, "airline": "Air India", "departure": "09:15", "arrival": "11:30", "status": "Delayed"},
#     {"flight_id": 103, "airline": "SpiceJet", "departure": "14:00", "arrival": "16:10", "status": "On Time"},
#     {"flight_id": 102, "airline": "Vistara", "departure": "08:45", "arrival": "10:50", "status": "Boarding"},
#     {"flight_id": 104, "airline": "Akasa Air", "departure": "12:20", "arrival": "14:30", "status": "On Time"}
# ]
# # -------- Binary Search --------
# def search_flight(flights, target):
#     low = 0
#     high = len(flights) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if flights[mid]["flight_id"] == target:
#             return flights[mid]
#         elif flights[mid]["flight_id"] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return None
# # -------- Sorting Functions --------
# def sort_by_departure(flights):
#     return sorted(flights, key=lambda x: x["departure"])
# def sort_by_arrival(flights):
#     return sorted(flights, key=lambda x: x["arrival"])
# # -------- Main Program --------
# print("Flight Records:")
# for f in flights:
#     print(f)
# # Sort by flight ID for searching
# flights.sort(key=lambda x: x["flight_id"])
# flight_id = int(input("\nEnter Flight ID to search: "))
# result = search_flight(flights, flight_id)
# if result:
#     print("\nFlight Found:")
#     print(result)
# else:
#     print("\nFlight not found")
# print("\nFlights Sorted by Departure Time:")
# for f in sort_by_departure(flights):
#     print(f)
# print("\nFlights Sorted by Arrival Time:")
# for f in sort_by_arrival(flights):
#     print(f)
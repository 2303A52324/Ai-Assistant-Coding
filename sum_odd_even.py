def sum_odd_even(numbers):
    """
    Calculate the sum of odd and even numbers in a list.
    
    Args:
        numbers: List of integers
        
    Returns:
        tuple: (sum_of_odd, sum_of_even)
    """
    sum_odd = 0
    sum_even = 0
    
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    
    return sum_odd, sum_even


# Example usage
if __name__ == "__main__":
    # Example list
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Calculate sums
    odd_sum, even_sum = sum_odd_even(numbers)
    
    # Display results
    print(f"List: {numbers}")
    print(f"Sum of odd numbers: {odd_sum}")
    print(f"Sum of even numbers: {even_sum}")
    
    # Interactive version - uncomment to use
    # user_input = input("Enter numbers separated by spaces: ")
    # numbers = [int(x) for x in user_input.split()]
    # odd_sum, even_sum = sum_odd_even(numbers)
    # print(f"\nSum of odd numbers: {odd_sum}")
    # print(f"Sum of even numbers: {even_sum}")

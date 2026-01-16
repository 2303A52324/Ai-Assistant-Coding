"""
Area Calculator for Different Shapes
This program demonstrates how to calculate the area of various geometric shapes.
"""

import math


def calculate_circle_area(radius):
    """
    Calculate the area of a circle.
    
    Formula: Area = π × r²
    where π (pi) ≈ 3.14159 and r is the radius
    
    Args:
        radius (float): The radius of the circle
        
    Returns:
        float: The area of the circle
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2


def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Formula: Area = length × width
    
    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
        
    Returns:
        float: The area of the rectangle
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative")
    return length * width


def calculate_triangle_area(base, height):
    """
    Calculate the area of a triangle.
    
    Formula: Area = (1/2) × base × height
    
    Args:
        base (float): The base of the triangle
        height (float): The height of the triangle (perpendicular to base)
        
    Returns:
        float: The area of the triangle
    """
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative")
    return 0.5 * base * height


def calculate_square_area(side):
    """
    Calculate the area of a square.
    
    Formula: Area = side²
    (A square is a special rectangle where length = width)
    
    Args:
        side (float): The length of one side of the square
        
    Returns:
        float: The area of the square
    """
    if side < 0:
        raise ValueError("Side cannot be negative")
    return side ** 2


def calculate_trapezoid_area(base1, base2, height):
    """
    Calculate the area of a trapezoid.
    
    Formula: Area = (1/2) × (base1 + base2) × height
    
    Args:
        base1 (float): The length of the first parallel side
        base2 (float): The length of the second parallel side
        height (float): The height (distance between parallel sides)
        
    Returns:
        float: The area of the trapezoid
    """
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("Bases and height cannot be negative")
    return 0.5 * (base1 + base2) * height


def main():
    """
    Main function to demonstrate area calculations for different shapes.
    """
    print("=" * 60)
    print("AREA CALCULATOR FOR DIFFERENT SHAPES")
    print("=" * 60)
    print()
    
    # Circle example
    print("1. CIRCLE")
    print("-" * 60)
    radius = 5.0
    circle_area = calculate_circle_area(radius)
    print(f"   Radius: {radius} units")
    print(f"   Formula: Area = pi * r^2")
    print(f"   Calculation: pi * {radius}^2 = {math.pi:.2f} * {radius**2} = {circle_area:.2f} square units")
    print(f"   Result: {circle_area:.2f} square units")
    print()
    
    # Rectangle example
    print("2. RECTANGLE")
    print("-" * 60)
    length = 8.0
    width = 6.0
    rectangle_area = calculate_rectangle_area(length, width)
    print(f"   Length: {length} units, Width: {width} units")
    print(f"   Formula: Area = length * width")
    print(f"   Calculation: {length} * {width} = {rectangle_area} square units")
    print(f"   Result: {rectangle_area} square units")
    print()
    
    # Triangle example
    print("3. TRIANGLE")
    print("-" * 60)
    base = 10.0
    height = 7.0
    triangle_area = calculate_triangle_area(base, height)
    print(f"   Base: {base} units, Height: {height} units")
    print(f"   Formula: Area = (1/2) * base * height")
    print(f"   Calculation: 0.5 * {base} * {height} = {triangle_area} square units")
    print(f"   Result: {triangle_area} square units")
    print()
    
    # Square example
    print("4. SQUARE")
    print("-" * 60)
    side = 4.0
    square_area = calculate_square_area(side)
    print(f"   Side: {side} units")
    print(f"   Formula: Area = side^2")
    print(f"   Calculation: {side}^2 = {square_area} square units")
    print(f"   Result: {square_area} square units")
    print()
    
    # Trapezoid example
    print("5. TRAPEZOID")
    print("-" * 60)
    base1 = 6.0
    base2 = 10.0
    height_trap = 5.0
    trapezoid_area = calculate_trapezoid_area(base1, base2, height_trap)
    print(f"   Base 1: {base1} units, Base 2: {base2} units, Height: {height_trap} units")
    print(f"   Formula: Area = (1/2) * (base1 + base2) * height")
    print(f"   Calculation: 0.5 * ({base1} + {base2}) * {height_trap} = {trapezoid_area} square units")
    print(f"   Result: {trapezoid_area} square units")
    print()
    
    print("=" * 60)


if __name__ == "__main__":
    main()

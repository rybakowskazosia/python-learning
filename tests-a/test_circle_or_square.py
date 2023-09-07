# import math
# import pytest

# def test_calculate_circle_circumference():
#     radius = 5
#     circle_circumference = 2 * math.pi * radius
#     calculate_result = circle_circumference(radius)
#     assert calculate_result == circle_circumference

# def test_calculate_square_circumference():
#     square_area = 16
    
import math
import pytest

def calculate_circle_circumference(radius):
    return 2 * math.pi * radius

def calculate_square_circumference(square_area):
    return 4 * math.sqrt(square_area)

def compare_circumference(circle_circumference, square_circumference):
    return circle_circumference > square_circumference

# Testy funkcji obliczeniowych
def test_calculate_circle_circumference():
    radius = 5
    expected_result = 2 * math.pi * radius
    # Wywołaj funkcję calculate_circle_circumference w odpowiedni sposób
    calculated_result = calculate_circle_circumference(radius)
    assert calculated_result == expected_result

def test_calculate_square_circumference():
    square_area = 16
    expected_result = 16
    # Wywołaj funkcję calculate_square_circumference w odpowiedni sposób
    calculated_result = calculate_square_circumference(square_area)
    assert calculated_result == expected_result

# Test funkcji porównującej
def test_compare_circumferences():
    circle_circumference = 20
    square_circumference = 16
    expected_result = True  # Koło ma większy obwód niż kwadrat
    # Wywołaj funkcję compare_circumferences w odpowiedni sposób
    calculated_result = compare_circumference(circle_circumference, square_circumference)
    assert calculated_result == expected_result


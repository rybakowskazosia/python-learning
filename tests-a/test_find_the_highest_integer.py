import pytest

def find_the_highest(numbers_list):
    if len(numbers_list) == 1:
        return numbers_list[0]
    
    if len(numbers_list) == 0:
        return None
    
    mid = len(numbers_list) // 2
    left_half = numbers_list[:mid]
    right_half = numbers_list[mid:]

    max_left = find_the_highest(left_half)
    max_right = find_the_highest(right_half)

    return max(max_left, max_right)


def test_find_te_highest_single_number():
    numbers_list = [55]
    assert find_the_highest(numbers_list) == 55

def test_find_the_highest_in_empty_list():
    numbers_list = []
    assert find_the_highest(numbers_list) is None

def test_find_the_highest_multiple_numbers():
    numbers_list = [15, 9, 12, 18, 77, 3, 0]
    assert find_the_highest(numbers_list) == 77
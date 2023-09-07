import pytest

def convert_date(date):
    parts = date.split('/')

    if len(parts) != 3:
        return "Wrong date format!"
    
    month, day, year = parts

    new_date_format = f"{year}{day.zfill(2)}{month.zfill(2)}"
    return new_date_format

def test_convert_date_correct_format():
    date_input = "04/01/2003"
    expected_output = "20030104"
    assert convert_date(date_input) == expected_output


def test_convert_date_incorrect_format():
    date_input = "04/01"
    expected_output = "Wrong date format!"
    assert convert_date(date_input) == expected_output

def test_convert_date_empty_input():
    date_input = ""
    expected_output = "Wrong date format!"
    assert convert_date(date_input) == expected_output


# https://adventofcode.com/2023/day/1
import re


def get_digits(string):
    return [char for char in string if char.isdigit()]


def replace_string_digits(string):
    digit_mapping = {
        "one": "o1ne",
        "two": "t2wo",
        "three": "t3hree",
        "four": "4four",
        "five": "5five",
        "six": "6six",
        "seven": "7seven",
        "eight": "8eight",
        "nine": "9nine",
    }
    new_string = string
    for word, digit in digit_mapping.items():
        new_string = new_string.replace(word, str(digit))
    return new_string


with open("1.txt", "r") as f:
    print(f)
    lines = f.readlines()
    all_digits = []
    for line in lines:
        line = replace_string_digits(line)
        digits = get_digits(line)
        digit = int(f"{digits[0]}{digits[-1]}")
        print(line, digits, digit)
        all_digits.append(digit)
    print(sum(all_digits))

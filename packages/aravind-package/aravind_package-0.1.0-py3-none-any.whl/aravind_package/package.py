# string_utils/utils.py

def reverse_string(s):
    """Reverses a given string."""
    return s[::-1]

def to_uppercase(s):
    """Converts a string to uppercase."""
    return s.upper()

def count_vowels(s):
    """Counts the number of vowels in a string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

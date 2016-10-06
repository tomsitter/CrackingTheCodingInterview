#! /usr/bin/env python3
from copy import deepcopy
from collections import OrderedDict

def all_unique_chars(text):
    # 1.1 - Implement an algorithm to determine if a string has all unique characters. What if you
    # can not use additional data structures?

    # The set() function returns a list of unique elements within a string or list
    if len(text) != len(set(text)):
        return False
    else:
        return True


def reverse_cstring(text):

    # 1.2 - Write code to reverse a C-Style String. (C-String means that “abcd” is represented as
    # five characters, including the null character.)

    # I'm assuming the expected output for 'abcd\n' would be 'dcba\n'

    # Split the text into individual characters, excluding the last character
    chars = list(text[:-1])

    # Join the reversed list back into a string and append a newline
    return ''.join(reversed(chars)) + '\n'


def remove_duplicate_chars(text):
    # 1.3 - Remove duplicate characters from a string without a buffer or copying the array
    # I'm pretty sure my solution would not be accepted

    # Iterate over text and add each character to a ordered dict
    # Keys will stay in the same order and duplicate keys will overwrite existing ones
    unique = OrderedDict()
    for char in text:
        unique[char] = None
    return ''.join(unique.keys())


def is_anagram(a, b):
    # 1.4 - Test whether two strings are anagrams or not

    # First, make sure they're the same length
    if len(a) != len(b):
        return False

    # If they are the same length, make sure there is the same number of each character
    for char in set(a):
        if a.count(char) != b.count(char):
            return False

    return True


def replace_space(text, replacement='%20'):
    # 1.5 - replace all spaces with '%20'

    return text.replace(' ', replacement)


def rotate_square_matrix(matrix, inplace=False):
    # 1.6 -- Rotate an NxN matrix in space
    # Essentially every element at position n and m must go to m and n
    if not inplace:
        matrix = deepcopy(matrix)

    # Matrix is square so just need the size of one side
    size = len(matrix)

    for x in range(size):
        for y in range(x, size):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

    return matrix


def find_pos_of_value(matrix, value=0):
    """Return a list of (x,y) positions of zeros in a matrix"""
    num_cols = len(matrix)
    num_rows = len(matrix[0])

    zeros = []
    for x in range(num_cols):
        for y in range(num_rows):
            if matrix[x][y] == value:
                zeros.append((x, y))

    return zeros


def zero_row_col(matrix, positions, inplace=False):
    """Return a copy of the matrix with rows and columns zeroed for every
    position in the positions array"""

    # The operations will edit the passed in matrix unless a deep copy is made
    if not inplace:
        matrix = deepcopy(matrix)

    num_cols = len(matrix)
    num_rows = len(matrix[0])

    for x, y in positions:
        # Cancel out entire row is easy
        matrix[x] = [0] * num_cols
        # Little bit more work to loop through each column
        for pos in range(num_rows):
            matrix[pos][x] = 0

    return matrix


def zero_row_col_where_any_zeros(matrix):
    # 1.7 - Given an NxM matrix, set entire row and column to zero if any element is zero
    # Note! This is a destructive function -- it will edit the original matrix

    zeros = find_pos_of_value(matrix)

    # Return matrix
    return zero_row_col(matrix, zeros)


def is_rotation(original, rotated):
    # 1.8 Given two strings, determine if string b is a 'rotation' of string a using substr only once
    # 'waterbottle' is a rotation of 'erbottlewat'

    # First, make sure they have the same len and characters
    if len(original) != len(rotated):
        return False

    # If the second string was rotated, we can concatentate them and the original string should be present
    if original in rotated + rotated:
        return True
    else:
        return False

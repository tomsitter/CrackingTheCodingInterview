import chapter_1 as ch1


def test_unique_chars():
    # Q 1.1
    assert ch1.all_unique_chars('UNIQ CHARS') is True
    assert ch1.all_unique_chars('DUPLICATE CHARS') is False
    
    
def test_reverse_cstring():
    # Q 1.2
    assert ch1.reverse_cstring('abcd\n') == 'dcba\n'
    assert ch1.reverse_cstring('\n') == '\n'
    assert ch1.reverse_cstring('Hello World!\n') == '!dlroW olleH\n'


def test_remove_duplicate_chars():
    # Q 1.3
    assert ch1.remove_duplicate_chars('aabbcc') == 'abc'
    assert ch1.remove_duplicate_chars('') == ''
    assert ch1.remove_duplicate_chars('abc') == 'abc'
    assert ch1.remove_duplicate_chars('aa bb cc') == 'a bc'


def test_is_anagram():
    # Q 1.4
    assert ch1.is_anagram('banana', 'aannab') is True
    assert ch1.is_anagram('banana', 'apple') is False
    assert ch1.is_anagram('banana', '') is False
    assert ch1.is_anagram('', 'apple') is False
    assert ch1.is_anagram('', '') is True
    

def test_replace_space():
    # Q 1.5
    assert ch1.replace_space('Hello World!') == 'Hello%20World!'
    assert ch1.replace_space('NoSpaces') == 'NoSpaces'
    assert ch1.replace_space('Two  Spaces ') == 'Two%20%20Spaces%20'


def test_rotate_square_matrix():
    # Q 1.6
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    rotated_matrix = [[1, 4, 7],
                      [2, 5, 8],
                      [3, 6, 9]]
    assert ch1.rotate_square_matrix(matrix) == rotated_matrix


def test_zero_row_col_where_any_zeros():
    # Q 1.7
    matrix = [[1, 2, 3],
              [4, 0, 6],
              [7, 8, 9]]
    zeroed_matrix = [[1, 0, 3],
                     [0, 0, 0],
                     [7, 0, 9]]

    assert ch1.zero_row_col_where_any_zeros(matrix) == zeroed_matrix


def test_is_rotation():
    # Q 1.8
    assert ch1.is_rotation('waterbottle', 'erbottlewat') == True
    assert ch1.is_rotation('waterbottle', 'waterbottle') == True
    assert ch1.is_rotation('waterbottle', 'werbottlewat') == False

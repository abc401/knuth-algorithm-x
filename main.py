import logging as lg
from random import choice
from preprocessing import get_filtered_words, encode_words, encode_str


def different(num1: int, num2: int) -> bool:
    '''
    Return True if for every bit in num1 that is set to 1, the equivalent bit in num2 is not set to 1
    '''
    n = ~ (num1 & num2)
    return ((n+1) & n == 0) and (n != 0)


def get_letters(en_word: int) -> list[int]:
    letters = []
    for i in range(26):
        if (en_word >> i) & 1:
            letters.append(i)
    return letters


def get_rows(words: list[int]):
    rows = [list() for i in range(26)]
    for word in words:
        for i in range(26):
            if (word >> 25 - i) & 1:
                rows[i].append(word)
    return dict(enumerate(rows))

def get_counts(words: list[int]):
    counts = {}
    for word in words:
        for i in range(26):
            bit_value = (word >> 25 - i) & 1
            counts[i] = counts.get(i, 0) + bit_value
    return counts

# TODO: Not include rows in count if they are not required by knuth x in current iteration

def knuth_x(words: list[int], n_excluded: int = 0, n_exclude: int = 1, rows = None):
    sol_sets = []
    if rows is None:
        rows = get_rows(words)
    counts = get_counts(words)
    
    
    minimum = min(counts, key=lambda x: counts[x])
    while not rows[minimum]:
        n_excluded += 1
        if n_excluded >= n_exclude:
            return sol_sets
        counts.pop(minimum)
        minimum = min(counts, key=lambda x: counts[x])
            
    min_rows = rows[minimum]
    while min_rows:
        selected = choice(min_rows)
        min_rows.remove(selected)
        current_sol_set = [selected]
        letters = get_letters(selected)
        remaining_choices = {index: col for index, col in rows.items() if index not in letters}
        if not remaining_choices:
            sol_sets.append(current_sol_set)   # Found a valid solution
            continue
        
        sub_sols = knuth_x(remaining_choices, rows=remaining_choices)
        if sub_sols:
            sol_sets.extend([current_sol_set.extend(sub_sol) for sub_sol in sub_sols])
    return sol_sets


def main(filename: str):
    words = get_filtered_words(filename)
    print(knuth_x(words))


if __name__ == '__main__':
    lg.basicConfig(level=lg.INFO)
    words = ['abcde',
             'fghij',
             'klmno',
             'pqrst',
             'uvwxy',
             'zabcd',
             'efghi']
    # words = encode_words(words)
    # print(words)
    # print(least_ones_col(words))
    #p, 44040736 10488352 [5, 9, 11, 21, 23]
    print(encode_str('fjlvx'))
    main('wordlist.txt')

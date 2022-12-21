def read_words(filename: str):
    with open(filename) as file:
        return file.read().splitlines()

def primary_filter(words: list[str], keep_with_len: int = 5):
    return [w for w in words if len(w) == keep_with_len]

def encode_str(s: str):
    '''
    Convert s into an int with at most 26 bits where the nth bit represents whether the nth letter of the
    alphabets is present in the strings, where the value of n start from zero at the left side i.e. left most bit
    represents whether 'a' is present in the string and the right most bit represents whether 'z' is present in the string
    '''
    result = 0
    for c in s:
        result |= 1 << ord('z') - ord(c.lower())
    return result

def encode_words(words: list[str]):
    return [encode_str(word) for word in words]

def secondary_filter(words: list[int], keep_with_len: int = 5):
    return [word for word in words if word.bit_count() == keep_with_len]

def get_filtered_words(filename: str) -> list[int]:
    words = read_words(filename)
    words = primary_filter(words)
    words = encode_words(words)
    words = secondary_filter(words)
    return words

if __name__ == '__main__':
    a = encode_str('a')
    print(a >> 25)
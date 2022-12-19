import logging as lg

def read_words(filename: str):
    with open(filename) as file:
        return file.read().splitlines()

def filter_words(words: list[str], keep_with_len: int = 5):
    return [w for w in words if len(w) == keep_with_len]

def remove_anagrams(words: list[str]):
    return set([tuple(set(w)) for w in words])

def main():
    words = read_words(filename)
    words = filter_words(words)
    words = remove_anagrams(words)
    print(words)
    

if __name__ == '__main__':
    
    lg.basicConfig(level=lg.INFO)
    filename = 'wordlist.txt'
    main()
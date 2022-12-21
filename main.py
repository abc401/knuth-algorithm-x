import logging as lg
from preprocessing import get_filtered_words, read_words

def main(filename: str):
    nfwords = read_words(filename)
    words = get_filtered_words(filename)
    

if __name__ == '__main__':
    
    lg.basicConfig(level=lg.INFO)
    # print(bin(encode_str('a')))
    # print(encode_str('abcdef').bit_count())
    main('wordlist.txt')
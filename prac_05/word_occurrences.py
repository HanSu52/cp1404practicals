"""
Author: Han Su
Date: 24/04/2020
https://github.com/HanSu52/cp1404practicals
"""


def main():
    word_count = {}
    text = input("Text: ")
    words = text.split()
    for word in words:
        occurrences = word_count.get(word, 0)
        word_count[word] = occurrences + 1
    words = list(word_count.keys())
    words.sort()
    for word in words:
        max_length = max((len(word) for word in words))
        print("{:{}} : {}".format(word, max_length, word_count[word]))


if __name__ == '__main__':
    main()

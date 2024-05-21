from collections import Counter

def count_word_frequency(filename):
    with open(filename, 'r') as file:
        text = file.read()

    words = text.split()

    word_frequency = Counter(words)

    sorted_word_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

    for word, frequency in sorted_word_frequency:
        print(f'{word}: {frequency}')

filename = 'example.txt'
count_word_frequency(filename)
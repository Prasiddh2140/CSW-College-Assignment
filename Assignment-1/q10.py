import string


def count_word_frequencies():
    sentence = input("Enter a sentence: ")

    # 1. Remove punctuation using str.maketrans and str.translate
    translator = str.maketrans("", "", string.punctuation)
    clean_sentence = sentence.translate(translator)

    # 2. Convert to lowercase and split into words
    words = clean_sentence.lower().split()

    # 3. Count frequencies of each unique word
    frequency_map = {}
    for word in words:
        frequency_map[word] = frequency_map.get(word, 0) + 1

    # 4. Sort alphabetically by word
    sorted_words = sorted(frequency_map.items())

    # 5. Format and display output
    output = " ".join(f"{word}: {count}" for word, count in sorted_words)
    print(output)


if __name__ == "__main__":
    count_word_frequencies()
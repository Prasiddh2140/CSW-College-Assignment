import string

def process_sentence():
    # 1. Accept text and separator inputs from the user
    sentence = input("Enter a sentence: ")
    separator = input("Enter a custom separator: ")

    # 2. Strip punctuation marks from the sentence
    # string.punctuation includes !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    cleaned_sentence = ""
    for char in sentence:
        if char not in string.punctuation:
            cleaned_sentence += char
        else:
            cleaned_sentence += " " # Replace punctuation with space to preserve word separation

    # 3. Split into words and convert to lowercase for uniform sorting
    words = [word.lower() for word in cleaned_sentence.split()]

    # 4. Handle empty input edge case
    if not words:
        print("Error: No valid words found to sort.")
        return

    # 5. Sort the word list in reverse alphabetical order
    words.sort(reverse=True)

    # 6. Join the sorted elements with the custom delimiter
    result = separator.join(words)

    # 7. Output the final string
    print(f"Output: {result}")

if __name__ == "__main__":
    process_sentence()

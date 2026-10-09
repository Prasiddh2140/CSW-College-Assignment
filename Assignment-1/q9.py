def process_paragraph():
    text = input("Enter a paragraph: ")

    # 1. Remove extra whitespace and normalize spacing
    words = text.split()
    cleaned_text = " ".join(words)

    # 2. Convert to title case
    title_cased_text = cleaned_text.title()

    # 3. Count vowel occurrences using character codes (ASCII values)
    # Character codes: 'A'=65, 'E'=69, 'I'=73, 'O'=79, 'U'=85
    vowel_codes = [ord(char) for char in "AEIOU"]
    upper_text = title_cased_text.upper()

    vowel_counts = {
        chr(code): upper_text.count(chr(code))
        for code in vowel_codes
    }

    # Display outputs
    print(f"\nProcessed Text: {title_cased_text}")
    counts_str = ", ".join(f"{vowel}: {count}" for vowel, count in vowel_counts.items())
    print(f"Vowel Counts: {counts_str}")


if __name__ == "__main__":
    process_paragraph()
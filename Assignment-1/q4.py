import string

def is_palindrome_for_loop(text: str) -> bool:
    """
    Checks if a string is a palindrome using a single for-loop.
    Ignores only case differences. Keeps spaces and punctuation.
    """
    # Normalize to lowercase as requested
    cleaned_text = text.lower()
    length = len(cleaned_text)
    
    # Iterate through the first half of the string
    for i in range(length // 2):
        # Compare with the corresponding character from the end
        if cleaned_text[i] != cleaned_text[length - 1 - i]:
            return False
            
    return True


def is_palindrome_two_pointer(text: str) -> bool:
    """
    Checks if a string is a palindrome using the two-pointer technique.
    Ignores case, spaces, and punctuation to evaluate full sentences.
    """
    # Filter out spaces and punctuation, and convert to lowercase
    # string.punctuation covers characters like: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    cleaned_text = "".join(char.lower() for char in text if char.isalnum())
    
    # Initialize two pointers at opposite ends
    left = 0
    right = len(cleaned_text) - 1
    
    # Move pointers inward until they meet
    while left < right:
        if cleaned_text[left] != cleaned_text[right]:
            return False
        left += 1
        right -= 1
        
    return True


def main():
    # Accept string input from the user
    user_input = input("Enter a string: ")
    
    # Evaluate using both functions
    res_for_loop = "Palindrome" if is_palindrome_for_loop(user_input) else "Not a Palindrome"
    res_two_pointer = "Palindrome" if is_palindrome_two_pointer(user_input) else "Not a Palindrome"
    
    # Display the comparison results
    print(f"For-loop Check: {res_for_loop}, Two-pointer Check: {res_two_pointer}")


if __name__ == "__main__":
    main()

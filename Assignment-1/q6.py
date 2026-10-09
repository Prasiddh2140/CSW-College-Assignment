def encrypt_string(text: str) -> str:
    """
    Encrypts a string by:
    1. Reversing the input string.
    2. Swapping every adjacent pair of characters.
    """
    # Step 1: Reverse the string
    reversed_text = text[::-1]
    
    # Step 2: Swap adjacent pairs
    chars = list(reversed_text)
    for i in range(0, len(chars) - 1, 2):
        chars[i], chars[i+1] = chars[i+1], chars[i]
        
    return "".join(chars)


def decrypt_string(text: str) -> str:
    """
    Decrypts the string by reversing the encryption steps:
    1. Un-swapping adjacent pairs (swapping them again restores original position).
    2. Reversing the string back to its original order.
    """
    # Step 1: Swap adjacent pairs back
    chars = list(text)
    for i in range(0, len(chars) - 1, 2):
        chars[i], chars[i+1] = chars[i+1], chars[i]
        
    unswapped_text = "".join(chars)
    
    # Step 2: Reverse the string back
    return unswapped_text[::-1]


def main():
    # Read user input string
    user_input = input("Enter a string to encrypt: ")
    
    # Perform operations
    encrypted = encrypt_string(user_input)
    decrypted = decrypt_string(encrypted)
    
    # Display results
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")


if __name__ == "__main__":
    main()

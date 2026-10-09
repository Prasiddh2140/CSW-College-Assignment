def main():
    try:
        # 1. Read decimal input from the user
        decimal_input = int(input("Enter a decimal number: "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    # 2. Convert using built-in functions and slice off prefixes [2:]
    binary_str = bin(decimal_input)[2:]
    octal_str = oct(decimal_input)[2:]
    hex_str = hex(decimal_input)[2:].upper()  # Upper-cased for standard Hex formatting

    # 3. Count the number of digits in each representation
    bin_digits = len(binary_str)
    oct_digits = len(octal_str)
    hex_digits = len(hex_str)

    # 4. Reverse the conversion back to decimal using int(string, base)
    rev_binary = int(binary_str, 2)
    rev_octal = int(octal_str, 8)
    rev_hex = int(hex_str, 16)

    # 5. Display the results
    print("\n--- Base Conversion Results ---")
    print(f"Binary representation: {binary_str} (Digits: {bin_digits})")
    print(f"Octal representation: {octal_str} (Digits: {oct_digits})")
    print(f"Hexadecimal representation: {hex_str} (Digits: {hex_digits})")

    print("\n--- Reversion Verification ---")
    print(f"Reconverted Binary to Decimal: {rev_binary}")
    print(f"Reconverted Octal to Decimal: {rev_octal}")
    print(f"Reconverted Hexadecimal to Decimal: {rev_hex}")

    # Final logic check verification
    if rev_binary == rev_octal == rev_hex == decimal_input:
        print("\nVerification status: SUCCESS (All values match original input)")
    else:
        print("\nVerification status: FAILED")

if __name__ == "__main__":
    main()

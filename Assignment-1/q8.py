def validate_password(password: str):
    """
    Validates a password string against 5 corporate security criteria.
    Returns:
        - (True, []) if the password is valid.
        - (False, error_messages) if one or more conditions fail.
    """
    error_messages = []
    
    # 1. Length Check
    if len(password) < 8:
        error_messages.append("Must contain at least 8 characters.")
        
    # 2. Whitespace Check
    if " " in password:
        error_messages.append("Must not contain any whitespaces.")
        
    # Flags for structural character checks
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    allowed_special = set("!@#$%")
    
    # Analyze each character in the string
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in allowed_special:
            has_special = True

    # 3. Check collected flags and compile errors
    if not has_upper:
        error_messages.append("Must include at least one uppercase letter (A–Z).")
    if not has_lower:
        error_messages.append("Must include at least one lowercase letter (a–z).")
    if not has_digit:
        error_messages.append("Must include at least one digit (0–9).")
    if not has_special:
        error_messages.append("Must include at least one special character from the set (!@#$%).")
        
    # 4. Return boolean status alongside failure details
    if not error_messages:
        return True, []
    else:
        return False, error_messages


def main():
    # Prompt user for input
    user_password = input("Enter a password to validate: ")
    
    # Execute validation function
    is_valid, errors = validate_password(user_password)
    
    # Format and present output results
    if is_valid:
        print("\nResult: Valid Password")
    else:
        print("\nResult: Invalid Password")
        print("Violated Rules:")
        for error in errors:
            print(f" - {error}")


if __name__ == "__main__":
    main()

def change_case(orig_string: str) -> str:
    # Initialize an empty string to store the changed characters
    changed = ""
    
    # Iterate through each letter in the original string
    for letter in orig_string:
        # Check if the letter is lowercase
        if letter == letter.lower():
            # Convert the lowercase letter to uppercase and append to the changed string
            changed += letter.upper()
        else:
            # Convert the uppercase letter to lowercase and append to the changed string
            changed += letter.lower()
    
    return changed

def split_in_half(orig_string: str) -> tuple:
    # Return a tuple containing two halves of the original string
    return (orig_string[:len(orig_string) // 2], orig_string[len(orig_string) // 2:])

def remove_special_characters(orig_string: str) -> str:
    # List of allowed characters
    allowed_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
    
    # Initialize an empty string to store the cleaned characters
    cleaned_string = ""
    
    # Iterate through each character in the original string
    for char in orig_string:
        # Check if the character is in the allowed list
        if char in allowed_characters:
            # Append the character to the cleaned string
            cleaned_string += char
    
    return cleaned_string

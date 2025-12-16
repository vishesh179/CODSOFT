import random
import string

def get_password_length():
    while True:
        try:
            length = int(input("Enter password length (minimum 6): "))
            if length < 6:
                print("Password length should be at least 6.")
            else:
                return length
        except ValueError:
            print("Please enter a valid number.")

def choose_character_types():
    print("\nChoose character types:")
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    if not (use_letters or use_digits or use_symbols):
        print("At least one option must be selected. Letters enabled by default.")
        use_letters = True

    return use_letters, use_digits, use_symbols

def generate_password(length, letters, digits, symbols):
    characters = ""

    if letters:
        characters += string.ascii_letters
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    password = ""
    for i in range(length):
        password += random.choice(characters)

    return password

def main():
    print("===== PASSWORD GENERATOR =====")

    length = get_password_length()
    letters, digits, symbols = choose_character_types()

    password = generate_password(length, letters, digits, symbols)

    print("\nGenerated Password:")
    print(password)

    print("\nPassword generated successfully.")

if __name__ == "__main__":
    main()

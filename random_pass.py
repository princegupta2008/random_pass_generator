import random
import string


def generate_pass(length, use_letter=True, use_nums=True, use_symbols=True):
    characters = ""
    if use_letter:
        characters += string.ascii_letters
    if use_nums:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("Select at least one Character set from:- \nLetters OR Numbers OR Symbols")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_response():
    global length
    while True:
        try:
            length = int(input("Enter your Passwords length: "))
            if length < 6:
                print("Password length must be at least 6")
                continue
            break
        except ValueError:
            print("Please enter a valid number to continue.")

    print("Do you need to include")
    use_letter = input("Letters? (y/n): ").lower() == 'y'
    use_nums = input("Numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Symbols? (y/n): ").lower() == 'y'

    return length, use_letter, use_nums, use_symbols

if __name__ == "__main__":
    length, use_letter, use_nums, use_symbols = get_user_response()
    password = generate_pass(length, use_letter, use_nums, use_symbols)
    print("Your Generated Password is: ", password)
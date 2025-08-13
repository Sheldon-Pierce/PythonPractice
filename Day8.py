# def greet():
#     print("Welcome Alice!")
#     print("My name is Sheldon")
#     print("How are you today?")
#
# greet()
#
# def greet_with_name(name):
#     print(f"Welcome {name}!")
#     print(f"How are you today {name}?")
#
# greet_with_name("sheldon")

# def greet_with(name, location):
#     print(f"Welcome {name}!")
#     print(f"What is it like in {location}?")

# greet_with("sheldon", "Seattle")
# greet_with(location="Seattle", name="Sheldon")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        if letter not in alphabet:
            encrypted_text += letter
        else:
            letter_index = alphabet.index(letter)
            shifted_letter_index = letter_index + shift_amount
            if shifted_letter_index >= len(alphabet):
                overflow_index = shifted_letter_index - len(alphabet)
                encrypted_text += alphabet[overflow_index]
            else:
                encrypted_text += alphabet[shifted_letter_index]
    print(encrypted_text)

def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for letter in original_text:
        if letter not in alphabet:
            decrypted_text += letter
        else:
            letter_index = alphabet.index(letter)
            shifted_letter_index = letter_index - shift_amount
            if shifted_letter_index < 0:
                underflow_index = shifted_letter_index + len(alphabet)
                decrypted_text += alphabet[underflow_index]
            else:
                decrypted_text += alphabet[shifted_letter_index]
    print(decrypted_text)

def caesar(caesar_direction, original_text, shift_amount):
    if caesar_direction == 'encode':
        encrypt(original_text, shift_amount)
    else:
        decrypt(original_text, shift_amount)

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
    text = input("Type your message:\n ").lower()
    shift = int(input("Type 'shift' to shift letters:\n "))
    caesar(direction, text, shift)
    restart = input("Type 'yes' to continue..., Otherwise, type 'no").lower()
    if restart == 'no':
        should_continue = False
        print("Thank you for playing!")









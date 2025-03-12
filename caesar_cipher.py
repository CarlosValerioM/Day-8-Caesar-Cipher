#!/usr/bin/env python3
"""
caesar_cipher.py - A simple Caesar Cipher encryption and decryption script.

Author: Carlos Valerio (CarlosValerioM)
Date: 2025/03/12
License: MIT
Dependencies: None (built-in functions only)

Description:
This script encrypts or decrypts a given word using the Caesar Cipher method.
The user specifies:
1. Whether they want to encrypt or decrypt.
2. The word to process.
3. The shift value (how many letters to shift in the alphabet).

The script will output the transformed word.

Usage:
Run the script and follow the prompts:
    python caesar_cipher.py

Example:
    Would you like to encrypt or decrypt: encrypt
    What word would you like to encrypt: hello
    What's the shift number: 3
    Encrypted word: khoor
"""

def encrypt(word, shift, abc):
    """
    Encrypts a word using the Caesar Cipher method.

    :param word: The word to encrypt.
    :param shift: The number of letters to shift.
    :param abc: The alphabet list used for shifting.
    """
    new_word = ""  # Stores the encrypted word
    for letter in word:
        if letter in abc:  # Ensure the letter exists in the alphabet
            index = (abc.index(letter) + shift) % len(abc)  # Make shift circular
            new_word += abc[index]
        else:
            new_word += letter  # Keep non-alphabet characters unchanged
    print(f"Encrypted word: {new_word}")


def decrypt(word, shift, abc):
    """
    Decrypts a word using the Caesar Cipher method.

    :param word: The word to decrypt.
    :param shift: The number of letters to shift back.
    :param abc: The alphabet list used for shifting.
    """
    new_word = ""  # Stores the decrypted word
    for letter in word:
        if letter in abc:  # Ensure the letter exists in the alphabet
            index = (abc.index(letter) - shift) % len(abc)  # Make shift circular
            new_word += abc[index]
        else:
            new_word += letter  # Keep non-alphabet characters unchanged
    print(f"Decrypted word: {new_word}")


def main():
    """
    Main function that prompts the user for input and calls encryption or decryption.
    """
    abc = list("abcdefghijklmnopqrstuvwxyz")  # Alphabet used for shifting

    # Get user input
    action = input("Would you like to encrypt or decrypt: ").strip().lower()
    word = input("What word would you like to process: ").strip().lower()
    shift = int(input("What's the shift number: "))

    # Validate action and call the appropriate function
    if action == "encrypt":
        encrypt(word, shift, abc)
    elif action == "decrypt":
        decrypt(word, shift, abc)
    else:
        print("Invalid option. Please enter 'encrypt' or 'decrypt'.")


# Run the script only if executed directly (not imported as a module)
if __name__ == '__main__':
    main()
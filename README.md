# Day-8-Caesar-Cipher
Your Caesar Cipher - Difficulty: Easy

## CaesarCipher

### Author:
Carlos Valerio (CarlosValerioM)

### Date:
2025/03/12

### License:
MIT License

### Dependencies:
None (built-in functions only)

### Description:
`CaesarCipher.py` is a Python script that implements a basic Caesar Cipher encryption and decryption. It allows users to either encrypt or decrypt a message by shifting the letters of the alphabet by a specified number.

It prompts the user for the following inputs:
1. The action to perform (encrypt or decrypt).
2. The word to be encrypted or decrypted.
3. The shift number, which determines how many positions each letter in the word will move in the alphabet.

The script then displays the encrypted or decrypted word based on the action and shift provided.

### Usage:

1. Clone this repository:

```bash
git clone https://github.com/CarlosValerioM/Day-8-Caesar-Cipher.git
Navigate to the project directory:
```

```bash
cd Day-8-Caesar-Cipher
```
Run the script:

```bash
python CaesarCipher.py
```
The script will prompt you for input, and based on your responses, it will calculate the encrypted or decrypted word.

## Example Output:
Enter the action (encrypt or decrypt): encrypt

Enter the word to encrypt: hello

Enter the shift number: 3

Encrypted word: khoor

Enter the action (encrypt or decrypt): decrypt

Enter the word to decrypt: khoor

Enter the shift number: 3

Decrypted word: hello

## How it works:
The user inputs the action (encrypt or decrypt), the word to be processed, and the shift number.

In the encryption process, each letter in the word is shifted forward by the specified number of positions in the alphabet.

In the decryption process, each letter in the word is shifted backward by the specified number of positions.

The script uses a predefined alphabet to calculate the new letter for encryption or decryption.

## License:
This project is licensed under the MIT License.

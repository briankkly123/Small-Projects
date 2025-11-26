# Morse Code Translator

# Dictionary representing the Morse code chart
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ', ': '--..--',
    '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}

# ----------------- Encrypt function -----------------
def encrypt(message):
    message = message.upper()
    words = message.split(' ')  # split message into words
    cipher_words = []

    for word in words:
        letters = [MORSE_CODE_DICT[letter] for letter in word]
        cipher_words.append(' '.join(letters))  # one space between letters

    # two spaces between words
    return '  '.join(cipher_words)


# ----------------- Decrypt function -----------------
def decrypt(message):
    # Reverse lookup dictionary
    # m variable is Morse, L is letter
    REVERSE_MORSE = {m: l for l, m in MORSE_CODE_DICT.items()}
    
    message = message.strip()
    words = message.split('  ')  # two spaces separate words
    decoded_words = []
    
    for word in words:
        letters = word.split(' ')
        decoded_word = ''.join(REVERSE_MORSE[code] for code in letters if code)
        decoded_words.append(decoded_word)
    
    return ' '.join(decoded_words)  # UPPERCASE letters

# ----------------- CLI function -----------------
def main():
    choice = input("Do you want to encrypt or decrypt a message? (e/d): ").lower()
    
    if choice == 'e':
        message = input("Enter the message to encrypt: ")
        encrypted = encrypt(message)
        print(f"Encrypted Message: {encrypted}")
        
    elif choice == 'd':
        message = input("Enter the Morse code to decrypt (use spaces): ")
        decrypted = decrypt(message)
        print(f"Decrypted Message: {decrypted}")
        
    else:
        print("Invalid choice. Select 'e' to encrypt or 'd' to decrypt.")

if __name__ == '__main__':
    main()

def caesar_encrypt(text: str, shift: int) -> str:
    """Encrypts text using the Caesar cipher algorithm."""
    encrypted_text = []
    
    for char in text:
        if char.isalpha():
            # Determine base ASCII code ('A' = 65, 'a' = 97)
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around using modulo 26
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text.append(shifted_char)
        else:
            # Preserve spaces, digits, and punctuation
            encrypted_text.append(char)
            
    return "".join(encrypted_text)


def caesar_decrypt(ciphertext: str, shift: int) -> str:
    """Decrypts ciphertext using reverse shift logic."""
    return caesar_encrypt(ciphertext, -shift)


if __name__ == "__main__":
    plaintext = input("Enter message to encrypt: ")
    shift_key = int(input("Enter shift key (e.g., 3): "))
    
    # 1. Encrypt
    cipher = caesar_encrypt(plaintext, shift_key)
    print(f"\n[+] Encrypted Ciphertext: {cipher}")
    
    # 2. Decrypt
    decrypted = caesar_decrypt(cipher, shift_key)
    print(f"[+] Decrypted Output:    {decrypted}")
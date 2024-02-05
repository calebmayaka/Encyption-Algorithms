from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes

def generate_key():
    # Generate a random 16-byte (128-bit) key
    return get_random_bytes(16)

def pad_text(text):
    # Pad the text to be a multiple of 8 bytes
    pad_length = 8 - (len(text) % 8)
    return text + bytes([pad_length] * pad_length)

def encrypt(text, key):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    padded_text = pad_text(text)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text

def decrypt(encrypted_text, key):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    decrypted_text = cipher.decrypt(encrypted_text)
    # Remove padding
    return decrypted_text[:-decrypted_text[-1]]

def main():
    # Get user input for the plaintext
    plaintext = input("Enter the text to be encrypted: ").encode('utf-8')

    # Generate a random key
    key = generate_key()

    # Encrypt the user input
    encrypted_text = encrypt(plaintext, key)

    # Decrypt the encrypted text
    decrypted_text = decrypt(encrypted_text, key)

    # Display the results
    print(f"\nOriginal Text: {plaintext.decode('utf-8')}")
    print(f"Generated Key: {key.hex()}")
    print(f"Encrypted Text: {encrypted_text.hex()}")
    print(f"Decrypted Text: {decrypted_text.decode('utf-8')}")

if __name__ == "__main__":
    main()

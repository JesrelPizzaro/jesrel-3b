import streamlit as st

st.header("Welcome to XOR Cipher!")
st.write("What is your name")

txt_FNAME = st.text_input("FIRST NAME")
txt_LNAME = st.text_input("LAST NAME")

btn_submit = st.button("submit")

if btn_submit:
  st.write(f"Hello {txt_FNAME} {txt_LNAME}|")

def xor_encrypt(plaintext, key):
    """Encrypts plaintext using XOR cipher with the given key, printing bits involved."""

    ciphertext = bytearray()
    for i in range(len(plaintext)):
        plaintext_byte = plaintext[i]
        key_byte = key[i % len(key)]
        cipher_byte = plaintext_byte ^ key_byte
        ciphertext.append(cipher_byte)
        
        print(f"Plaintext byte: {bin(plaintext_byte)[2:]:>08} = {chr(plaintext_byte)}")
        print(f"Key byte:       {bin(key_byte)[2:]:>08} = {chr(key_byte)}")
        print(f"XOR result:     {bin(cipher_byte)[2:]:>08} = {chr(cipher_byte)}")
        print("--------------------")
    
    
    return ciphertext

def xor_decrypt(ciphertext, key):
    
    """Decrypts ciphertext using XOR cipher with the given key."""
    return xor_encrypt(ciphertext, key)   # XOR decryption is the same as encryption

# Example usage:
plaintext = bytes(input().encode())
key = bytes(input().encode())
    
if len(plaintext) >= len(key):
    if plaintext != key:
        cipher = xor_encrypt(plaintext, key)
        print(f"Ciphertext:", "".join([f"{chr(byte_val)}" for byte_val in cipher]))
        
        decrypt = xor_decrypt(cipher, key)
        print(f"Decrypted:", "".join([f"{chr(byte_va)}" for byte_va in decrypt]))
    else:
        print("Plaintext should not be equal to the key")
else:
    print("Plaintext length should be equal or greater than the length of key")

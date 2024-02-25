import streamlit as st

st.header("Welcome to Caesar Cipher!")
st.write("What is your name")

txt_FNAME = st.text_input("FIRST NAME")
txt_LNAME = st.text_input("LAST NAME")

btn_submit = st.button("submit")

if btn_submit:
  st.write(f"Hello {txt_FNAME} {txt_LNAME}|")

def encrypt_decrypt(text, shift_keys, ifdecrypt):
    """
    Encrypts a text using Caesar Cipher with a list of shift keys.
    Args:
        text: The text to encrypt.
        shift_keys: A list of integers representing the shift values for each character.
        ifdecrypt: flag if decrypt or encrypt
    Returns:
        A string containing the encrypted text if encrypt and plain text if decrypt
    """
    result = ""
    shift_keys_len = len(shift_keys)
        
    for i, char in enumerate(text):
        shift_key = shift_keys[i % shift_keys_len] if not ifdecrypt else -shift_keys[i % shift_keys_len]
    
        result += chr((ord(char) + shift_key - 32) % 94 +32)
        print(i, char, shift_keys[i % shift_keys_len], result[i])
        
    return result


# Example usage
text = input()
shift_keys = list(map(int, input().split()))
encrypted_text = encrypt_decrypt(text, shift_keys, False)
print("----------")
decrypted_text = encrypt_decrypt(encrypted_text, shift_keys, True)
print("----------")

print("Text:", text)
print("Shift keys:", " ".join(map(str, shift_keys)))
print("Cipher:", encrypted_text)
print("Decrypted text:", decrypted_text)


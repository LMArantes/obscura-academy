import streamlit as st
import pandas as pd

st.set_page_config(page_title="Vigenère Cipher", page_icon="🔑")

st.title("Vigenère Cipher")
st.write(
    "The Vigenère cipher is a method of encrypting alphabetic text using a series of different Caesar ciphers "
    "based on a keyword. It is more secure than the Caesar cipher because it uses multiple shifts based on the letters "
    "of the keyword, making frequency analysis harder."
)

key = st.text_input("Enter a keyword").lower()
text = st.text_input("Enter text to encrypt").lower()
if text and key:
    encrypted_text = ''
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            encrypted_text += chr(((ord(char) - 97 + shift) % 26) + 97)
            key_index += 1
        else:
            encrypted_text += char
    st.write(f"Encrypted text: {encrypted_text}")

st.write("### Vigenère Cipher Grid")
vigenere_csv_path = "assets/vigenere-grid.csv"  # Ensure the file is in the working directory
vigenere_df = pd.read_csv(vigenere_csv_path, index_col=0)
st.dataframe(vigenere_df)

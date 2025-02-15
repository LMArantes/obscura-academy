import streamlit as st

st.set_page_config(page_title="Substitution Cipher", page_icon="🔑")

st.title("Substitution Cipher")
st.write(
    "The Substitution cipher replaces each letter in the plaintext with another letter based on a fixed "
    "substitution rule. Unlike the Caesar cipher, where letters shift uniformly, the substitution cipher "
    "uses a key where each letter maps to a different letter or symbol."
)

st.write("### Create Your Own Substitution Cipher")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
substitution_key = {}

cols = st.columns(6)  # Creates 6 columns for input fields
for i, letter in enumerate(alphabet):
    with cols[i % 6]:  # Distribute inputs across columns
        substitution_key[letter] = st.text_input(f"{letter}", max_chars=1, key=letter)

text = st.text_input("Enter text to encrypt").upper()
if text:
    encrypted_text = ''.join(
        substitution_key[char] if char in substitution_key and substitution_key[char] else char for char in text
    )
    st.write(f"Encrypted text: {encrypted_text}")

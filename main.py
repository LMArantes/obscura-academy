import streamlit as st
import pandas as pd


def main():
    st.set_page_config(page_title="Obscura Academy", layout="wide")

    st.sidebar.title("Obscura Academy")
    page = st.sidebar.radio("Navigate",
                            ["Home", "Caesar Cipher", "Vigenère Cipher", "Substitution Cipher", "Challenges"])

    if page == "Home":
        home_page()
    elif page == "Caesar Cipher":
        caesar_cipher_page()
    elif page == "Vigenère Cipher":
        vigenere_cipher_page()
    elif page == "Substitution Cipher":
        substitution_cipher_page()
    elif page == "Challenges":
        challenges_page()


def home_page():
    st.title("Welcome to Obscura Academy")
    st.write("### About Obscura Academy")
    st.write(
        "Obscura Academy is a beginner-friendly platform designed to introduce users to the fundamentals of "
        "cryptography in an engaging and interactive way.")
    st.write(
        "Our goal is to help users develop problem-solving skills and an understanding of historical encryption "
        "techniques through hands-on lessons and challenges.")

    st.image("assets/obscura-academy-logo.png", use_container_width=True)

    st.write("### Why Learn Cryptography?")
    st.write("- Understand the basics of secure communication")
    st.write("- Develop logical thinking and problem-solving skills")
    st.write("- Gain hands-on experience with classic ciphers")

    st.write("### Available Lessons")
    st.write("1. Caesar Cipher")
    st.write("2. Vigenère Cipher")
    st.write("3. Substitution Cipher")

    st.write("### Coming Soon")
    st.write("- More advanced cryptographic techniques")
    st.write("- Interactive challenges and puzzles")
    st.write("- Community discussions and learning resources")


def caesar_cipher_page():
    st.title("Caesar Cipher")
    st.write("The Caesar cipher is one of the earliest and simplest known ciphers. It is a type of substitution "
             "cipher in which each letter in the plaintext is shifted a fixed number of places down or up the "
             "alphabet. The shift value, also known as the key, determines how many positions each letter is moved. "
             "For example, with a shift of 3, 'A' would be replaced by 'D', 'B' would become 'E', and so on.")
    st.write("This method is named after Julius Caesar, who reportedly used it to communicate with his generals in a "
             "way that obscured messages from enemies. However, due to its simplicity, it is easily broken using "
             "frequency analysis.")

    st.write("")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/CipherDisk2000.jpg/1920px-CipherDisk2000.jpg",
             caption="Caesar Cipher Disk", width=400)
    st.write("")

    st.write("To encrypt a message using the Caesar cipher, follow these steps:")
    st.write("1. Choose a shift value (key).")
    st.write("2. Replace each letter in the plaintext with the letter that appears [key] positions further along in "
             "the alphabet.")
    st.write("3. If the shift moves past 'Z', it wraps around to the beginning of the alphabet.")
    st.write("For example, with a shift of 3, the word 'HELLO' would be encrypted as 'KHOOR'."
             "away.")
    shift = st.slider("Choose shift amount", 1, 25, 3)
    text = st.text_input("Enter text to encrypt")
    if text:
        encrypted_text = ''.join(
            chr(((ord(char) - 97 + shift) % 26) + 97) if char.isalpha() else char for char in text.lower())
        st.write(f"Encrypted text: {encrypted_text}")


def vigenere_cipher_page():
    st.title("Vigenère Cipher")
    st.write(
        "The Vigenère cipher is a method of encrypting alphabetic text using a series of different Caesar ciphers "
        "based on a keyword.")
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


def substitution_cipher_page():
    st.title("Substitution Cipher")
    st.write(
        "The Substitution cipher replaces each letter in the plaintext with another letter based on a fixed "
        "substitution rule.")

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
            substitution_key[char] if char in substitution_key and substitution_key[char] else char for char in text)
        st.write(f"Encrypted text: {encrypted_text}")


def challenges_page():
    st.title("Challenges")
    st.write("Coming soon!")


if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Vigenère Cipher", page_icon="🔑")

st.title("Vigenère Cipher")

st.image("assets/vigenere.jpg", width=300)

st.write(
    "The Vigenère cipher is a method of encrypting alphabetic text using a series of different Caesar ciphers "
    "based on a keyword. It is more secure than the Caesar cipher because it uses multiple shifts based on the letters "
    "of the keyword, making frequency analysis harder."
)

st.markdown("### How Does the Vigenère Cipher Work?")
st.write(
    "Unlike the Caesar cipher, which shifts letters by a fixed amount, the Vigenère cipher shifts each letter "
    "differently based on a repeating **keyword**. This keyword determines the shift for each letter in the plaintext."
)
st.write("**Encryption Steps:**")
st.write("1. Choose a keyword (e.g., `KEY`).")
st.write("2. Repeat the keyword until it matches the length of the message.")
st.write("3. Use the **Vigenère Table** to find the encrypted letter.")
st.write("4. Decrypt by reversing the lookup process.")

st.markdown("---")  # Divider

st.write("### Vigenère Cipher Grid")
st.write(
    "The **Vigenère Grid** is a 26x26 table where each row represents a Caesar shift for a given letter. "
    "The **first row** is the normal alphabet, and each subsequent row shifts the letters by one position."
)
st.write("To encrypt a letter, find the row corresponding to the **keyword letter** and the column corresponding to "
         "the **plaintext letter**. The intersection gives the encrypted letter.")

st.write("### Example:")
st.write("**Plaintext:** `HELLO`")
st.write("**Keyword:** `KEYKE` (repeated to match the length of `HELLO`)")
st.write("**Encryption Process:**")
st.write("  - `H` (row `K`) → `R`")
st.write("  - `E` (row `E`) → `I`")
st.write("  - `L` (row `Y`) → `J`")
st.write("  - `L` (row `K`) → `V`")
st.write("  - `O` (row `E`) → `S`")
st.write("**Encrypted Message:** `RIJVS`")

vigenere_csv_path = "assets/vigenere-grid.csv"  # Ensure the file is in the working directory
vigenere_df = pd.read_csv(vigenere_csv_path, index_col=0)
st.dataframe(vigenere_df)

st.write("### Encoder:")

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


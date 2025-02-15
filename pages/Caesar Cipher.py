import streamlit as st

st.set_page_config(page_title="Caesar Cipher", page_icon="🔑")

st.title("Caesar Cipher")
st.write("The Caesar cipher is one of the earliest and simplest known ciphers. It is a type of substitution "
         "cipher in which each letter in the plaintext is shifted a fixed number of places down or up the "
         "alphabet. The shift value, also known as the key, determines how many positions each letter is moved. "
         "For example, with a shift of 3, 'A' would be replaced by 'D', 'B' would become 'E', and so on.")

st.write("This method is named after Julius Caesar, who reportedly used it to communicate with his generals in a "
         "way that obscured messages from enemies. However, due to its simplicity, it is easily broken using "
         "frequency analysis.")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/CipherDisk2000.jpg/1920px-CipherDisk2000.jpg", caption="Caesar Cipher Disk", width=400)

st.write("To encrypt a message using the Caesar cipher, follow these steps:")
st.write("1. Choose a shift value (key).")
st.write("2. Replace each letter in the plaintext with the letter that appears [key] positions further along in "
         "the alphabet.")
st.write("3. If the shift moves past 'Z', it wraps around to the beginning of the alphabet.")
st.write("For example, with a shift of 3, the word 'HELLO' would be encrypted as 'KHOOR'.")

shift = st.slider("Choose shift amount", 1, 25, 3)
text = st.text_input("Enter text to encrypt")
if text:
    encrypted_text = ''.join(
        chr(((ord(char) - 97 + shift) % 26) + 97) if char.isalpha() else char for char in text.lower()
    )
    st.write(f"Encrypted text: {encrypted_text}")

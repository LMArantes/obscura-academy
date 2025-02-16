import streamlit as st

st.set_page_config(page_title="Basic Python for Cryptography", layout="wide")

st.title("Basic Python for Cryptography")

st.subheader("Why Learn Python for Cryptography?")
st.write(
    "Python is one of the most **beginner-friendly programming languages**, widely used for **cybersecurity, "
    "cryptography, and data analysis**. It allows you to quickly **write and test encryption algorithms**, "
    "making it ideal for solving puzzles, encrypting messages, and analyzing ciphers."
)

st.markdown("### **Getting Started with Python**")
st.write(
    "Python uses a simple syntax that makes it easy to read and write code. Below are some fundamental concepts you "
    "need to know before we start encrypting messages."
)

st.subheader("Python Syntax: Variables and Data Types")
st.write(
    "A **variable** is used to store information that can be reused later. In Python, we don’t need to declare "
    "variable types explicitly; Python automatically understands the type."
)

python_code = """ 
# Defining variables
message = "HELLO"  # A string (text)
shift = 3  # An integer (number)
pi = 3.14159  # A floating-point number (decimal)
is_encrypted = False  # A boolean (True/False)

# Displaying variables
print(message)
print(shift)
print(pi)
print(is_encrypted)
"""
st.code(python_code, language="python")

st.markdown(
    """
### **Common Data Types in Python**
| **Type** | **Example** | **Description** |
|----------|------------|----------------|
| String (`str`) | `"HELLO"` | A sequence of characters. |
| Integer (`int`) | `3`, `100` | Whole numbers. |
| Float (`float`) | `3.14`, `2.718` | Decimal numbers. |
| Boolean (`bool`) | `True`, `False` | Represents truth values. |
"""
)

st.subheader("Conditional Statements (if/else)")
st.write(
    "Conditional statements allow programs to make decisions. Below is an example checking if a message contains a "
    "certain word."
)

if_else_code = """ 
message = "This is a secret message"

if "secret" in message:
    print("🔒 This message is encrypted!")
else:
    print("✅ This message is safe.")
"""
st.code(if_else_code, language="python")

st.subheader("Loops in Python")
st.write(
    "Loops allow us to **repeat actions multiple times**. The `for` loop is useful when we want to **iterate through "
    "text letter by letter**, which is essential for encryption."
)

loop_code = """ 
message = "HELLO"
for letter in message:
    print("Current Letter:", letter)
"""
st.code(loop_code, language="python")

st.subheader("Functions in Python")
st.write(
    "A **function** is a reusable block of code that performs a specific task. "
    "For example, we can create a function to encrypt text."
)

function_code = """ 
def encrypt_message(text):
    encrypted = text[::-1]  # Reverse the text as a simple encryption
    return encrypted

# Encrypting the word "PYTHON"
result = encrypt_message("PYTHON")
print("Encrypted Message:", result)
"""
st.code(function_code, language="python")

st.subheader("The Caesar Cipher")
st.write(
    "The **Caesar cipher** is one of the oldest encryption techniques. It shifts each letter in a message by a fixed "
    "number of places. For example, with a shift of **3**, the letter **A** becomes **D**, **B** becomes **E**, "
    "and so on."
)

st.write("### **Try it Yourself: Encrypt a Message!**")
st.write(
    "Enter a message and choose a shift number. The program will encrypt it using the **Caesar cipher**."
)

# User Input for Encryption
user_message = st.text_input("Enter your message:")
user_shift = st.slider("Choose shift value:", 1, 25, 3)


# Function to Encrypt User Input
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            elif char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            result += chr(shifted)
        else:
            result += char
    return result


if user_message:
    encrypted_message = caesar_cipher(user_message, user_shift)
    st.write(f"🔒 **Encrypted Message:** {encrypted_message}")

st.subheader("Challenge: Decrypt This Message!")
st.write(
    "Below is an encrypted message using the **Caesar cipher**. Try to figure out the original text!"
)

# Predefined challenge message
challenge_message = "WKLV LV D VHFUHW PHVVDJH"
st.code(challenge_message, language="text")

user_attempt = st.text_input("Your decryption attempt:")

if user_attempt:
    if user_attempt.upper() == "THIS IS A SECRET MESSAGE":
        st.success("✅ Correct! You decrypted the message successfully.")
    else:
        st.error("❌ Incorrect. Try again!")

st.subheader("What's Next?")
st.write(
    "Now that you understand Python syntax and the **Caesar cipher**, try to explore more **complex ciphers** like "
    "the **Vigenère cipher**, which uses a **keyword** to encrypt text, and coding an encrypter."
)

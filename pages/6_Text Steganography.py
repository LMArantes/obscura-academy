import streamlit as st

st.set_page_config(page_title="Text Steganography", layout="wide")

st.image("assets/encryption.png")

st.title("Text Steganography")
st.markdown("## *Hiding Messages in Plain Sight*")
st.markdown("---")

st.subheader("What is Text Steganography?")
st.write(
    "Text steganography is the technique of **concealing information within text** using formatting tricks, "
    "special characters, and invisible symbols. Unlike cryptography, which transforms the content of a message, "
    "steganography hides the existence of a message altogether."
)

st.subheader("Historical Background")
st.write(
    "Text-based steganography has been used throughout history for covert communication. Methods such as **invisible "
    "ink, acrostics, and null ciphers** were commonly used to encode messages in written documents. In the digital "
    "age, these techniques have evolved into advanced methods that use **invisible characters** and text formatting "
    "to hide messages in plain sight."
)

st.subheader("Modern Techniques in Text Steganography")

st.markdown(
    """
### **1. Whitespace Encoding**
Whitespace characters (such as spaces and tabs) can be manipulated to encode information. Since these characters are typically ignored by readers, they serve as an effective way to embed hidden data.

**Example:**  
A message may be encoded using **spaces** and **tabs** in a specific pattern:

> Hello ‎ World ‎ ‎  this ‎ is    an ‎ ‎ ‎ ‎ ‎ example.

The spacing between words or lines could encode binary data.

---

### **2. Zero-Width Characters**
Some Unicode characters are **invisible** to humans but can still be detected by computers. These include:
- **Zero-width space ( `​` )**
- **Zero-width non-joiner ( `‌` )**
- **Zero-width joiner ( `‍` )**

By inserting these characters within a text, a hidden message can be embedded without affecting its appearance.

**Example:**  
A normal-looking message such as:

> Meet me at the park.

Might actually contain hidden information if copied and analyzed.

---

### **3. Formatting-Based Steganography**
Certain text properties, such as **font size, bold/italic styling, or even punctuation**, can be used to conceal messages.

**Example:**
A sequence of capitalized words in a document may form a hidden message:

> The Enemy Strikes Tonight
    
This might indicate an acronym **T.E.S.T.** used for further decoding.

---

### **4. Character Substitution with Similar-Looking Unicode Characters**
Some Unicode characters **look identical** to standard letters but have different underlying values. This technique can be used to embed hidden text.

**Example:**
- **𝐓𝐡𝐢𝐬** **𝐥𝐨𝐨𝐤𝐬** **𝐧𝐨𝐫𝐦𝐚𝐥** (but uses bold Unicode letters)
- **𝚃𝚑𝚒𝚜 𝚕𝚘𝚘𝚔𝚜 𝚗𝚘𝚛𝚖𝚊𝚕** (but uses mathematical monospace)

This is difficult to detect without careful examination.

---
"""
)

st.subheader("Applications of Text Steganography")
st.write(
    "Text steganography is widely used in various fields, including cybersecurity, digital watermarking, and covert "
    "communication."
)

st.markdown(
    """
### **Common Uses:**
- **Covert Communication**: Used to send secret messages without attracting attention.
- **Digital Watermarking**: Protects ownership rights in text-based documents.
- **Cybersecurity**: Helps forensic investigators detect hidden malicious instructions.
"""
)

st.subheader("Text Steganography Challenge")
st.write(
    "Below is a message that appears normal, but it contains a hidden word. Can you find and reveal the secret message?"
)

# Hidden message using capitalized Characters (hidden word: "START")
hidden_message = "thiS sentence conTains A secRet message. can you find iT?"

st.code(hidden_message, language="plaintext")

user_attempt = st.text_input("Enter the hidden message you found:")

if user_attempt:
    if user_attempt.strip().upper() == "START":
        st.success("Correct! You have successfully uncovered the hidden message.")
    else:
        st.error("Incorrect. Try again or check the hint below.")

# Tip (Spoiler) for users who need help
with st.expander("💡 Click for a Hint"):
    st.write("Try checking the capitalized characters.")

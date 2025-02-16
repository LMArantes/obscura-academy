import streamlit as st

st.set_page_config(page_title="Introduction to Cryptography", layout="wide")

st.image("assets/cryptography.png")

st.title("Introduction to Basic Cryptography")

st.subheader("What is Cryptography?")
st.write(
    "Cryptography is the art and science of securing information by converting it into a format that can only be "
    "understood by intended recipients. It has been used for centuries to protect secrets, ensure privacy, and enable "
    "secure communication between individuals, organizations, and even nations."
)

st.subheader("A Brief History of Cryptography")
st.write(
    "The need for secrecy in communication dates back to ancient times. Some of the earliest cryptographic techniques "
    "were simple substitution ciphers used by military leaders and diplomats to protect sensitive information."
)

st.markdown(
    """
#### **Early Cryptographic Techniques**
- **Caesar Cipher (100 BCE)**: Named after Julius Caesar, this method shifts letters of the alphabet by a fixed number of places.
- **Scytale Cipher (Ancient Greece, 5th Century BCE)**: A transposition method used by the Spartans, involving wrapping a strip of parchment around a cylinder.
- **Vigenère Cipher (1500s CE)**: Considered unbreakable for centuries, this polyalphabetic cipher uses a keyword to shift letters.
- **Enigma Machine (World War II)**: A sophisticated electromechanical encryption device used by Nazi Germany, famously cracked by Alan Turing and his team at Bletchley Park.
"""
)

st.image("assets/enigma.jpg", caption="Enigma Machine", width=350)

st.subheader("Cryptography in the Modern World")
st.write(
    "In today's digital age, cryptography is no longer just about keeping military secrets. It is the backbone of "
    "modern cybersecurity, enabling **secure communication, financial transactions, and data protection**. From "
    "end-to-end encrypted messaging apps to online banking security, cryptographic techniques protect billions of "
    "users worldwide."
)

st.markdown(
    """
#### **Applications of Cryptography Today**
- **Cybersecurity**: Protects online communications, passwords, and sensitive information.
- **Blockchain & Cryptocurrency**: Secures Bitcoin, Ethereum, and other decentralized financial systems.
- **Secure Communications**: Enables encrypted messaging apps like **Signal, WhatsApp, and Telegram**.
- **Digital Signatures**: Ensures authenticity and prevents fraud in legal documents and software updates.
- **National Security**: Governments use advanced cryptography for classified intelligence and secure communications.
"""
)

st.subheader("Why Learn Cryptography?")
st.write(
    "Understanding cryptography is essential for anyone interested in **cybersecurity, hacking, digital privacy, "
    "or even Alternate Reality Games (ARGs)**."
    "Whether you're cracking puzzles, protecting personal data, or developing secure software, cryptographic skills "
    "are invaluable."
)

st.subheader("Start Learning!")
st.write(
    "Explore the lessons in **Obscura Academy** to begin your journey. "
    "Start with the classic **Caesar Cipher**, then advance to more complex methods like **Vigenère and modern "
    "cryptographic systems**!"
)

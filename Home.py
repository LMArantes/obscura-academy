import streamlit as st

st.set_page_config(page_title="Obscura Academy", layout="wide")

st.image("assets/obscura-academy-image-logo.png", width=250)

st.title("Obscura Academy")
st.write(
    "Welcome to **Obscura Academy**, an interactive learning platform where you unravel the mysteries of "
    "encryption, coding, and secret messages. Inspired by **ARGs (Alternate Reality Games)**, digital forensics, "
    "and cryptographic challenges, this academy is designed for those fascinated by puzzles, hidden messages, "
    "and the art of secrecy."
)

# Interactive Introduction
st.subheader("What is Obscura Academy?")
st.write(
    "In a world filled with hidden codes, encrypted messages, and digital breadcrumbs, **Obscura Academy** is your "
    "gateway "
    "to learning the art of cryptography and codebreaking. Whether you're an aspiring **detective, hacker, "
    "ARG player, or "
    "just someone who loves solving puzzles**, this academy will equip you with essential skills in **encryption, "
    "decryption, "
    "and pattern recognition**."
)

# Interactive Question (Encourage Exploration)
st.subheader(" Are You Ready to Begin?")
user_choice = st.radio(
    "Choose your path:",
    ["🔑 Yes, let's unlock the secrets!", "🤔 I want to know more first"]
)

if user_choice == "🔑 Yes, let's unlock the secrets!":
    st.write("Excellent! Use the **sidebar navigation** to explore different ciphers and take on challenges.")
    st.write("Your journey into the **world of cryptography and hidden messages begins now!**")
elif user_choice == "🤔 I want to know more first":
    st.write(
        "**Obscura Academy is not just about learning, but about solving real cryptographic puzzles.**\n"
        "If you've ever been intrigued by mysterious ciphers in ARGs, coded messages in movies, or wanted to understand"
        "how digital security works, this is the place to start."
    )

# Learning Paths
st.subheader("What Will You Learn?")
st.write(
    "- **Caesar Cipher** - Learn the secrets of Julius Caesar's ancient encryption technique.\n"
    "- **Vigenère Cipher** - A cipher so complex it remained unbroken for centuries.\n"
    "- **Substitution Cipher** - Create your own secret alphabet and encrypt messages.\n"
    "- **Challenges & ARG Puzzles** - Solve cryptic challenges inspired by real ARG mysteries."
)

# ARG & Internet Mystery Connection
st.subheader("Why is Cryptography Important in ARGs?")
st.write(
    "Many famous **ARGs (Alternate Reality Games)** use cryptography to hide messages, unlock new levels, "
    "or lead players down deep rabbit holes. Games like **Cicada 3301, The Wyoming Incident, and mysterious internet "
    "puzzles**"
    "have all used cryptographic techniques like the **Caesar and Vigenère ciphers** to test players' skills. "
    "By learning these techniques, you’ll be prepared to tackle real internet mysteries!"
)

# Encourage Users to Explore
st.subheader("Ready to Begin?")
st.write(
    "Navigate using the **sidebar** and start decrypting messages! "
    "Your first challenge is waiting..."
)

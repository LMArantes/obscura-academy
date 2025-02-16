import streamlit as st

st.set_page_config(page_title="Obscura Academy", layout="wide")

st.image("assets/obscura-academy-image-logo.png", width=250)

st.title("Obscura Academy")
st.write(
    "Welcome to **Obscura Academy**, an interactive learning platform where you **unravel the mysteries** of "
    "**encryption, steganography, coding, and digital forensics**. "
    "This academy is designed for those fascinated by **puzzles, hidden messages, and the art of secrecy**, "
    "taking inspiration from **ARGs (Alternate Reality Games)**, digital forensics, and real-world cryptographic "
    "challenges."
)

st.markdown("---")

# Introduction Section
st.subheader("What is Obscura Academy?")
st.write(
    "In a world filled with hidden codes, encrypted messages, and digital breadcrumbs, **Obscura Academy** is your "
    "gateway to learning the art of cryptography, codebreaking, and **information security**. "
    "Whether you're an aspiring **detective, hacker, ARG player, or cybersecurity enthusiast**, this academy "
    "will equip you with essential skills in **encryption, steganography, and file analysis**."
)

# Learning Paths
st.subheader("What Will You Learn?")
st.write(
    "- **Cryptography Fundamentals** – Learn how ancient and modern encryption methods work.\n"
    "- **Classic Ciphers (Caesar, Vigenère, and more!)** – Crack historical encryption techniques.\n"
    "- **Steganography** – Hide and reveal messages in images and audio files.\n"
    "- **File Analysis & Digital Forensics** – Extract metadata and analyze file structures.\n"
    "- **Basic Coding for Cryptography** – Use Python to encrypt, decrypt, and analyze data.\n"
    "- **ARG-Inspired Challenges** – Solve cryptic puzzles inspired by real internet mysteries."
)

# ARG & Internet Mystery Connection
st.subheader("Why is Cryptography Important in ARGs?")
st.write(
    "Many famous **ARGs (Alternate Reality Games)** use cryptography, hidden clues, and digital forensics "
    "to create complex puzzles. Games like **Cicada 3301, The Wyoming Incident, and mysterious internet "
    "puzzles** have all used cryptographic techniques such as **Caesar ciphers, Vigenère encryption, "
    "and steganography** to challenge players. By learning these skills, **you’ll be prepared to tackle real internet "
    "mysteries**!"
)

st.write("")

st.image("assets/Cicada_3301_logo.jpg", width=250, caption="Cicada 3301")

st.write("")

# Interactive Question: Choose Your Learning Path
st.subheader("Choose Your Learning Path")
user_choice = st.radio(
    "Where would you like to begin?",
    [
        "Cryptography – Learn encryption, ciphers, and how to decode secrets.",
        "Steganography – Hide and extract messages from images and audio.",
        "Coding – Use Python to encrypt, decrypt, and analyze files."
    ]
)

if user_choice == "Cryptography – Learn encryption, ciphers, and how to decode secrets.":
    st.write("**Welcome to the world of Cryptography!** Use the **sidebar navigation** to start exploring ciphers, "
             "learn about encryption techniques, and test your decryption skills.")
elif user_choice == "Steganography – Hide and extract messages from images and audio.":
    st.write("**Discover the secrets of Steganography!** Learn how to **hide information in images and audio files**, "
             "and explore real-world techniques used in digital forensics.")
elif user_choice == "Coding – Use Python to encrypt, decrypt, and analyze files.":
    st.write("**Jump into the world of Programming for Cryptography!** Explore how Python can be used to **encrypt, "
             "decrypt, and analyze data**, and take on coding challenges designed for beginners.")


# Encourage Users to Explore
st.subheader("Ready to Begin?")
st.write(
    "Navigate using the **sidebar** and start decrypting messages, hiding text in images, or analyzing files! "
    "Your first challenge is waiting..."
)

import streamlit as st

st.set_page_config(page_title="Introduction to Steganography", layout="wide")

st.image("assets/lock.png")

st.title("Introduction to Steganography")
st.markdown("## *The Art of Hidden Messages*")

st.markdown("---")

st.subheader("What is Steganography?")
st.write(
    "Steganography is the practice of concealing information within other non-secret data to make it "
    "invisible to unintended recipients. Unlike cryptography, which encrypts data to obscure its meaning, "
    "steganography focuses on making the existence of a message undetectable. Historically, this technique "
    "has been used for covert communication, intelligence operations, and digital security."
)

st.image("assets/steganography.png", caption="The same image viewed by white, blue, green, and red lights reveals "
                                             "different numbers.")

st.subheader("A Brief History of Steganography")
st.write(
    "The concept of steganography dates back to ancient civilizations. Throughout history, individuals and "
    "organizations have developed techniques to conceal messages in various media."
)

st.markdown(
    """
### Historical Steganographic Methods:
- **Ancient Greece (5th Century BCE):** Messages were tattooed onto a messenger's shaved scalp and concealed once the hair grew back.
- **Invisible Ink (16th–20th Century):** Chemicals such as lemon juice were used to write messages that only became visible under heat or UV light.
- **Microdots (World War II):** Entire documents were reduced to microscopic images and embedded within seemingly ordinary text or images.
- **Null Ciphers (Early 20th Century):** Messages were hidden in plain text by using specific word patterns or letter sequences.
"""
)

st.image("assets/Chart_in_the_hand_of_Dr_John_Dee._Steganographiae.png", caption="A chart from Johannes Trithemius's "
                                                                                 "Steganographia copied by Dr. John "
                                                                                 "Dee in 1591.", width=350)

st.subheader("Modern Steganographic Techniques")
st.write(
    "After the advent of digital technology, steganography has evolved into the embedding of hidden information "
    "within digital media such as images, audio, and video files. These modern techniques are used in a variety of "
    "applications, from cybersecurity to digital rights management."
)

st.markdown(
    """
### Contemporary Applications:
- **Image Steganography:** Information is embedded within an image’s pixel values, often using the Least Significant Bit (LSB) technique.
- **Audio Steganography:** Messages are concealed within audio signals, making them imperceptible to the human ear.
- **Video Steganography:** Data is embedded in video frames, ensuring it remains undetectable during playback.
- **Text Steganography:** Hidden messages are placed within text documents through invisible characters, whitespace manipulation, or specific formatting.
- **Network Steganography:** Data is covertly transferred within network traffic, making it difficult to detect during transmission.
"""
)

st.subheader("The Importance of Steganography in Cybersecurity")
st.write(
    "Steganography plays a significant role in both security and privacy. While it is commonly used for legitimate "
    "purposes,"
    "such as digital watermarking and data protection, it can also be exploited for malicious intent, including "
    "concealing malware"
    "or transmitting illicit information. Understanding steganographic methods is essential for cybersecurity "
    "professionals, forensic analysts,"
    "and individuals concerned with data privacy."
)

st.markdown(
    """
### Practical Uses of Steganography:
- **Covert Communication:** Enables secure messaging without raising suspicion.
- **Digital Watermarking:** Protects intellectual property by embedding ownership details in digital media.
- **Forensic Investigation:** Helps detect hidden information in cybercrime investigations.
- **Data Protection:** Provides an additional layer of security for sensitive information.
"""
)

st.subheader("Next Steps in Learning Steganography")
st.write(
    "Obscura Academy provides hands-on lessons in steganography, from encoding messages within images to extracting "
    "hidden information from various media formats. As you progress, you will explore both historical and modern "
    "techniques, developing skills applicable to cybersecurity, forensic analysis, and intelligence operations."
)

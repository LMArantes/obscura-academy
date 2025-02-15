import streamlit as st

st.set_page_config(page_title="Obscura Academy", layout="wide")

st.title("Welcome to Obscura Academy")
st.write("### About Obscura Academy")
st.write(
    "Obscura Academy is a beginner-friendly platform designed to introduce users to the fundamentals of "
    "cryptography in an engaging and interactive way."
)
st.write(
    "Our goal is to help users develop problem-solving skills and an understanding of historical encryption "
    "techniques through hands-on lessons and challenges."
)

st.image("assets/obscura-academy-logo.png", use_container_width=True)

st.write("### Why Learn Cryptography?")
st.write("- Understand the basics of secure communication")
st.write("- Develop logical thinking and problem-solving skills")
st.write("- Gain hands-on experience with classic ciphers")

st.write("### Available Lessons")
st.write("Navigate to lessons using the sidebar.")

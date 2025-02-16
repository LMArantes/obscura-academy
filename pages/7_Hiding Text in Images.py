import streamlit as st
from stegano.lsb import hide, reveal
from PIL import Image
import io

st.set_page_config(page_title="LSB Image Steganography", layout="wide")

st.title("Hiding Text in Images")
st.markdown("## *Least Significant Bit (LSB) Steganography*")
st.markdown("---")

st.write(
    "The **Least Significant Bit (LSB) method** is a technique in steganography that hides information "
    "within the least significant bits of an image’s pixels. This allows secret messages to be embedded "
    "without visibly altering the image. This method is commonly used in digital steganography because it "
    "preserves the overall look of the image while concealing information inside it."
)

st.image("assets/LeastSignificantBitDemonstration.jpg", caption="Least Significant Bit demonstration.")

st.subheader("How It Works:")
st.markdown(
    """
1. The user uploads an image.
2. A secret message is embedded into the image using **LSB steganography**.
3. The modified image is generated, and the user can download it.
4. Another user can later upload the modified image to extract and reveal the hidden message.
"""
)

st.subheader("🔐 Hide a Message in an Image")

# Image Upload Section
uploaded_image = st.file_uploader("Upload an image (PNG only)", type=["png"])

if uploaded_image:
    # Open image
    image = Image.open(uploaded_image)

    # Display uploaded image
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Input for the secret message
    secret_message = st.text_area("Enter the secret message you want to hide:")

    if st.button("🔏 Encode Message into Image"):
        if secret_message:
            # Encode the message into the image
            encoded_image = hide(image, secret_message)

            # Convert image to a downloadable format
            image_bytes = io.BytesIO()
            encoded_image.save(image_bytes, format="PNG")
            image_bytes.seek(0)

            # Provide a download button
            st.success("Message successfully hidden in the image!")
            st.download_button(
                label="📥 Download Encoded Image",
                data=image_bytes,
                file_name="encoded_image.png",
                mime="image/png"
            )
        else:
            st.warning("Please enter a message before encoding.")

st.subheader("📤 Extract a Hidden Message from an Image")

# Image Upload for Decoding
uploaded_encoded_image = st.file_uploader("Upload an image with a hidden message (PNG only)", type=["png"], key="decode")

if uploaded_encoded_image:
    encoded_image = Image.open(uploaded_encoded_image)

    # Display the uploaded encoded image
    st.image(encoded_image, caption="Uploaded Encoded Image", use_container_width=True)

    if st.button("🔍 Reveal Hidden Message"):
        try:
            hidden_text = reveal(encoded_image)
            if hidden_text:
                st.success("Hidden Message Found:")
                st.code(hidden_text, language="plaintext")
            else:
                st.warning("No hidden message was found in this image.")
        except Exception as e:
            st.error("Error while decoding the image. Ensure it contains a hidden message.")

import streamlit as st
from pysstv.color import Robot36
from PIL import Image
import io
import numpy as np
import wave
st.set_page_config(page_title="SSTV - Slow Scan Television", layout="wide")

st.title("Slow Scan Television (SSTV)")
st.markdown("## *Transmitting Images Through Sound*")

st.markdown("---")

st.subheader("What is SSTV?")
st.write(
    "Slow Scan Television (SSTV) is a method of transmitting images using audio signals over radio frequencies. "
    "Unlike traditional television, which transmits continuous video at high frame rates, SSTV transmits still images "
    "line-by-line over a period of several seconds. This technique is widely used in **amateur radio, "
    "space communication, and scientific research.**"
)

st.subheader("Example: SSTV Transmission")
st.write(
    "Below is an example of an image transmitted using SSTV and its corresponding SSTV audio signal. "
    "You can **view the image and listen to the transmission audio** to understand how SSTV works."
)

# Display the SSTV-transmitted image
st.image("assets/sstv-image.png", caption="Image Received via SSTV Transmission", width=250)

# Play the corresponding SSTV audio
st.audio("assets/sstv-audio.wav", format="audio/wav")

st.write(
    "This audio file represents the sound generated when transmitting the above image via **SSTV Martin 1**. "
    "If decoded correctly, this sound would reconstruct the image at the receiving end."
)

st.subheader("Historical Background")
st.write(
    "SSTV was developed in the late 1950s as a way for amateur radio operators (HAM radio users) to send images over "
    "radio waves. It was quickly adopted by space agencies, including **NASA, which used SSTV to transmit images from "
    "early space missions.**"
)

st.write("")

st.image("assets/sstv_nasa.png", caption="The International Space Station has a  history of transmitting SSTV "
                                         "pictures for global events", width=250)
st.write("")

st.markdown(
    """
### **Key Historical Milestones:**
- **1957** - First SSTV experiments conducted using analog television standards.
- **1966** - NASA’s Lunar Orbiter missions use SSTV to send images of the Moon back to Earth.
- **1969** - Apollo 11’s Moon landing images were transmitted via SSTV before being converted to standard TV format.
- **Present Day** - The International Space Station (ISS) still uses SSTV to broadcast images to Earth via HAM radio.
"""
)

st.image("assets/ISS_sstv.png", caption="An SSTV image received by an amateur station transmitted from the ISS using "
                                        "the PD-120 mode.", width=250)

st.subheader("How Does SSTV Work?")
st.write(
    "SSTV transmits images as **audio frequencies**, encoding pixel brightness levels into sound waves. The receiver "
    "interprets these signals and reconstructs the image line-by-line. Different SSTV modes (such as **Robot 36, "
    "Scottie, and Martin**) vary in resolution and transmission time."
)

st.markdown(
    """
### **Steps in an SSTV Transmission:**
1. **Image Preparation** - The image is converted into a format compatible with SSTV.
2. **Audio Signal Generation** - The image data is modulated into audio tones.
3. **Transmission** - The audio signal is transmitted over radio frequencies or stored as a sound file.
4. **Decoding & Reconstruction** - A receiving station interprets the audio and reconstructs the image.
"""
)

st.subheader("Modern Uses of SSTV")

st.markdown(
    """
##### **Applications of SSTV Today:**
- **Amateur Radio (HAM Radio)** - Enthusiasts use SSTV to communicate and share images worldwide.
- **Scientific Research** - SSTV is used to send environmental and meteorological data from remote locations.
- **Aviation & Maritime Communication** - Transmitting images in areas where internet access is limited.
- **Space Exploration** - The International Space Station (ISS) periodically broadcasts images to HAM radio operators on Earth.
"""
)

st.subheader("How SSTV Differs from Traditional Steganography")
st.write(
    "While SSTV is not a steganographic method in itself, it shares some similarities with covert communication "
    "techniques. It allows images to be **transmitted as disguised audio signals**, making it an interesting way to "
    "store and transport visual data without direct image transmission. This makes SSTV useful in scenarios where "
    "traditional data transfer methods are unavailable."
)

st.title("Convert an Image to SSTV Audio")

st.write(
    "Upload an image, and it will be converted into an **SSTV** transmission signal. "
    "You can then **listen to the audio transmission** or **download the SSTV audio file** for further decoding."
)

# Image Upload
uploaded_image = st.file_uploader("Upload an image (PNG or JPG)", type=["png", "jpg", "jpeg"])

if uploaded_image:
    # Open and process image
    image = Image.open(uploaded_image).convert("RGB")  # Keep as PIL Image
    image = image.resize((320, 256))  # Standard SSTV resolution for Robot 36

    # Display uploaded image
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("🎙️ Convert to SSTV Audio"):
        # Encode image using SSTV Robot 36 mode
        sstv = Robot36(image, samples_per_sec=11025, bits=16)  # Correct parameters

        # Create an in-memory buffer to store audio
        audio_buffer = io.BytesIO()

        # Generate SSTV signal and write to buffer
        sstv.write_wav(audio_buffer)  # FIX: Directly write to buffer

        # Move buffer position to start for playback and download
        audio_buffer.seek(0)

        # Provide playback and download options
        st.success("SSTV audio successfully generated!")

        # Play SSTV audio in browser
        st.audio(audio_buffer, format="audio/wav")

        # Download SSTV audio file
        st.download_button(
            label="📥 Download SSTV Audio",
            data=audio_buffer,
            file_name="sstv_audio.wav",
            mime="audio/wav"
        )

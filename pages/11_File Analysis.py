import streamlit as st
import os
import pandas as pd
import exifread  # Extracts image metadata (EXIF)
import binascii  # Extracts hex data
import PyPDF2  # Extracts metadata from PDFs
import mutagen  # Extracts metadata from audio files
import tempfile
import zipfile

st.set_page_config(page_title="File Analysis: Metadata & Hex Editors", layout="wide")

st.title("File Analysis: Metadata & Hex Editors")

st.subheader("Upload a File or ZIP Archive for Analysis")
uploaded_file = st.file_uploader(
    "Upload an image, PDF, text, audio, or ZIP file",
    type=["jpg", "jpeg", "png", "pdf", "txt", "mp3", "flac", "zip"]
)


def extract_metadata(file_path):
    """Extracts metadata from a file based on its type."""
    metadata = {}

    # Extract file system metadata (only for ZIP extraction)
    if not file_path.endswith(".zip"):
        stat_info = os.stat(file_path)
        metadata["File Name"] = os.path.basename(file_path)
        metadata["File Size (KB)"] = round(stat_info.st_size / 1024, 2)

    # Extract metadata for images (EXIF)
    if file_path.lower().endswith((".jpg", ".jpeg", ".tiff")):
        with open(file_path, "rb") as f:
            tags = exifread.process_file(f)
            for tag in tags.keys():
                metadata[tag] = str(tags[tag])

    # Extract metadata for PDFs (creation/modification dates)
    elif file_path.lower().endswith(".pdf"):
        with open(file_path, "rb") as f:
            pdf_reader = PyPDF2.PdfReader(f)
            pdf_metadata = pdf_reader.metadata
            if pdf_metadata:
                for key, value in pdf_metadata.items():
                    metadata[key] = value

    # Extract metadata for audio files
    elif file_path.lower().endswith((".mp3", ".flac")):
        audio = mutagen.File(file_path, easy=True)
        if audio is not None:
            for key, value in audio.tags.items():
                metadata[key] = ", ".join(value)

    return metadata


# Process uploaded file
if uploaded_file:
    # Save file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.getvalue())
        file_path = temp_file.name

    # Check if uploaded file is a ZIP archive
    if uploaded_file.name.endswith(".zip"):
        st.write("📂 Extracting files from ZIP archive...")
        extracted_files = []
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            extracted_dir = tempfile.mkdtemp()  # Create a temp directory for extracted files
            zip_ref.extractall(extracted_dir)  # Extract files
            extracted_files = zip_ref.namelist()

        # Display extracted file names
        st.write("### Extracted Files:")
        for file in extracted_files:
            st.write(f"📄 {file}")

        # Process each extracted file
        for extracted_file in extracted_files:
            extracted_file_path = os.path.join(extracted_dir, extracted_file)
            metadata_dict = extract_metadata(extracted_file_path)

            st.write(f"### Metadata for {extracted_file}")
            if metadata_dict:
                metadata_df = pd.DataFrame(metadata_dict.items(), columns=["Metadata Field", "Value"])
                st.dataframe(metadata_df)
            else:
                st.write("❌ No metadata found.")

    else:
        # Extract metadata for a single file
        metadata_dict = extract_metadata(file_path)

        st.write("### Extracted Metadata")
        if metadata_dict:
            metadata_df = pd.DataFrame(metadata_dict.items(), columns=["Metadata Field", "Value"])
            st.dataframe(metadata_df)
        else:
            st.write("❌ No metadata found.")

st.subheader("Hex Dump: Viewing Raw File Data")
st.write(
    "**Hex editors** allow you to view the raw hexadecimal representation of a file. "
    "Some cryptographic puzzles hide messages in **hex codes** or require modifying files at the binary level."
)

st.subheader("View File's Hex Dump")

if uploaded_file and not uploaded_file.name.endswith(".zip"):
    with open(file_path, "rb") as f:
        hex_data = binascii.hexlify(f.read(256)).decode("utf-8")  # Read first 256 bytes

    # Format hex output for better readability
    hex_display = " ".join(hex_data[i:i + 2] for i in range(0, len(hex_data), 2))
    st.text_area("Hex Dump (First 256 Bytes)", hex_display, height=150)

st.markdown("---")

st.subheader("Try it Yourself: Metadata Challenge")
st.write(
    "We've created a **challenge ZIP file** containing various files with hidden metadata clues. "
    "Download the ZIP file, upload it to our analysis tool, and see if you can uncover the secrets!"
)

# Path to the challenge ZIP file
zip_file_path = "assets/metadata_challenge.zip"

# Read ZIP file for download button
with open(zip_file_path, "rb") as f:
    zip_data = f.read()

# Add a Download Button for the ZIP file
st.download_button(
    label="📥 Download Metadata Challenge ZIP",
    data=zip_data,
    file_name="metadata_challenge.zip",
    mime="application/zip",
    help="Click to download the challenge ZIP file containing hidden metadata clues."
)

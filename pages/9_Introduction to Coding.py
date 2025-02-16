import streamlit as st
import pandas as pd
import numpy as np

# Generate input sizes
x = np.linspace(1, 50, 100)

# Compute Big O functions
data = {
    "Input Size (n)": x,
    "O(1) - Constant": np.ones_like(x),
    "O(log n) - Logarithmic": np.log(x),
    "O(n) - Linear": x,
    "O(n log n) - Log-linear": x * np.log(x),
    "O(n²) - Quadratic": x**2,
    "O(2ⁿ) - Exponential": 2**(x / 8)  # Scaling down for visualization
}

# Convert to DataFrame
big_o_df = pd.DataFrame(data)

st.set_page_config(page_title="Introduction to Coding", layout="wide")

st.image("assets/web-development.png")

st.title("Introduction to Coding")
st.markdown("## *Understanding the Fundamentals*")
st.markdown("---")

st.subheader("What is Coding?")
st.write(
    "Coding is the process of giving **instructions to a computer** in a language it understands. These instructions, "
    "known as programs, tell the computer what tasks to perform. Everything from websites, mobile apps, and video games"
    "to operating systems and cybersecurity tools is built using code."
)

st.subheader("How Do Computers Work?")
st.write(
    "At its core, a computer is a **machine that processes data** using electronic signals. These signals are "
    "represented in **binary code**, a system of ones (`1`) and zeros (`0`). Every operation a computer "
    "performs—whether displaying an image, running software, or encrypting a message—is ultimately translated into "
    "**binary instructions**."
)

st.markdown("### **The Basics of Computer Operations**")

st.subheader("Understanding Binary and How Computers Interpret Code")
st.write(
    "Computers operate using the **binary system**, where each digit (bit) can be either **0 or 1**. A sequence of "
    "bits forms a **byte**, which can represent numbers, letters, images, and even sound."
)

# Create a DataFrame with ASCII letters and their binary representation
data = {
    "Character": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"],
    "Binary Representation": [
        "01000001", "01000010", "01000011", "01000100", "01000101",
        "01000110", "01000111", "01001000", "01001001", "01001010",
        "01001011", "01001100", "01001101", "01001110", "01001111", "01010000"
    ]
}

# Convert to DataFrame and display it
binary_df = pd.DataFrame(data)
st.dataframe(binary_df, width=500)

st.subheader("The Role of Mathematics in Coding")
st.write(
    "Mathematics plays a crucial role in programming. Many cryptographic techniques, puzzles, and online challenges "
    "require a basic understanding of math concepts like **modular arithmetic, prime numbers, and logical operations**."
)

st.markdown(
    """
### **Key Mathematical Concepts in Programming**
1. **Boolean Logic** - The foundation of decision-making in programming (`True` / `False` conditions).
2. **Modular Arithmetic** - Used in encryption, cryptography, and cyclic patterns (e.g., Caesar cipher).
3. **Prime Numbers** - Fundamental in modern encryption (RSA cryptography).
4. **Pattern Recognition** - Detecting trends and structures in data (used in AI, pattern matching, and puzzle-solving).
5. **Algorithms** - Step-by-step procedures for solving problems, often requiring logical thinking and mathematical precision.
"""
)

st.subheader("Why Learn to Code?")
st.write(
    "Coding is not just about writing software—it enhances **problem-solving skills, logical thinking, "
    "and creativity**. Whether you're interested in web development, cybersecurity, artificial intelligence, "
    "or cryptography, coding is an essential skill."
)

# Display Big O Notation explanation
st.subheader("Understanding Big O Notation")
st.write(
    "Big O notation describes how the runtime of an algorithm increases relative to the input size (`n`). "
    "The chart below illustrates different growth rates, from constant time O(1) to exponential time O(2^n). "
    "Efficient algorithms tend to have **O(1)**, **O(log n)**, or **O(n)** complexity, while less efficient algorithms "
    "such as **O(n²)** or **O(2ⁿ)** can become impractical for large inputs."
)

# Display the Big O complexity chart using st.line_chart()
st.line_chart(big_o_df.set_index("Input Size (n)"))

st.markdown(
    """
### **Applications of Coding**
- **Web Development** → Building websites, interactive applications.
- **Cryptography & Cybersecurity** → Protecting data using encryption techniques.
- **Game Development** → Designing games using programming languages.
- **Hacking & Digital Forensics** → Analyzing and securing systems.
- **Automation & AI** → Creating scripts and machine learning models.
"""
)

st.subheader("Next Steps in Learning Coding")
st.write(
    "Now that you understand the fundamentals of how computers process information, let's dive deeper into specific "
    "topics. Next, we will explore **HTML**, the basic language used to create and structure web pages. "
    "Understanding HTML is crucial because many online challenges and ARGs hide clues within a website’s source code."
)

html_code = """ 
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to Obscura Academy</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a basic HTML page. Stay curious!</p>
</body>
</html>
"""

st.code(html_code, language="html")

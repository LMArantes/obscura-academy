import streamlit as st
from streamlit_image_comparison import image_comparison

st.set_page_config(page_title="Basic HTML", layout="wide")

st.title("Basic HTML")
st.markdown("## *Structuring Web Pages*")
st.markdown("---")

st.subheader("What is HTML?")
st.write(
    "HTML (**HyperText Markup Language**) is the standard language used to **create and structure web pages**. "
    "It defines how content is displayed on a webpage using **elements and tags**. HTML is not a programming language, "
    "but a **markup language** that organizes text, images, and links into a structured format."
)

st.subheader("Basic Structure of an HTML Page")

html_code = """ 
<!DOCTYPE html>
<html>
<head>
    <title>My First Web Page</title>
</head>
<body>
    <h1>Welcome to Obscura Academy</h1>
    <p>This is a simple paragraph explaining HTML basics.</p>
</body>
</html>
"""

st.code(html_code, language="html")

st.markdown(
    """
### **Key Parts of an HTML Page**
- `<!DOCTYPE html>` → Declares the document as HTML.
- `<html>` → The **root** element containing all webpage content.
- `<head>` → Stores **metadata** like the webpage title and links to styles/scripts.
- `<title>` → Defines the **browser tab title**.
- `<body>` → Contains the **main content** of the page.
- `<h1>` → A **heading**, used for titles.
- `<p>` → A **paragraph**, used for text content.
"""
)

st.subheader("Common HTML Elements")

st.markdown(
    """
### **Important HTML Tags**
| **Tag** | **Description** |
|---------|----------------|
| `<h1>` to `<h6>` | Headings, where `<h1>` is the largest and `<h6>` the smallest. |
| `<p>` | Paragraph of text. |
| `<a href="">` | A hyperlink to another webpage. |
| `<img src="">` | Displays an image. |
| `<ul>` & `<li>` | Creates a **bullet-point list**. |
| `<ol>` & `<li>` | Creates a **numbered list**. |
| `<!-- Comment -->` | A **hidden comment** that does not appear on the webpage but can be seen in the source code. |
"""
)

st.subheader("Hidden Messages in HTML (Common in ARGs & Puzzles)")
st.write(
    "HTML is often used in **online challenges** and **ARGs (Alternate Reality Games)** to hide clues in **comments, "
    "metadata, or invisible elements**. One way to find hidden messages is to **inspect the page source** ("
    "Right-click → View Page Source)."
)

hidden_html_code = """ 
<!DOCTYPE html>
<html>
<head>
    <title>Secret Webpage</title>
    <!-- Secret Message: The password is "shadow" -->
</head>
<body>
    <h1>Welcome</h1>
    <p>Nothing to see here... or is there?</p>
</body>
</html>
"""

st.code(hidden_html_code, language="html")

st.write(
    "The comment inside the `<head>` section contains a **hidden message**, which can be found by inspecting the "
    "page's source code."
)

st.header("🌐 Webpage vs. HTML Source Code")

st.write(
    "Many online puzzles and ARGs hide clues within the **HTML source code** of a webpage. "
    "Here, you can compare a **visual webpage screenshot** with its **HTML source code** representation."
)

image_comparison(
    img1="assets/website-html.png",
    img2="assets/website-screenshot.png",
    label1="Website View",
    label2="HTML Source Code",
)

st.subheader("What are Developer Tools?")
st.write(
    "Web browsers come with built-in **Developer Tools (DevTools)** that allow you to inspect and modify "
    "a webpage’s **HTML, CSS, and JavaScript**. This is useful for **finding hidden clues, debugging websites, "
    "and understanding how web pages work.**"
)

st.markdown(
    """
### **How to Open Developer Tools?**
- **Google Chrome** → Right-click anywhere on the page and select `"Inspect"`, or press `F12` or `Ctrl + Shift + I`.
- **Firefox** → Right-click → `"Inspect"`, or press `F12`.
- **Edge** → Press `F12` or `Ctrl + Shift + I`.
- **Safari** → Enable `"Show Develop menu"` in Preferences, then `Option + Command + I`.

### **Main Sections of DevTools**
| **Tab** | **Purpose** |
|---------|------------|
| **Elements** | View and edit the HTML structure of the page. |
| **Console** | Run JavaScript commands and debug scripts. |
| **Network** | Inspect requests made by the website (useful for API clues). |
| **Sources** | View and edit JavaScript and other page resources. |
| **Application** | Check cookies, local storage, and hidden data. |
"""
)

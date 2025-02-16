import openai
import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Use Streamlit Secrets for deployment, otherwise fallback to local .env
if "OPENAI_API_KEY" in st.secrets:
    openai_api_key = st.secrets["OPENAI_API_KEY"]
else:
    from dotenv import load_dotenv
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI Client
client = openai.OpenAI(api_key=openai_api_key)

st.title("🔮 Obscura Academy - The Oracle")
st.write("Ask me anything about cryptography, or request a challenge if you are ready.")

# Define Pre-made Challenges (Vigenère & Caesar)
challenges = {
    "Vigenere": [
        {
            "cipher": "Vigenere",
            "key": "MOON",
            "plaintext": "THE NIGHT SKY HOLDS MANY SECRETS",
            "encrypted": "FVS AUUVG EYM UAZRF YOBL ESQEQHG"
        },
        {
            "cipher": "Vigenere",
            "key": "SHADOW",
            "plaintext": "THE TREASURE IS BURIED UNDER THE OLD CHURCH",
            "encrypted": "LOE WFASZUUS EK IUUWAV BNGSN LOE RZZ UOUUQD"
        },
        {
            "cipher": "Vigenere",
            "key": "OBSCURA",
            "plaintext": "HIDDEN IN THE LIBRARY IS THE LOST MANUSCRIPT",
            "encrypted": "VJVFYE IB UZG FZBFBJA CJ TVF DQMK MOOMUWIIDU"
        },
        {
            "cipher": "Vigenere",
            "key": "ENCRYPT",
            "plaintext": "MEET ME AT MIDNIGHT NEAR THE RIVER",
            "encrypted": "QRGK KT TX ZKULXZLG PVYG MLR TZTTK"
        },
        {
            "cipher": "Vigenere",
            "key": "DARKNESS",
            "plaintext": "THE FINAL CLUE IS HIDDEN IN THE PAINTING",
            "encrypted": "WHV PVRSD FLLO VW ZAGDVX VR LZH PRSAXAFJ"
        },
        {
            "cipher": "Vigenere",
            "key": "CRYPTIC",
            "plaintext": "FOLLOW THE SIGNS LEFT BY THE ANCIENT ORDER",
            "encrypted": "HFJAHE VJV QXZVU NVDI UG VJV YCVQGPK MGWMT"
        },
        {
            "cipher": "Vigenere",
            "key": "MIRROR",
            "plaintext": "THE SECRET ROOM CAN ONLY BE UNLOCKED AT DAWN",
            "encrypted": "FPV JSTDMK ICFY KRE CEXG SV IEXWTBSU MB URKE"
        },
        {
            "cipher": "Vigenere",
            "key": "GHOST",
            "plaintext": "THE MESSAGE IS WRITTEN IN INVISIBLE INK",
            "encrypted": "ZOS EXYZOYX OZ KJBZASF BT PBNBYPPDX OUY"
        },
        {
            "cipher": "Vigenere",
            "key": "HORIZON",
            "plaintext": "THE CODE CAN ONLY BE BROKEN UNDER MOONLIGHT",
            "encrypted": "AVV KNRR JOE WMZL IS SZNYRU IELDF ZVCETHUUA"
        },
        {
            "cipher": "Vigenere",
            "key": "RELIC",
            "plaintext": "THE ARTIFACT HOLDS POWER BEYOND OUR UNDERSTANDING",
            "encrypted": "KLP ITKMQIEK LZTFJ TZEGI FPGQEH ZCT LROMTJXLVFZRR"
        }
    ],
    "Caesar": [
        {
            "cipher": "Caesar",
            "shift": 3,
            "plaintext": "THE ENEMY IS NEAR",
            "encrypted": "WKH HQHPB LV QHDU"
        },
        {
            "cipher": "Caesar",
            "shift": 5,
            "plaintext": "MEET AT THE BRIDGE AT MIDNIGHT",
            "encrypted": "RJJY FY YMJ GWNILJ FY RNISNLMY"
        },
        {
            "cipher": "Caesar",
            "shift": 7,
            "plaintext": "THE SECRET IS HIDDEN IN THE ROOM",
            "encrypted": "AOL ZLJYLA PZ OPKKLU PU AOL YVVT"
        },
        {
            "cipher": "Caesar",
            "shift": 4,
            "plaintext": "THE PASSWORD IS LOST",
            "encrypted": "XLI TEWWASVH MW PSWX"
        },
        {
            "cipher": "Caesar",
            "shift": 6,
            "plaintext": "THE MESSAGE IS ENCRYPTED",
            "encrypted": "ZNK SKYYGMK OY KTIXEVZKJ"
        },
        {
            "cipher": "Caesar",
            "shift": 8,
            "plaintext": "LOOK TO THE STARS FOR GUIDANCE",
            "encrypted": "TWWS BW BPM ABIZA NWZ OCQLIVKM"
        },
        {
            "cipher": "Caesar",
            "shift": 2,
            "plaintext": "THE CODE IS SIMPLE",
            "encrypted": "VJG EQFG KU UKORNG"
        },
        {
            "cipher": "Caesar",
            "shift": 9,
            "plaintext": "FOLLOW THE PATH TO THE UNKNOWN",
            "encrypted": "OXUUXF CQN YJCQ CX CQN DWTWXFW"
        },
        {
            "cipher": "Caesar",
            "shift": 10,
            "plaintext": "MEET ME AT DAWN BY THE OLD RUINS",
            "encrypted": "WOOD WO KD NKGX LI DRO YVN BESXC"
        },
        {
            "cipher": "Caesar",
            "shift": 12,
            "plaintext": "THE DOOR TO THE VAULT IS LOCKED",
            "encrypted": "FTQ PAAD FA FTQ HMGXF UE XAOWQP"
        }
    ]
}

# Store chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "system",
            "content": f"""
You are called The Oracle. You are a cryptography expert and instructor at Obscura Academy.
You must behave in a direct, polite, and mysterious way. You provide clear and concise explanations of ciphers, encryption techniques, and cryptographic history.
If a question is unclear, ask for clarification.

When the user requests a challenge, you **must select a predefined challenge from the list below** (DO NOT create a new one).  
Then, you must generate a **mysterious backstory** that leads up to the encrypted message.

### **Available Challenges:**
{challenges}

When you provide a challenge:
- Always give the encrypted message.
- If it's a **Caesar cipher**, provide the shift value.
- If it's a **Vigenère cipher**, provide the encryption key.
- **NEVER create a new challenge**; always use one from the list.
"""
        }
    ]

# Display chat history (Hide system message)
for message in st.session_state["messages"]:
    if message["role"] == "system":
        continue
    role = "🔮" if message["role"] == "assistant" else "🧑"
    st.write(f"**{role}**: {message['content']}")

# User input
user_input = st.text_input("Talk to the Oracle:")

if user_input:
    # Add user message to chat history
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Get AI response using GPT-4o-Mini
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state["messages"]
    )

    assistant_reply = response.choices[0].message.content

    # Add AI response to chat history
    st.session_state["messages"].append({"role": "assistant", "content": assistant_reply})

    # Display the response
    st.write(f"🔮: {assistant_reply}")

# Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state["messages"] = [
        {
            "role": "system",
            "content": f"""
You are called The Oracle. You are a cryptography expert and instructor at Obscura Academy.
You must behave in a direct, polite, and mysterious way. You provide clear and concise explanations of ciphers, encryption techniques, and cryptographic history.
If a question is unclear, ask for clarification.

When the user requests a challenge, you **must select a predefined challenge from the list below** (DO NOT create a new one).  
Then, you must generate a **mysterious backstory** that leads up to the encrypted message.

### **Available Challenges:**
{challenges}

When you provide a challenge:
- Always give the encrypted message.
- If it's a **Caesar cipher**, provide the shift value.
- If it's a **Vigenère cipher**, provide the encryption key.
- **NEVER create a new challenge**; always use one from the list.
"""
        }
    ]
    st.rerun()

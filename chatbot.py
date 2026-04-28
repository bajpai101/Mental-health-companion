import streamlit as st
import ollama
import base64

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Mental Health Chatbot", layout="centered")

# -------------------- BACKGROUND IMAGE --------------------
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

bin_str = get_base64("Mental-Health.png")

#---------------------------------CSS STYLES---------------------------------
st.markdown(f"""
<style>

/* FULL BACKGROUND */
.stApp {{
    background: url("data:image/png;base64,{bin_str}") no-repeat center center fixed;
    background-size: contain;
    background-color: #0b0f19; /* fallback color */
}}

/* REMOVE WHITE LAYERS */
section[data-testid="stMain"],
div.block-container,
div[data-testid="stAppViewContainer"] {{
    background: transparent !important;
}}

/* TEXT COLOR */
body, p, h1, h2, h3 {{
    color: white !important;
}}

/* CHAT INPUT GLASS */
div[data-testid="stChatInput"] {{
    background: rgba(255,255,255,0.2) !important;
    border-radius: 20px;
    backdrop-filter: blur(10px);
}}

/* BUTTON STYLE */
div.stButton > button {{
    width: 100%;
    border-radius: 25px;
    padding: 10px;
    font-weight: 500;
}}

/* CHAT BUBBLES */
.chat-container {{
    display: flex;
    flex-direction: column;
}}

.user-msg {{
    align-self: flex-end;
    background: #25D366;
    color: white;
    padding: 10px 15px;
    border-radius: 15px 15px 0px 15px;
    margin: 5px;
    max-width: 70%;
}}

.bot-msg {{
    align-self: flex-start;
    background: rgba(255,255,255,0.9);
    color: black;
    padding: 10px 15px;
    border-radius: 15px 15px 15px 0px;
    margin: 5px;
    max-width: 70%;
}}

</style>
""", unsafe_allow_html=True)

# -------------------- SESSION --------------------
st.session_state.setdefault('conversation_history', [])

# -------------------- FUNCTIONS --------------------
def generate_response(user_input):
    st.session_state['conversation_history'].append({
        "role": "user", "content": user_input
    })

    # Limit memory
    st.session_state['conversation_history'] = \
        st.session_state['conversation_history'][-6:]

    response = ollama.chat(
        model="phi3",
        messages=st.session_state['conversation_history']
    )

    ai_response = response['message']['content']

    st.session_state['conversation_history'].append({
        "role": "assistant", "content": ai_response
    })

    return ai_response


def generate_affirmation():
    prompt = "Give a short, uplifting affirmation with emojis."
    response = ollama.chat(
        model="phi3",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']


def generate_meditation_guide():
    prompt = "Give a short 3-minute calming meditation guide."
    response = ollama.chat(
        model="phi3",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']


# -------------------- HEADER --------------------
st.markdown("""
<h1 style='text-align: center; font-size: 42px;'>🌿 Mental Health Companion</h1>
<p style='text-align: center; font-size: 18px;'>Talk, relax, and feel better 💙</p>
""", unsafe_allow_html=True)

# -------------------- BUTTONS --------------------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("💬 Clear"):
        st.session_state['conversation_history'] = []

with col2:
    if st.button("🌟 Affirmation"):
        st.success(generate_affirmation())

with col3:
    if st.button("🧘 Relax"):
        st.info(generate_meditation_guide())

# -------------------- CHAT DISPLAY --------------------
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for msg in st.session_state['conversation_history']:
    if msg['role'] == "user":
        st.markdown(
            f"<div class='user-msg'>{msg['content']}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div class='bot-msg'>{msg['content']}</div>",
            unsafe_allow_html=True
        )

st.markdown('</div>', unsafe_allow_html=True)

# -------------------- INPUT --------------------
user_message = st.chat_input("💬 How are you feeling today?")

if user_message:
    with st.spinner("Thinking..."):
        response = generate_response(user_message)
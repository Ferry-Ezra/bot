import streamlit as st
import random
import datetime

# --- Setup halaman ---
st.set_page_config(
    page_title="Eztorenesia",
    page_icon="🤖",
    layout="wide"
)
st.markdown("""
    <h1 style="text-align:center; color:#E1306C;">Halo</h1>
    <p style="text-align:center;">Ngobrol santai sama Gue! Klik tombol Reset untuk mulai ulang.</p>
""", unsafe_allow_html=True)

# --- Session state ---
if "chat" not in st.session_state:
    st.session_state.chat = []

if "custom_responses" not in st.session_state:
    st.session_state.custom_responses = {}

# --- Tombol Reset ---
if st.button("Reset Chat"):
    st.session_state.chat = []

# --- Input multi-line ---
user_input = st.text_area("Tulis pesanmu disini ✍️:", height=60)

# --- Default responses FerryBot ---
default_responses = {
    "halo": ["Halo juga! 👋", "Hai! 😎 Gimana kabarnya?", "Hey! Senang ketemu kamu 😁"],
    "siapa kamu": ["Aku FerryBot, chatbot santai yang menemanimu di IG 😎", "Aku bot, tapi bisa diajak ngobrol kok! 😁"],
    "apa kabar": ["Baik banget! Kamu sendiri gimana?", "Sehat selalu 😁", "Lagi semangat nih! 🌟"],
    "terima kasih": ["Sama-sama! 😊", "Senang bisa bantu 😎"],
    "selamat pagi": ["Selamat pagi! 🌞 Semangat hari ini!", "Pagi! Jangan lupa sarapan 😁"],
    "selamat malam": ["Selamat malam! 🌙 Semoga mimpi indah ✨", "Malam! Jangan begadang ya 😎"],
    "lucu": ["Haha 😆, aku suka jokes juga 😎", "Hihi 😁", "Lucu ya? 😂"],
    "ferry": ["Hehe iya, itu aku 😎", "Ferry hadir! 😁"]
}

# --- Fungsi merespons ---
def get_bot_response(user_text):
    user_lower = user_text.lower()
    # cek custom responses
    for key, answers in st.session_state.custom_responses.items():
        if key in user_lower:
            return random.choice(answers)
    # cek default responses
    for key, answers in default_responses.items():
        if key in user_lower:
            return random.choice(answers)
    return "Hmm, aku belum paham itu 😅"

# --- Simpan percakapan ---
if user_input:
    bot_response = get_bot_response(user_input)
    st.session_state.chat.append(("Kamu", user_input))
    st.session_state.chat.append(("FerryBot", bot_response))

# --- Tampilkan chat gaya IG/WhatsApp ---
for speaker, text in st.session_state.chat:
    if speaker == "Kamu":
        st.markdown(
            f"<div style='text-align:right; background-color:#f3f3f3; color:#000; padding:8px; border-radius:12px; margin:5px 0; display:inline-block; max-width:70%'>{text}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div style='text-align:left; background-color:#E1306C; color:white; padding:8px; border-radius:12px; margin:5px 0; display:inline-block; max-width:70%'>{text}</div>",
            unsafe_allow_html=True
        )

st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

# --- Fitur belajar sementara ---
with st.expander("Ajari FerryBot jawaban baru"):
    new_keyword = st.text_input("Kata kunci / pertanyaan baru")
    new_answer = st.text_input("Jawaban FerryBot")
    if st.button("Tambahkan jawaban baru"):
        if new_keyword.strip() and new_answer.strip():
            if new_keyword.lower() in st.session_state.custom_responses:
                st.session_state.custom_responses[new_keyword.lower()].append(new_answer)
            else:
                st.session_state.custom_responses[new_keyword.lower()] = [new_answer]
            st.success(f"Jawaban baru untuk '{new_keyword}' berhasil ditambahkan! 😎")

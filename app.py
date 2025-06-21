import streamlit as st
import random

st.set_page_config(page_title="Thi tốt nhé 💖", page_icon="🌸", layout="centered")

st.title("🌸 Gửi Lời Chúc Thi Tốt 🌸")
name = st.text_input("Nhập tên người bạn muốn gửi lời chúc:", placeholder="Ví dụ: Vy, Linh,...")

if name:
    gifs = [
        "https://media.giphy.com/media/3ohs4BSacFKI7A717y/giphy.gif",
        "https://media.giphy.com/media/l0Exk8EUzSLsrErEQ/giphy.gif",
        "https://media.giphy.com/media/3o7TKsQ8y7KpLCRMIY/giphy.gif"
    ]

    st.image(random.choice(gifs), caption="Thi thật tốt nhé!", use_column_width=True)

    st.markdown(f"""
    <div style="background-color:#ffe8f0; padding:20px; border-radius:12px; font-size:18px">
    Gửi **{name}**,<br><br>
    Chúc cậu một kỳ thi thật suôn sẻ. Tớ tin rằng cậu <b>đủ giỏi, đủ mạnh mẽ</b> để vượt qua tất cả.<br>
    Hãy giữ vững tinh thần, <span style="color:#d63031; font-weight:bold">tập trung, bình tĩnh</span> và làm hết sức mình nhé!<br><br>
    Tớ ở đây, âm thầm cổ vũ cậu từng phút 💖<br><br>
    <div style="text-align:right;">– Một người đang dõi theo cậu</div>
    </div>
    """, unsafe_allow_html=True)

import streamlit as st
import random

# ------------------------------
# 🎨 페이지 설정
# ------------------------------
st.set_page_config(
    page_title="가위✌️ 바위✊ 보🖐 게임!",
    page_icon="🎮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ------------------------------
# 🎉 타이틀 & 설명
# ------------------------------
st.markdown("<h1 style='text-align: center; color: #f63366;'>🎮 가위✌️ 바위✊ 보🖐 챌린지!</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>운과 센스를 발휘해 컴퓨터를 이겨보세요! 😎</h3>", unsafe_allow_html=True)
st.markdown("---")

# ------------------------------
# 🎭 이모지 매핑
# ------------------------------
emoji_dict = {
    "가위": "✌️",
    "바위": "✊",
    "보": "🖐"
}

choices = ["가위", "바위", "보"]

# ------------------------------
# 🕹️ 사용자 선택
# ------------------------------
st.subheader("당신의 선택은? 🤔")
player_choice = st.radio(
    "가위✌️, 바위✊, 보🖐 중 하나를 선택하세요:",
    choices,
    horizontal=True,
    index=0
)

# ------------------------------
# 🤖 컴퓨터 선택
# ------------------------------
computer_choice = random.choice(choices)

# ------------------------------
# 🧠 승부 판단 로직
# ------------------------------
def get_result(player, computer):
    if player == computer:
        return "비겼어요! 🤝"
    elif (player == "가위" and computer == "보") or \
         (player == "바위" and computer == "가위") or \
         (player == "보" and computer == "바위"):
        return "이겼어요! 🏆"
    else:
        return "졌어요... 😢"

# ------------------------------
# 🧾 결과 출력
# ------------------------------
if st.button("결과 확인하기! 🎲"):
    st.markdown("---")
    st.markdown(f"### 당신의 선택: {emoji_dict[player_choice]} **{player_choice}**")
    st.markdown(f"### 컴퓨터의 선택: {emoji_dict[computer_choice]} **{computer_choice}**")
    result = get_result(player_choice, computer_choice)
    st.markdown(f"## 🔥 결과: **{result}**")
    st.balloons()

# ------------------------------
# 📌 푸터
# ------------------------------
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Made with ❤️ using Streamlit | 가위바위보 챌린지</p>", unsafe_allow_html=True)

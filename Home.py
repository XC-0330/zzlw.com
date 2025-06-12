import streamlit as st

# 加载自定义古风样式
with open("static/style.css", "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 设置页面为横屏样式
st.set_page_config(
    page_title="中州世界观",
    layout="wide"
)

st.markdown("<h1 style='text-align: center; font-size: 3em;'>欢迎来到中州</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>请输入通行密码以进入世界</h3>", unsafe_allow_html=True)

# 居中密码输入框
col1, col2, col3 = st.columns([3, 2, 3])
with col2:
    password = st.text_input("密码", type="password")
    if st.button("进入"):
        if password == "1231":
            st.success("密码正确，正在进入中州世界...")
            st.switch_page("pages/1_今日中州.py")
        else:
            st.error("密码错误，请重试")

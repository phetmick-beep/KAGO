import streamlit as st
import google.generativeai as genai

# ตั้งค่าหน้าจอ
st.set_page_config(page_title="KAGO AI", page_icon="🤖")

# เชื่อมต่อกุญแจ
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    st.sidebar.success("✅ เชื่อมต่อ AI สำเร็จ")
except Exception as e:
    st.sidebar.error(f"❌ กุญแจผิด: {e}")

st.title("🤖 KAGO AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("ลองพิมพ์ถามอะไรก็ได้..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"⚠️ AI ไม่ตอบเพราะ: {e}")


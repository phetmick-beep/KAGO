import streamlit as st
import google.generativeai as genai

# เชื่อมต่อกับกุญแจที่คุณใส่ในหน้า Secrets
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("❌ ไม่พบ API Key! กรุณาตรวจสอบหน้า Secrets อีกครั้ง")

st.set_page_config(page_title="KAGO AI", page_icon="🤖")

# --- แถบข้างสำหรับระบบสมาชิก ---
with st.sidebar:
    st.title("💎 Membership")
    st.info("โอนเงินเพื่อรับรหัสผ่านที่: BCEL One 160-XXXX-XXXX")
    passcode = st.text_input("กรอกรหัสปลดล็อก:", type="password")
    
    if passcode == "KAGO888":
        st.success("✅ ปลดล็อก Premium แล้ว!")
        st.session_state.premium = True
    else:
        st.session_state.premium = False

# --- หน้าแชทหลัก ---
st.title("🤖 KAGO AI Smart Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("พิมพ์คำถามของคุณ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except:
            st.error("AI กำลังรอสัญญาณ... กรุณาลองใหม่อีกครั้งครับ")

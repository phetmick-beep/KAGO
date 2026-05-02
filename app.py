import streamlit as st

# --- ข้อมูลรับเงิน ---
MY_BANK = "BCEL One: 160XXXXXXXXXXXX" 

st.set_page_config(page_title="KAGO AI")
st.title("🤖 KAGO AI Smart Assistant")

if "premium" not in st.session_state:
    st.session_state.premium = False

# --- แถบข้าง ---
st.sidebar.title("💎 Membership")
if not st.session_state.premium:
    st.sidebar.warning("Status: Free")
    if st.sidebar.button("Upgrade to Premium"):
        st.sidebar.info(f"Please transfer to: {MY_BANK}")
    if st.sidebar.button("Test Premium Mode"): # ปุ่มไว้ให้คุณกดทดสอบเอง
        st.session_state.premium = True
else:
    st.sidebar.success("Status: Premium (Smartest Mode)")

# --- ส่วนแชท ---
query = st.chat_input("Ask KAGO AI...")
if query:
    with st.chat_message("user"):
        st.write(query)
    with st.chat_message("assistant"):
        if st.session_state.premium:
            st.write("🚀 (Premium) วิเคราะห์คำตอบด้วยสมองกลขั้นสูง...")
        else:
            st.write("🤖 (Free) ขอบคุณสำหรับคำถามครับ! สนใจอัปเกรดเพื่อความฉลาดเพิ่มไหม?")

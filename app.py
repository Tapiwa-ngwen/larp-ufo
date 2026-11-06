import streamlit as st

st.set_page_config(page_title="larp.UFO Terminal", page_icon="🛸", layout="centered")

st.title("🛸 larp.UFO Terminal")
st.write("Mobile web interface and wallet simulator.")

command = st.text_input("Enter command or value:")

if st.button("Execute"):
    st.success(f"Executed: {command}")
    st.code(f">>> Processing {command}...\n>>> Success: Operational parameters verified.", language="bash")
  

import streamlit as st

st.title("🚀 larp.UFO Terminal")
st.write("Welcome to the mobile web interface.")

# Example input / interaction matching your app logic
user_input = st.text_input("Enter command or query:")

if st.button("Run Simulation"):
    # Insert your core larp_ufo logic here
    st.success(f"Executed successfully for: {user_input}")

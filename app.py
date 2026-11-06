import streamlit as st

st.set_page_config(page_title="larp.UFO Multi-Wallet Simulator", page_icon="🛸", layout="centered")

# Initialize session state for balances and logs if not already present
if "balances" not in st.session_state:
    st.session_state.balances = {
        "Phantom": 1420.50,
        "MT5": 5250.00,
        "Pumpfun": 89.25,
        "Fomo": 310.00
    }

if "terminal_logs" not in st.session_state:
    st.session_state.terminal_logs = ["System initialized. All operational parameters secure."]

st.title("🛸 larp.UFO // Multi-Wallet Terminal")
st.markdown("Simulated mobile wallet interface, balance manager, and execution terminal.")

# Navigation tabs
tab1, tab2, tab3 = st.tabs(["💳 Wallets & Balances", "⚙️ Balance Config", "💻 Terminal Execution"])

with tab1:
    st.subheader("Active Wallet Balances")
    
    # Display wallets in a grid style metric view
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Phantom Wallet", value=f"${st.session_state.balances['Phantom']:,.2f}")
        st.metric(label="Pumpfun Balance", value=f"${st.session_state.balances['Pumpfun']:,.2f}")
    with col2:
        st.metric(label="MT5 Account", value=f"${st.session_state.balances['MT5']:,.2f}")
        st.metric(label="Fomo Wallet", value=f"${st.session_state.balances['Fomo']:,.2f}")

with tab2:
    st.subheader("Modify Wallet Balances")
    st.markdown("Configure custom values for your simulated display interfaces.")
    
    selected_wallet = st.selectbox("Select Wallet to Modify", list(st.session_state.balances.keys()))
    new_amount = st.number_input("New Balance Value ($)", value=float(st.session_state.balances[selected_wallet]))
    
    if st.button("Update Balance"):
        st.session_state.balances[selected_wallet] = new_amount
        st.success(f"Successfully updated {selected_wallet} balance to ${new_amount:,.2f}!")
        st.rerun()

with tab3:
    st.subheader("Terminal & Command Execution")
    
    command = st.text_input("Enter command or value:", placeholder="e.g., inject_payload, reset_balances, sync_mt5")
    
    if st.button("Execute"):
        if command.strip():
            log_entry = f"Executed: {command} -> Success: Parameters verified."
            st.session_state.terminal_logs.append(log_entry)
        else:
            st.warning("Please enter a valid command.")

    st.markdown("---")
    st.markdown("**Execution Log:**")
    for log in reversed(st.session_state.terminal_logs[-5:]):
        st.code(log, language="bash")
        

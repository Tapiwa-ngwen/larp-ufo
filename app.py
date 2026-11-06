import streamlit as st

st.set_page_config(page_title="larp.UFO Mobile Simulator", page_icon="🛸", layout="centered")

# Custom CSS to make it look like a sleek mobile interface
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background-color: #1f2937;
        color: white;
        border: 1px solid #374151;
        font-weight: 600;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #374151;
        border-color: #4b5563;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "current_screen" not in st.session_state:
    st.session_state.current_screen = "home"

if "balances" not in st.session_state:
    st.session_state.balances = {
        "Phantom": 0.01,
        "MT5": 5250.00,
        "Pumpfun": 1420.50,
        "Fomo": 310.00
    }

# --- NAVIGATION BAR ---
col_nav1, col_nav2, col_nav3, col_nav4 = st.columns(4)
with col_nav1:
    if st.button("🏠 Home"):
        st.session_state.current_screen = "home"
        st.rerun()
with col_nav2:
    if st.button("👻 Phantom"):
        st.session_state.current_screen = "Phantom"
        st.rerun()
with col_nav3:
    if st.button("📈 MT5"):
        st.session_state.current_screen = "MT5"
        st.rerun()
with col_nav4:
    if st.button("🚀 Pumpfun"):
        st.session_state.current_screen = "Pumpfun"
        st.rerun()

st.markdown("---")

# --- HOME / LAUNCHER SCREEN ---
if st.session_state.current_screen == "home":
    st.title("🛸 larp.UFO Launcher")
    st.markdown("Select an app to open:")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("👻 Open Phantom Wallet"):
            st.session_state.current_screen = "Phantom"
            st.rerun()
        if st.button("🚀 Open Pumpfun"):
            st.session_state.current_screen = "Pumpfun"
            st.rerun()
    with col2:
        if st.button("📈 Open MT5 Terminal"):
            st.session_state.current_screen = "MT5"
            st.rerun()
        if st.button("🔥 Open Fomo Sniper"):
            st.session_state.current_screen = "Fomo"
            st.rerun()
            
    st.markdown("---")
    st.subheader("⚙️ Balance Control Panel")
    wallet_choice = st.selectbox("Select Wallet to Edit", list(st.session_state.balances.keys()))
    new_balance = st.number_input("Set Balance ($)", value=float(st.session_state.balances[wallet_choice]))
    if st.button("Update Balance"):
        st.session_state.balances[wallet_choice] = new_balance
        st.success(f"Updated {wallet_choice} balance to ${new_balance:,.2f}!")
        st.rerun()

# --- PHANTOM APP SCREEN ---
elif st.session_state.current_screen == "Phantom":
    st.markdown("## 👻 Phantom")
    st.markdown(f"**Cash Balance:** ${st.session_state.balances['Phantom']:,.2f}")
    
    if st.button("Deposit Funds"):
        st.success("Deposit gateway opened.")
        
    st.markdown("### Explore Markets")
    st.markdown("- **Diamond** — $0.0010979 ($1M MC)")
    st.markdown("- **ANSEM** — $0.0535 ($54M MC)")
    st.markdown("- **BIRB** — $0.0979 ($28M MC)")
    st.markdown("- **CHOO** — $0.00478744 ($4.7M MC)")

# --- MT5 APP SCREEN ---
elif st.session_state.current_screen == "MT5":
    st.markdown("## 📈 MetaTrader 5")
    st.markdown(f"**Account Equity:** ${st.session_state.balances['MT5']:,.2f}")
    
    st.selectbox("Symbol", ["XAUUSDz (Gold)", "BTCUSDz", "BCHUSDz"])
    lot = st.number_input("Lot Size", value=0.1)
    
    col_buy, col_sell = st.columns(2)
    with col_buy:
        if st.button("BUY"):
            st.success("Order executed: BUY")
    with col_sell:
        if st.button("SELL"):
            st.success("Order executed: SELL")

# --- PUMPFUN APP SCREEN ---
elif st.session_state.current_screen == "Pumpfun":
    st.markdown("## 🚀 Pumpfun")
    st.markdown(f"**Balance:** ${st.session_state.balances['Pumpfun']:,.2f}")
    
    if st.button("Deposit"):
        st.info("Redirecting to funding interface...")
        
    st.markdown("### Weekly Top Trades")
    st.markdown("- **bystevenr** : +$49,414.14")
    st.markdown("- **RawZestyFinch** : +$40,582.43")
    
    st.markdown("### Trending Tokens")
    st.markdown("- **NIO** — $0.00188 (+82.23%)")
    st.markdown("- **WHITE** — $0.000410 (+9,490.45%)")

# --- FOMO APP SCREEN ---
elif st.session_state.current_screen == "Fomo":
    st.markdown("## 🔥 Fomo Sniper")
    st.markdown(f"**Available Funds:** ${st.session_state.balances['Fomo']:,.2f}")
    st.text_input("Token Contract Address (CA)")
    if st.button("⚡ Snipe Now"):
        st.warning("Snipe order broadcasted to mempool...")
        

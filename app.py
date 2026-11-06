import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="larp.UFO Simulator", layout="centered")

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
  body { background-color: #0b0e11; color: #ffffff; padding: 10px; display: flex; flex-direction: column; align-items: center; }
  .phone-screen { width: 100%; max-width: 380px; background: #12161c; border-radius: 20px; overflow: hidden; border: 1px solid #2a2e37; box-shadow: 0 10px 30px rgba(0,0,0,0.8); display: flex; flex-direction: column; min-height: 620px; position: relative; }
  .screen { display: none; padding: 16px; flex-direction: column; gap: 15px; height: 550px; overflow-y: auto; }
  .screen.active { display: flex; }
  
  /* Top Bar */
  .app-header { display: flex; justify-content: space-between; align-items: center; font-weight: bold; font-size: 18px; padding-bottom: 10px; border-bottom: 1px solid #23272e; }
  
  /* Cards & Lists */
  .card { background: #1a1e24; padding: 14px; border-radius: 12px; border: 1px solid #2d323e; }
  .balance-title { color: #848e9c; font-size: 12px; text-transform: uppercase; }
  .balance-val { font-size: 28px; font-weight: bold; margin-top: 4px; color: #f0b90b; }
  
  .item-row { display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid #1f242d; }
  .item-name { font-weight: 600; font-size: 14px; }
  .item-sub { font-size: 12px; color: #848e9c; }
  .item-price { text-align: right; font-weight: 600; font-size: 14px; }
  .green { color: #0ecb81; } .red { color: #f6465d; }

  /* Buttons */
  .btn { width: 100%; background: #ab9ff2; color: #000; font-weight: bold; padding: 12px; border: none; border-radius: 10px; cursor: pointer; text-align: center; }
  .btn-buy { background: #0ecb81; color: #fff; flex: 1; }
  .btn-sell { background: #f6465d; color: #fff; flex: 1; }
  .btn-group { display: flex; gap: 10px; }

  /* Admin Control Panel */
  .admin-panel { width: 100%; max-width: 380px; margin-top: 15px; background: #161a22; padding: 15px; border-radius: 12px; border: 1px solid #2d323e; }
  .admin-title { font-size: 14px; font-weight: bold; margin-bottom: 10px; color: #ab9ff2; }
  .input-field { width: 100%; padding: 8px; margin-bottom: 8px; background: #0b0e11; border: 1px solid #2b303c; color: white; border-radius: 6px; }

  /* Bottom Nav */
  .bottom-nav { display: flex; background: #181c24; border-top: 1px solid #252a34; position: absolute; bottom: 0; width: 100%; }
  .nav-item { flex: 1; text-align: center; padding: 12px 0; font-size: 11px; color: #848e9c; cursor: pointer; }
  .nav-item.active { color: #ab9ff2; font-weight: bold; }
</style>
</head>
<body>

<div class="phone-screen">
  <!-- PHANTOM APP -->
  <div id="phantom" class="screen active">
    <div class="app-header">👻 Phantom</div>
    <div class="card">
      <div class="balance-title">Account Balance</div>
      <div class="balance-val" id="disp-phantom">$0.01</div>
    </div>
    <button class="btn">Deposit</button>
    <div style="font-weight: bold; margin-top: 5px;">Explore Markets</div>
    <div class="item-row">
      <div><div class="item-name">Diamond</div><div class="item-sub">$1M MC</div></div>
      <div class="item-price">$0.0010979</div>
    </div>
    <div class="item-row">
      <div><div class="item-name">ANSEM</div><div class="item-sub">$54M MC</div></div>
      <div class="item-price">$0.0535</div>
    </div>
    <div class="item-row">
      <div><div class="item-name">BIRB</div><div class="item-sub">$28M MC</div></div>
      <div class="item-price">$0.0979</div>
    </div>
  </div>

  <!-- MT5 APP -->
  <div id="mt5" class="screen">
    <div class="app-header">📈 MetaTrader 5</div>
    <div class="card">
      <div class="balance-title">Balance / Equity</div>
      <div class="balance-val" id="disp-mt5">$5,250.00</div>
    </div>
    <div class="item-row">
      <div><div class="item-name">XAUUSDz</div><div class="item-sub">Gold vs US Dollar</div></div>
      <div class="item-price green">4401.89<sup>6</sup></div>
    </div>
    <div class="item-row">
      <div><div class="item-name">BTCUSDz</div><div class="item-sub">Bitcoin</div></div>
      <div class="item-price red">78332.31</div>
    </div>
    <div class="btn-group" style="margin-top: 15px;">
      <button class="btn btn-buy">SELL</button>
      <button class="btn btn-sell">BUY</button>
    </div>
  </div>

  <!-- PUMPFUN / FOMO APP -->
  <div id="fomo" class="screen">
    <div class="app-header">🚀 Pumpfun / Fomo</div>
    <div class="card">
      <div class="balance-title">Wallet Balance</div>
      <div class="balance-val" id="disp-fomo">$1,420.50</div>
    </div>
    <div style="font-weight: bold; margin-top: 5px;">Trending Tokens</div>
    <div class="item-row">
      <div><div class="item-name">NIO</div><div class="item-sub">$1.79M MC</div></div>
      <div class="item-price green">+82.23%</div>
    </div>
    <div class="item-row">
      <div><div class="item-name">WHITE</div><div class="item-sub">$401K MC</div></div>
      <div class="item-price green">+9,490.45%</div>
    </div>
  </div>

  <!-- Bottom Navigation -->
  <div class="bottom-nav">
    <div class="nav-item active" onclick="switchApp('phantom', this)">👻 Phantom</div>
    <div class="nav-item" onclick="switchApp('mt5', this)">📈 MT5</div>
    <div class="nav-item" onclick="switchApp('fomo', this)">🚀 Fomo</div>
  </div>
</div>

<!-- Admin Control Panel -->
<div class="admin-panel">
  <div class="admin-title">⚡ Real-Time Balance Control</div>
  <select id="target-app" class="input-field">
    <option value="phantom">Phantom Wallet</option>
    <option value="mt5">MT5 Account</option>
    <option value="fomo">Fomo Balance</option>
  </select>
  <input type="number" id="new-bal" class="input-field" placeholder="Enter new amount ($)">
  <button class="btn" style="background: #0ecb81; color: white;" onclick="updateBalance()">Update Screen Balance</button>
</div>

<script>
  function switchApp(appId, el) {
    document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
    document.getElementById(appId).classList.add('active');
    el.classList.add('active');
  }

  function updateBalance() {
    const target = document.getElementById('target-app').value;
    const val = parseFloat(document.getElementById('new-bal').value);
    if (!isNaN(val)) {
      document.getElementById('disp-' + target).innerText = '$' + val.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2});
    }
  }
</script>

</body>
</html>
"""

components.html(html_code, height=850, scrolling=True)

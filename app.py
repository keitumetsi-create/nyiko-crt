import streamlit as st
st.set_page_config(page_title="Nyiko CRT - 4H", page_icon="👑", layout="centered")
st.markdown("<h1 style='text-align:center;color:#FFD700;'>👑 Nyiko CRT 4H</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Tells you BUY or SELL + When</p>", unsafe_allow_html=True)
timeframe = st.selectbox("Timeframe:", ["4H (Your Style)", "H1", "D1"])
instrument = st.selectbox("Pair:", ["XAUUSD", "NAS100", "US30", "GBPUSD", "EURUSD"])
c1, c2 = st.columns(2)
with c1:
    high = st.number_input("Candle High", value=0.0, format="%.2f")
with c2:
    low = st.number_input("Candle Low", value=0.0, format="%.2f")
current = st.number_input("Current Price NOW", value=0.0, format="%.2f")
if high > 0 and low > 0 and current > 0 and high > low:
    rng = high - low
    fifty = low + rng*0.5
    q25 = low + rng*0.25
    q75 = low + rng*0.75
    if (instrument=="XAUUSD" and rng<7) or (instrument in ["NAS100","US30"] and rng<70):
        st.warning("### ⛔ NO CRT TODAY - Range too small, DON'T TRADE")
        st.stop()
    st.divider()
    st.write(f"**50%: {fifty:.2f} | 25%: {q25:.2f} | 75%: {q75:.2f}**")
    st.divider()
    if current <= q25:
        st.success(f"## 🟢🟢 STRONG BUY NOW - {instrument}")
        st.success(f"Price at Discount (Below 25%)")
        st.write(f"👉 ACTION: BUY NOW at {current}")
        st.write(f"🎯 TP1: {fifty:.2f}")
        st.write(f"🎯 TP2: {high:.2f}")
        st.write(f"🛑 SL: {low - (rng*0.1):.2f}")
        st.balloons()
    elif current < fifty and current > q25:
        st.success(f"## 🟢 BUY BIAS - Wait M15")
        st.write(f"👉 ACTION: Look for BUY around {current}")
        st.write(f"🎯 TP: {fifty:.2f} -> {high:.2f}")
        st.write(f"🛑 SL: Below {low:.2f}")
    elif current >= q75:
        st.error(f"## 🔴🔴 STRONG SELL NOW - {instrument}")
        st.error(f"Price at Premium (Above 75%)")
        st.write(f"👉 ACTION: SELL NOW at {current}")
        st.write(f"🎯 TP1: {fifty:.2f}")
        st.write(f"🎯 TP2: {low:.2f}")
        st.write(f"🛑 SL: {high + (rng*0.1):.2f}")
    elif current > fifty and current < q75:
        st.error(f"## 🔴 SELL BIAS - Wait M15")
        st.write(f"👉 ACTION: Look for SELL around {current}")
        st.write(f"🎯 TP: {fifty:.2f} -> {low:.2f}")
        st.write(f"🛑 SL: Above {high:.2f}")
    else:
        st.warning(f"### ⚠️ PRICE AT 50% - NO ENTRY YET")
        st.write(f"Wait for price to go to 25% for BUY or 75% for SELL")
    st.divider()
    st.info(f"💡 4H Rule: Buy below 50%, Sell above 50%")
st.caption("Nyiko | Education only")

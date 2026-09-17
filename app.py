import streamlit as st

st.set_page_config(page_title="Nyiko CRT - 4H Reader", page_icon="👑", layout="centered")

st.markdown("<h1 style='text-align:center;color:#FFD700;'>👑 Nyiko CRT - 4H Reader</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>4H with Safety Filter</p>", unsafe_allow_html=True)

timeframe = st.selectbox("Select Timeframe you use:", ["4H (Your Style)", "H1", "D1 - Daily"])
instrument = st.selectbox("Instrument:", ["XAUUSD (Gold)", "NAS100 / US30", "Forex Majors"])

col1, col2 = st.columns(2)
with col1:
    high = st.number_input(f"{timeframe} High", value=0.0, format="%.2f")
with col2:
    low = st.number_input(f"{timeframe} Low", value=0.0, format="%.2f")

current = st.number_input("Current Price", value=0.0, format="%.2f")

if high > 0 and low > 0 and current > 0:
    if high <= low:
        st.error("High must be bigger than Low!")
    else:
        range_size = high - low
        
        # SAFETY FILTER
        is_no_crt = False
        if instrument == "XAUUSD (Gold)" and range_size < 7:
            is_no_crt = True
            min_range = 7
        elif instrument == "NAS100 / US30" and range_size < 70:
            is_no_crt = True
            min_range = 70
        elif instrument == "Forex Majors" and range_size < 0.0008 * current:
            is_no_crt = True
        
        st.divider()
        
        if is_no_crt:
            st.warning(f"### ⛔ NO CRT - NO TRADE")
            st.write(f"Range is only {range_size:.2f} - too small!")
            st.write(f"Wait for next {timeframe} candle. Market is choppy.")
            st.info("Pro traders skip this. Save your money!")
        else:
            fifty = low + (range_size * 0.5)
            quarter = low + (range_size * 0.25)
            three_quarter = low + (range_size * 0.75)
            
            st.subheader("📊 CRT Levels")
            c1, c2, c3 = st.columns(3)
            c1.metric("25%", f"{quarter:.2f}")
            c2.metric("50% - KEY", f"{fifty:.2f}")
            c3.metric("75%", f"{three_quarter:.2f}")

            st.divider()
            if current < fifty:
                st.success(f"### 🟢 BUY BIAS - {timeframe}")
                st.write(f"**Target 1:** {fifty:.2f}")
                st.write(f"**Target 2:** {high:.2f}")
                st.write(f"**SL:** Below {low:.2f}")
            else:
                st.error(f"### 🔴 SELL BIAS - {timeframe}")
                st.write(f"**Target 1:** {fifty:.2f}")
                st.write(f"**Target 2:** {low:.2f}")
                st.write(f"**SL:** Above {high:.2f}")

st.divider()
st.caption("Nyiko CRT | Not financial advice")
        st.divider()
        if current < fifty:
            st.success(f"### 🟢 BUY BIAS - {timeframe}")
            st.write(f"**Entry:** Around {current}")
            st.write(f"**Target 1:** {fifty:.2f} (50%)")
            st.write(f"**Target 2:** {high:.2f} (High)")
            st.write(f"**Stop Loss:** Below {low:.2f}")
            st.info("Wait for M15/M5 bullish market structure / FVG before entering!")
        else:
            st.error(f"### 🔴 SELL BIAS - {timeframe}")
            st.write(f"**Entry:** Around {current}")
            st.write(f"**Target 1:** {fifty:.2f} (50%)")
            st.write(f"**Target 2:** {low:.2f} (Low)")
            st.write(f"**Stop Loss:** Above {high:.2f}")
            st.info("Wait for M15/M5 bearish market structure / FVG before entering!")

st.divider()
st.link_button("💬 Join WhatsApp Signals", "https://wa.me/your_number", use_container_width=True)
st.caption("Nyiko CRT | Not financial advice - For education only")

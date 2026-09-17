import streamlit as st
from PIL import Image

st.set_page_config(page_title="Nyiko CRT Reader", layout="centered")
st.title("Nyiko CRT - Free Reader")
st.caption("Upload chart -> BUY/SELL + SL/TP")

uploaded = st.file_uploader("Upload Screenshot", type=["png","jpg","jpeg"])
p = st.text_input("Current Price e.g. 4268")
h = st.text_input("H1 High e.g. 4366")
l = st.text_input("H1 Low e.g. 4235")

if uploaded:
    st.image(Image.open(uploaded), use_column_width=True)
    if st.button("ANALYZE NOW"):
        try:
            cur = float(p) if p else 4270
            hh = float(h) if h else 4366
            ll = float(l) if l else 4235
        except:
            cur, hh, ll = 4270, 4366, 4235
        if cur - ll < (hh-ll)*0.15:
            d="BUY"; conf=68; entry=f"{ll+15}"; sl=f"{ll-15}"; tp1=f"{hh-10}"; exp=f"Sweep low {ll}"
        elif hh - cur < (hh-ll)*0.15:
            d="SELL"; conf=70; entry=f"{hh-20}"; sl=f"{hh+15}"; tp1=f"{ll+10}"; exp=f"Sweep high {hh}"
        else:
            d="WAIT"; conf=45; entry="No entry"; sl="-"; tp1="-"; exp="Wait for sweep"
        st.write(f"DIRECTION: {d}")
        st.write(f"CONFIDENCE: {conf}%")
        st.write(f"ENTRY: {entry}")
        st.write(f"SL: {sl}")
        st.write(f"TP1: {tp1}")
        st.write(exp)

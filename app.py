import streamlit as st

st.set_page_config(page_title="TIEMPO MUERTO", page_icon="⏱️", layout="centered")

st.title("⏱️ Downtime Calculator")
st.caption("Convierte minutos de tiempo muerto a horas decimales (y viceversa).")

st.divider()

mode = st.radio(
    "Modo",
    ["Minutos → Horas decimales", "Horas decimales → Minutos"],
    horizontal=True
)

if mode == "Minutos → Horas decimales":
    minutes = st.number_input(
        "Minutos de tiempo muerto",
        min_value=0,   # int
        step=1,        # int
        value=90       # int
    )
    hours = minutes / 60.0

    st.metric("Horas decimales", f"{hours:.1f}")
    st.write(f"**{minutes} min** = **{hours:.1f} h**")

    st.caption("Tip: 15 min = 0.25 h • 30 min = 0.5 h • 45 min = 0.75 h • 90 min = 1.5 h")

else:
    hours = st.number_input(
        "Horas decimales de tiempo muerto",
        min_value=0.0,
        step=0.25,
        value=1.5
    )
    minutes = hours * 60.0

    st.metric("Minutos", f"{minutes:.0f}")
    st.write(f"**{hours:.1f} h** = **{minutes:.0f} min**")

st.divider()
st.caption("Solo como referencia 😄")

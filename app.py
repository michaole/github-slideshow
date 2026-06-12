import streamlit as st
import pathlib

st.set_page_config(page_title="Judo 5.5 KYU – Fiszki", page_icon="🥋", layout="centered")

html = pathlib.Path("flashcards.html").read_text(encoding="utf-8")
st.components.v1.html(html, height=750, scrolling=True)

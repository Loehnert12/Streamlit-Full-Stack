import streamlit as st
from datetime import date

st.set_page_config(page_title = "Date Difference Calulator")

st.header("Please login to access the calculator.")

title = st.text_input("Username", "")
title = st.text_input("Password", "")
import streamlit as st
from datetime import date

st.set_page_config(page_title = "Date Difference Calulator")

st.header("This is my basic application!")
st.subheader("Lets figure out a day difference calculation.")
st.write("NOTE: If you select 01/01/2025 as a start date and 01/15/2025 as the end date, that is only 14 days NOT 15 days")

st.header("Select your starting date.")

start_date = st.date_input(
    "Pick a start date",
    value = date.today(),
    min_value = date(2000, 1, 1),
    max_value = date (2100, 12, 31),
    key = "start_date"
)

st.write(f"Start date: {start_date:%B %d, %Y}")

end_date = st.date_input(
    "Pick an end date",
    value = date.today(),
    min_value = date(2000, 1, 1),
    max_value = date (2100, 12, 31),
    key = "end_date"
)

st.write(f"End date: {end_date:%B %d, %Y}")

if start_date > end_date:
    st.error("The start date has to be before the end date. Please double check the dates. :)")
else:
    day_diff = (end_date - start_date).days
    st.header(f"It has been {day_diff} days since {start_date:%B %d, %Y}")
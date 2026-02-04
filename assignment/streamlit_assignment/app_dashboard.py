import streamlit as st

st.title("Simple Sales Dashboard")
st.subheader("This is a simple sales dashboard")

months = st.selectbox("Select a month", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 400,
    "May": 500,
    "June": 2100,
    "July": 700,
    "August": 1580,
    "September": 900,
    "October": 1000,
    "November": 1600,
    "December": 1200
}

st.metric("Sales for the selected month :",months, sales[months])
st.bar_chart(sales.values(),y_label="Sales",x_label="Months,")





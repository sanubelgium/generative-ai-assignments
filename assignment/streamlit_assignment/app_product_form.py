import streamlit as st

st.sidebar.header("Product Form")

product_name = st.sidebar.text_input("Product Name")
product_category = st.sidebar.selectbox("Category", ["Electronics", "Clothing", "Books", "Home & Kitchen"])
product_price = st.sidebar.number_input("Product Price", min_value=0.0, step=0.01)

if st.sidebar.button("Add Product"):
    st.success("Product Added Successfully")
    st.write("Product Name: ", product_name)
    st.write("Product Category: ", product_category)
    st.write("Product Price: ", product_price)
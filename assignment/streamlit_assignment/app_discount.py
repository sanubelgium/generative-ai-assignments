import streamlit as st

st.title("Discount Calculator")

price = st.number_input("Enter the product price")
discount = st.slider("Enter the discount percentage", min_value=0, max_value=50)

if st.button("Calculate Discounted Price"):
    discount_amount = price * (discount / 100)
    final_price = price - discount_amount
    
    st.success("Final Price: " + str(final_price))
    
    st.write("Example:")
    st.write("Original Price: ", str(price))
    st.write("Discount: ", str(discount) + "%")
    st.write("Final Price: ", str(final_price))
    
    st.write("Price Comparison")
    
    comparison_data = {
        "Before": str(price),
        "After": str(final_price)
    }
    
    st.table(comparison_data)
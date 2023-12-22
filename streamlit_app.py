import streamlit as st

st.header('st.button')

if st.button('Hi'):
     st.write('Yes. Who are you??')
else:
     st.write('Goodbye')

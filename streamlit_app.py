import streamlit as st

st.header('st.button')

if st.button('Hi'):
     st.write('Yes. Who are you??')
     if st.button('Hii'):
         st.write('I am hearing you')
else:
     st.write('Goodbye')

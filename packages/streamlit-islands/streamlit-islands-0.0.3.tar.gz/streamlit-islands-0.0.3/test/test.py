import streamlit as st
import streamlit_islands as sti

def say_hello(name):
    st.write(name*10)

def add(a, b):
    if st.button('Show the result'):
        st.toast("The result is: " + str(a + b)) 

# Test the function
files = ["streamlit_islands/test.md", "README.md"]
for file in files:
    content1 = sti.load_content(file)
    st.markdown("---")
import streamlit as st

#   Sidebar
st.sidebar.header("Setting panel")
st.sidebar.checkbox(" Dar Mode",key = "dark mode")
st.sidebar("This is an example of how to use ")
col1,col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("This is the first column.")
with col2:
    st.header("Column 2")
    st.write("This is the second column.")
tab1, tab2 = st.tabs(["About Us", "Contact"])
with tab1:
    st.header("About.Us")
    st.write

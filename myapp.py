import streamlit as st
st.set_page_config(page_title='cartoon')
st.header("Types of Cartoons")

col1,col2=st.columns(2)
with col1:
  st.subheader("Jerry")
  st.image("http://clipart-library.com/images/kiKByzxoT.jpg",caption="Jerry",width=200,use_column_width=True)
  st.write("Jerry is soo cute")
  with col2:
    st.subheader("Dora")
  st.image("https://2.bp.blogspot.com/-RgxTTFbpAgY/UUCAUA7CS9I/AAAAAAAAGLU/TLqTuhXjhXc/s1600/16.png",caption="Dora",width=200,use_column_width=True)
  st.write("Dora is sweet")

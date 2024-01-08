import streamlit as st
st.set_page_config(page_title='cartoon')
st.header("Types of Cartoons")

col1,col2,col3=st.columns(4)
with col1:
  st.subheader("Jerry")
  st.image("http://clipart-library.com/images/kiKByzxoT.jpg",caption="Jerry",width=200,use_column_width=True)
  st.write("Jerry is soo cute")
with col2:
  st.subheader("Dora")
  st.image("https://2.bp.blogspot.com/-RgxTTFbpAgY/UUCAUA7CS9I/AAAAAAAAGLU/TLqTuhXjhXc/s1600/16.png",caption="Dora",width=200,use_column_width=True)
  st.write("Dora is sweet")
with col3:
  st.subheader("sinchan")
  st.image("https://media.tenor.com/7SE3IKEub60AAAAi/shinchan.gif",caption="shinchan",width=200,use_column_width=True)
  st.write("sinchan is naughty")
with col4:
  st.subheader("Motu and patlu")
  st.image("https://media.tenor.com/Itzu4p4UpU0AAAAM/gale-lag-yaara-motu.gif",caption="shinchan",width=200,use_column_width=True)
  st.write("motu and patlu  are funny")



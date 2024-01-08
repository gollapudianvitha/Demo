import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of Cats")

col1,col2=st.columns(2)
with col1:
  st.subheader("Persian Cat")
  st.image("https://cdn.fotofits.com/petzlover/gallery/img/l/persian-552570.jpg",caption="Persian Cat",width=300,use_column_width=True)
  st.write("Persian cats are cute")
  with col2:
    st.subheader("Ragdoll Cat")
  st.image("https://tse2.mm.bing.net/th?id=OIP.JWq61hdMTQvB-BjE_EIUcAHaHa&pid=Api&P=0&h=180",caption="Ragdoll Cat",width=300,use_column_width=True)
  st.write("Ragdoll cats are proud")

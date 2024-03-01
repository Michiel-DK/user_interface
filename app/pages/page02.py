import streamlit as st

spell = st.secrets['spell']
key = st.secrets.some_magic_api.key

st.write(spell)


st.write(key)
import pandas as pd
import streamlit as st
import requests


st.title("""Real estate estimator""")

rooms = st.slider('Set the number of rooms!', min_value=1, max_value=10, value=2)

st.write("""There are **{}** room in real estate!""".format(rooms))

area = st.slider('Set the property area!', min_value=20, max_value=200, value=50)

st.write(f"""The property area is **{area}**""")

balcony = st.slider(f'Set the balcony area!', min_value=0, max_value=50, value=0)

st.markdown(f"""<html>The balcony area is <b>{balcony}</b> m<sup>2</sup></html>""", unsafe_allow_html=True)


params = {'area': area, 'rooms': rooms, 'balcony': balcony}
pred = requests.get('http://fastapi:8000/pred', params=params)
pred = pred.json()

st.write(f"""""")
st.write(f"""""")
st.write(f'The real estate costs approx. **{pred["Pred"]:.2f}** million HUF.')





# app.py
import streamlit as st
import requests

st.title("Latest Temperature at KMDW")

url = "https://www.weather.gov/wrh/graphical/graphicalJSON.php?data=obs&site=kmdw"

try:
    res = requests.get(url).json()
    temp = res["data"]["temperature"][-1]
    time = res["data"]["time"][-1]
    st.metric(label="Temperature (°F)", value=temp)
    st.write(f"Updated at: {time}")
except Exception as e:
    st.error(f"Failed to fetch temperature: {e}")

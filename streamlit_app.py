import streamlit as st
import requests

st.title("Latest Temperature at KMDW")

url = "https://www.weather.gov/wrh/graphical/graphicalJSON.php?data=obs&site=kmdw"
headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    data = res.json()

    temp = data["data"]["temperature"][-1]
    time = data["data"]["time"][-1]

    st.metric(label="Temperature (°F)", value=temp)
    st.write(f"Updated at: {time}")
except Exception as e:
    st.error(f"Failed to fetch temperature: {e}")

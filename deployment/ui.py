import streamlit as st
import requests
import json

st.title("🔧 Vehicle Failure Prediction System")

st.write("Enter engine sensor values to predict failure risk")

# Example input field (simple version)
input_json = st.text_area(
    "Paste JSON Input",
    height=300,
    placeholder='{"sensor_1": 518.67, "sensor_2": 641.82, "...": "..."}'
)

if st.button("Predict Failure"):
    try:
        payload = json.loads(input_json)

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        result = response.json()

        st.success("Prediction Successful")
        st.json(result)

    except Exception as e:
        st.error(f"Error: {e}")

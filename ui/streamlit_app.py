import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="Fake News Detector", page_icon="🕵️")

st.title("🕵️ IP-Aware Fake News Detector")
st.markdown("Predict if a news article is **REAL** or **FAKE** based on content and source IP.")

# Inputs
news_text = st.text_area("Enter News Article Content", height=200, placeholder="Paste article text here...")
ip_address = st.text_input("Enter Source IP Address", placeholder="e.g., 192.168.1.1")

if st.button("Analyze News"):
    if not news_text or not ip_address:
        st.warning("Please provide both news text and IP address.")
    else:
        with st.spinner("Analyzing content and checking IP reputation..."):
            try:
                payload = {"text": news_text, "ip_address": ip_address}
                response = requests.post(API_URL, json=payload)
                
                if response.status_code == 200:
                    result = response.json()
                    pred = result["prediction"]
                    conf = result["confidence"]
                    
                    if pred == "FAKE":
                        st.error(f"🚨 **Prediction: FAKE NEWS**")
                        st.write(f"Confidence: {conf:.2%}")
                    else:
                        st.success(f"✅ **Prediction: REAL NEWS**")
                        st.write(f"Confidence: {conf:.2%}")
                else:
                    st.error(f"Error: {response.json().get('detail', 'Unknown API error')}")
            except requests.exceptions.ConnectionError:
                st.error("❌ Could not connect to the API. Ensure the backend is running.")

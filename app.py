import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# App layout
st.set_page_config(page_title="SmartSolar Recommender", page_icon="☀️", layout="centered")

st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
        }
        h1 {
            color: #1a4d2e;
            font-size: 42px;
        }
        .stButton > button {
            background-color: #1a4d2e;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("## ☀️ **SmartSolar Recommender**")
st.markdown("### Should you invest in solar panels? Enter your info to find out.")

# Input fields
income = st.number_input("💰 Monthly Income (USD)", min_value=0.0, step=50.0)
energy = st.number_input("⚡ Energy Consumed (kWh)", min_value=0.0, step=10.0)
co2 = st.number_input("🌍 CO₂ Emissions (kg)", min_value=0.0, step=5.0)

# Predict button
if st.button("🔍 Predict Recommendation"):
    input_data = np.array([[income, energy, co2]])
    prediction = model.predict(input_data)[0]

    # Display result
    if prediction == 2:
        st.success("✅ **High Likelihood of Purchase** — You’re a strong candidate for solar investment!")
    elif prediction == 1:
        st.info("⚠️ **Moderate Likelihood of Purchase** — Consider solar panels based on further analysis.")
    else:
        st.warning("❌ **Low Likelihood of Purchase** — Solar panels may not be the best fit right now.")



import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import date

# Load Firebase credentials
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_config.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

st.set_page_config(page_title="CarbonWise", page_icon="🌱")
st.title("🌍 CarbonWise - Track Your Carbon Footprint")

st.markdown("**Enter your daily activity to calculate your carbon emissions.**")

# Input Section
travel = st.selectbox("Travel Mode", ["None", "Bike", "Bus", "Car"])
distance = st.slider("Distance Travelled (km)", 0, 100, 10)
meal = st.selectbox("Meal Type", ["Veg", "Non-Veg", "Vegan"])
electricity = st.slider("Electricity Used (kWh)", 0, 50, 5)

# Emission Calculator
def calculate_emissions(travel, distance, meal, electricity):
    travel_emission = {
        "None": 0,
        "Bike": 0,
        "Bus": distance * 0.1,
        "Car": distance * 0.21
    }[travel]

    meal_emission = {
        "Veg": 1,
        "Non-Veg": 3,
        "Vegan": 0.5
    }[meal]

    electricity_emission = electricity * 0.92
    return round(travel_emission + meal_emission + electricity_emission, 2)
# Suggestions
def get_suggestions(travel, meal, electricity):
    tips = []
    if travel == "Car":
        tips.append("🚴 Try using public transport or cycling.")
    if meal == "Non-Veg":
        tips.append("🥗 Consider switching to a plant-based diet twice a week.")
    if electricity > 20:
        tips.append("💡 Reduce appliance usage and switch to LED lights.")
    return tips

# Submit & Display
if st.button("Submit"):
    emission = calculate_emissions(travel, distance, meal, electricity)
    tips = get_suggestions(travel, meal, electricity)

    log = {
        "date": str(date.today()),
        "travel": travel,
        "distance": distance,
        "meal": meal,
        "electricity": electricity,
        "emission": emission,
        "suggestions": tips
    }

    db.collection("carbon_logs").add(log)

    st.success(f"✅ Your estimated carbon emission: {emission} kg CO₂")

    st.markdown("### 🌟 Tips to Reduce Emissions")
    for tip in tips:
        st.info(tip)

    if emission < 5:
        st.balloons()
        st.success("🏅 You've earned the Eco Starter Badge!")


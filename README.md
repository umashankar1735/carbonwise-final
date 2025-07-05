# 🌱 CarbonWise — Personal Carbon Footprint Tracker

> A smart, gamified tracker that empowers individuals to monitor and reduce their carbon footprint — built with Python, Streamlit, and Firebase.

---

## 🧠 Problem Statement

Climate change is an urgent global issue, but most people are unaware of how their **daily activities** — like transportation, food choices, and electricity use — contribute to carbon emissions. Without visibility into their impact, it's difficult for individuals to make more sustainable decisions.

---

## 💡 Our Solution

**CarbonWise** is a simple, intuitive web app that allows users to:

- **Log everyday activities** like travel, meals, and energy usage
- **Calculate real-time carbon emissions**
- **Receive actionable, AI-powered sustainability tips**
- **Track personal goals** and earn eco-badges through gamification
- **Visualize progress** and feel rewarded for living greener

> CarbonWise isn't just a tracker — it's your personal guide toward a cleaner, more responsible lifestyle.

---

## 🚀 Key Features

| Feature                             | Description                                                                 |
|------------------------------------|-----------------------------------------------------------------------------|
| 🧾 Activity Input                  | Users log travel (car, bike, bus), food (veg/non-veg), electricity usage    |
| 📊 Carbon Emission Estimator      | Calculates estimated CO₂ emissions based on standard conversion factors     |
| 💡 Personalized AI Suggestions    | Rule-based engine provides green alternatives (e.g., public transport)     |
| 🏆 Gamified Progress              | Earn badges and celebrate eco-friendly habits                              |
| 🔥 Firebase Integration           | All logs are stored in Firestore in real time                              |
| ✅ Streamlit UI                   | Lightweight, clean, responsive interface                                   |

---

## 🧑‍💻 Tech Stack

| Layer       | Tech                         |
|-------------|------------------------------|
| Frontend    | [Streamlit](https://streamlit.io/) |
| Backend     | [Firebase Firestore](https://firebase.google.com/docs/firestore) |
| Auth        | Firebase Auth (Future Scope) |
| Hosting     | Streamlit Cloud / Local      |
| Language    | Python 3.x                   |

---

## 📦 How to Run the Project Locally

### 🔧 Prerequisites

- Python 3.x installed
- Firebase Firestore project set up
- `firebase_config.json` downloaded from Firebase (Service Account)

---

### 🚀 Running the App

```bash
# Step 1: Install required packages
pip install streamlit firebase-admin

# Step 2: Place firebase_config.json in the project root (DO NOT push to GitHub)

# Step 3: Run the app
streamlit run streamlit_app.py
```

🔐 Security Note
The file firebase_config.json is intentionally excluded from this repository. It contains sensitive credentials and must never be shared or pushed to version control.

This file should be added to .gitignore (already handled in this repo).

🎯 Future Enhancements
✅ Google/Firebase login (for personalized dashboards)

📈 Emission history and charts

🛰️ Automatic activity capture using location and sensors

🧠 Integrate with real-time AI for adaptive suggestions

🌍 Public leaderboard and community challenges


👨‍💻 Developed By
Team Quantumania
🎓 Amrita Vishwa Vidyapeetam

👤 K. Sai Uma Shankar
👤 A. Harshitha
👤 M. Rahul
👤 G. Harmila
Team Lead MAIL📧 ksaiumashankar@gmail.com



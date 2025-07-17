# 🔋 EV Pulse NXT — Predict Smarter. Drive Farther.

> An AI-powered EV battery life prediction system using Machine Learning, Flask, and HTML+CSS — deployed on Hugging Face Spaces.

![istockphoto-2163729535-612x612](https://github.com/user-attachments/assets/acfb22e8-cb6a-41f9-9cab-d9d82dfd7718)


---


## 🚀 Overview

**EV Pulse NXT** is an AI-powered battery analytics system designed to extend the life and performance of electric vehicle (EV) batteries. Built with a Flask backend and a user-friendly Streamlit interface, EV Pulse leverages machine learning to predict Remaining Useful Life (RUL), detect early signs of battery degradation, and classify charging behaviors for optimal performance.

With the rise of EV adoption and the need for smarter energy usage, EV Pulse NXT provides users, researchers, and fleet operators with actionable insights from real-world battery data. Whether you're concerned about overcharging, unexpected wear, or simply optimizing energy consumption, EV Pulse empowers you with intelligent forecasting and decision support.


---

## 🧠 Key Features

### 🔹 1. Battery Life Prediction Engine
- Predicts **Remaining Useful Life (RUL)** using Random Forest Regressor
- Analyzes real-world battery parameters:
  - EV Model
  - Battery Type
  - Battery temperature
  - Charging Duration
  - Charging Mode
  - Charging Cycles
  - Degradation Rate
  - Efficiency (%)

### 🔹 2. Smart Charging Classifier
- Categorizes charging sessions:
  - ✅ Balanced (Optimal)
  - ⚠️ Undercharged
  - ❌ Overcharged

### 🔹 3. Degradation Analysis
- Detects signs of early battery wear
- Visualizes trends in degradation over time

### 🔹 4. Streamlit Dashboard + Flask API
- Upload CSV → Get predictions instantly
- Visualizations include:
  - Line plot: Actual vs Predicted RUL
  - Heatmaps, Histograms, Box Plots
- REST API powered by Flask
- Hosted on Hugging Face Spaces

---


## 🧩 Tech Stack

| Layer            | Technology Used                            |
|------------------|---------------------------------------------|
| Frontend         | HTML+CSS (Web UI)                          |
| Backend          | Flask (REST API)                            |
| ML / AI          | Scikit-learn (Random Forest)                |
| Deployment       | Hugging Face Spaces                         |
| Visualization    | Matplotlib, Seaborn, Plotly                 |
| Data Handling    | Pandas, NumPy                               |

---

## ⚙️ ML Pipeline

**🔢 Input Features:**
- EV Model
- Battery Type
- Battery temperature
- Charging Duration
- Charging Mode
- Charging Cycles
- Degradation Rate
- Efficiency (%)

**🛠️ Workflow:**
1. Data Preprocessing (cleaning, encoding, scaling)
2. Model Training: Random Forest Regressor
3. Evaluation & Metrics
4. Classification: Optimal Charging Class
5. Flask API & Streamlit Dashboard Integration

---

## 🖼️ Screenshots

<img width="1280" height="2856" alt="Screenshot_20250715_154014" src="https://github.com/user-attachments/assets/faea2c41-a5c2-4530-b067-d8be05c9fbfa" />


---

## 📈 Results

- R² Score: ~0.92+ on test data
- Balanced accuracy for charging classifier: ~90%
- Real-time feedback on battery health and life

---

## 📅 Roadmap

- [x] RUL Prediction Model (Random Forest)
- [x] Charging Duration Classifier
- [x] Streamlit UI & Flask Integration
- [x] Hugging Face Deployment
- [ ] Live sensor/IoT data integration
- [ ] Export API for mobile app integration

---

## 🙌 Inspiration

> “Battery is the heart of your EV. Our mission: make it last longer using AI.”

EV Pulse NXT was inspired by the growing need for intelligent battery management systems in the Indian EV market. It combines cognitive models, real data, and intuitive design to empower every EV owner.

---




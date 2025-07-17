🔋 EV Pulse — Predict Smarter. Drive Farther.

🧠 An AI-powered battery analytics tool that predicts EV battery life, detects early degradation, and recommends smart charging behavior using machine learning and Flask.
![istockphoto-2163729535-612x612](https://github.com/user-attachments/assets/e2312ff9-e208-4bbd-b954-a6d94644d8a7)


🚀 Overview
EV Pulse is your electric vehicle’s predictive assistant — built with Flask for a lightweight backend and deployed via Hugging Face Spaces for seamless access. It empowers EV users to monitor battery health, forecast remaining useful life (RUL), and make informed decisions about charging, using real EV telemetry data and machine learning insights.

Whether you’re an EV driver, fleet manager, or energy researcher, EV Pulse helps you understand, preserve, and optimize your battery.

🧠 Key Features
1️⃣ Battery Life Prediction Engine
🔍 Uses a trained Random Forest Regressor
📊 Predicts Remaining Useful Life (RUL) in cycles or hours
🧾 Input features include:

State of Charge (SOC %), Voltage, Current

Battery & Ambient Temperature

Charging Duration, Efficiency

Battery Type, EV Model, Charging Mode, Degradation Rate

2️⃣ Charging Duration Classifier
⚡ Classifies a charging session as:

Undercharged

Balanced (Optimal)

Overcharged
🧠 Helps users adopt healthy charging habits for battery longevity

3️⃣ Battery Degradation Analysis
📉 Detects early degradation based on charging cycles & performance metrics
🔔 Warns if battery health trends indicate unusual wear

4️⃣ Web Dashboard + API Access
🌐 Web interface built with Streamlit
🔌 Backend powered by Flask
🚀 Hosted on Hugging Face Spaces
📈 Offers:

Interactive plots (RUL predictions, heatmaps, boxplots)

Real-time inference

Upload CSV and get instant results

🧩 Tech Stack
Layer	Technology Used
Frontend	HTML+CSS (Web UI)
Backend	Flask (REST API)
Machine Learning	Scikit-learn (Random Forest, Classifier)
Deployment	Hugging Face Spaces, GitHub
Data Handling	Pandas, NumPy, CSV
Visualization	Matplotlib, Seaborn, Plotly

⚙️ ML Pipeline
🔢 Input Features:
EV Model 

Battery Type 

Battery temperature 

Charging Duration 

Charging Mode 

Charging Cycles 

Degradation Rate 

Efficiency (%)

🛠️ Pipeline Steps:
Data preprocessing (cleaning, encoding, scaling)

Train/test split

Model training using Random Forest Regressor

Classification model for charging behavior

Model evaluation & export

🔍 Output:
Remaining battery life (in cycles)

Optimal charging category

Visual insights via dashboard

🧪 Demo & Screenshots
![android2](https://github.com/user-attachments/assets/e11339b9-c736-4a36-9ea7-8d6cbd6153f7)



📈 Roadmap
✅ Model training and evaluation

✅ HTML+CSS (web interface)

✅ Flask backend with prediction API

✅ Deployment on Hugging Face Spaces

🔜 Add live battery data integration (via mobile or IoT)

🔜 Export model as mobile-ready API

🧠 Inspiration
“Battery is the heart of your EV. Our mission: make it last longer with AI.”

Inspired by the growing demand for EV maintenance tools, EV Pulse was built to empower users with foresight — not just analytics. Combining practical engineering, real user data, and ML models, it brings transparency to battery life management

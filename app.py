from flask import Flask, request, render_template
import numpy as np
import joblib

app = Flask(__name__)

# Load trained model (expects 8 numeric features)
model = joblib.load('battery_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Directly read all numeric input values from the form
        battery_temp = float(request.form['battery_temp'])
        charging_duration = float(request.form['charging_duration'])
        degradation_rate = float(request.form['degradation_rate'])
        charging_mode = float(request.form['charging_mode'])     # already label encoded
        efficiency = float(request.form['efficiency'])
        battery_type = float(request.form['battery_type'])       # already label encoded
        charging_cycles = float(request.form['charging_cycles'])
        ev_model = float(request.form['ev_model'])               # already label encoded

        # Create input array for prediction
        input_data = np.array([[battery_temp, charging_duration, degradation_rate,
                                charging_mode, efficiency, battery_type,
                                charging_cycles, ev_model]])

        # Make prediction
        prediction = model.predict(input_data)

        return render_template('index.html', prediction_text=f'Predicted Battery Life: {prediction[0]:.2f} hours')

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {e}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
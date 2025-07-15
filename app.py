from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  # ✅ allow POST
def index():
    prediction_text = ""
    if request.method == 'POST':
        # Get form inputs
        battery_temp = request.form['battery_temp']
        charging_duration = request.form['charging_duration']
        degradation_rate = request.form['degradation_rate']
        charging_mode = request.form['charging_mode']
        efficiency = request.form['efficiency']
        battery_type = request.form['battery_type']
        charging_cycles = request.form['charging_cycles']
        ev_model = request.form['ev_model']

        # Dummy prediction logic (replace with your ML model)
        prediction_text = f"Predicted battery life: {100 - float(degradation_rate):.2f} hours"

    return render_template('index.html', prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)

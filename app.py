from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Dummy model logic (replace with your model)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        seconds = float(request.form['seconds'])
        lat = float(request.form['latitude'])
        lon = float(request.form['longitude'])
        prediction = "USA"  # Dummy result
        return render_template('index.html', prediction_text=prediction)
    except Exception as e:
        return render_template('index.html', prediction_text="Error in input: " + str(e))

if __name__ == '__main__':
    app.run(debug=True)

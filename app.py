from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("ufo-model.pkl")


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        seconds = float(request.form['seconds'])
        lat = float(request.form['latitude'])
        lon = float(request.form['longitude'])

        # Prepare the input for prediction
        features = np.array([[seconds, lat, lon]])
        prediction = model.predict(features)[0]

        return render_template('index.html', prediction_text=prediction)
    except Exception as e:
        return render_template('index.html', prediction_text="Error: " + str(e))

if __name__ == '__main__':
    app.run(debug=True)

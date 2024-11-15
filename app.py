from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect all input features from the form
        features = [
            float(request.form['age']),
            float(request.form['sex']),
            float(request.form['cp']),
            float(request.form['trestbps']),
            float(request.form['chol']),
            float(request.form['fbs']),
            float(request.form['restecg']),
            float(request.form['thalach']),
            float(request.form['exang']),
            float(request.form['oldpeak']),
            float(request.form['slope']),
            float(request.form['ca']),
            float(request.form['thal'])
        ]

        # Convert input to a NumPy array with the required shape
        input_data = np.array([features])
        
        # Make prediction
        prediction = model.predict(input_data)

        # Interpret result
        result = "Heart Disease Detected" if prediction[0] == 1 else "No Heart Disease"
    
    except ValueError:
        # Error message for invalid inputs
        result = "Please enter valid numerical values for all fields."

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)
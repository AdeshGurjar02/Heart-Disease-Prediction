from flask import Flask, render_template, request
import pickle
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open('heart_disease_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the data from the form
        age = float(request.form['age'])
        sex = int(request.form['sex'])
        trestbps = float(request.form['trestbps'])
        chol = float(request.form['chol'])
        fbs = int(request.form['fbs'])
        thalach = float(request.form['thalach'])
        exang = int(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = int(request.form['slope'])
        ca = int(request.form['ca'])

        # Convert categorical features to one-hot encoding
        cp = int(request.form['cp'])
        restecg = int(request.form['restecg'])
        thal = int(request.form['thal'])
        
        # One-hot encode cp, restecg, and thal
        cp_1 = 1 if cp == 1 else 0
        cp_2 = 1 if cp == 2 else 0
        cp_3 = 1 if cp == 3 else 0
        restecg_1 = 1 if restecg == 1 else 0
        restecg_2 = 1 if restecg == 2 else 0
        thal_1 = 1 if thal == 1 else 0
        thal_2 = 1 if thal == 2 else 0
        thal_3 = 1 if thal == 3 else 0

        # Create a numpy array with the inputs
        features = np.array([[age, sex, trestbps, chol, fbs, thalach, exang, oldpeak, slope, ca, cp_1, cp_2, cp_3, restecg_1, restecg_2, thal_1, thal_2, thal_3]])

        # Use the model to predict
        prediction = model.predict(features)

        # Return the result
        if prediction[0] == 1:
            result = "High chance of heart disease"
        else:
            result = "Low chance of heart disease"
        
        return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)

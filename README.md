# Heart-Disease-Prediction
Heart Disease Prediction
Overview
This project provides a web application for predicting the likelihood of heart disease based on patient data. The application uses a machine learning model to analyze various health metrics and predict whether a patient is at high risk for heart disease.

Features
Web Interface: A simple and user-friendly web interface for entering patient data.
Prediction Model: Utilizes a trained machine learning model to predict the risk of heart disease.
Categorical Encoding: Converts categorical features into one-hot encoded format to be used by the model.
Results Display: Provides predictions with a clear message indicating high or low risk of heart disease.
Technologies Used
Flask: A lightweight WSGI web application framework in Python.
Scikit-Learn: For machine learning model training and prediction.
NumPy: For numerical operations.
HTML/CSS: For creating the web interface.
Python 3.10: The programming language used for development.
Installation
Clone the Repository
bash
Copy code
git clone https://github.com/username/heart-disease-prediction.git
Navigate to the Project Directory
bash
Copy code
cd heart-disease-prediction
Create a Virtual Environment (Optional but recommended)
bash
Copy code
python -m venv venv
Activate the Virtual Environment
Windows
bash
Copy code
venv\Scripts\activate
Mac/Linux
bash
Copy code
source venv/bin/activate
Install Dependencies
bash
Copy code
pip install -r requirements.txt
Run the Flask Application
bash
Copy code
python app.py
Usage
Open the Application Navigate to http://127.0.0.1:5000/ in your web browser.
Enter Patient Data Fill out the form with the required health metrics.
Submit the Form Click the "Predict" button to get the prediction result.
View Prediction The result will be displayed on the same page, indicating whether there is a high or low chance of heart disease.
Data
The model was trained on a dataset containing various health metrics. The features include:

Age
Sex
Chest Pain Type (cp)
Resting Blood Pressure (trestbps)
Cholesterol Level (chol)
Fasting Blood Sugar (fbs)
Resting Electrocardiographic Results (restecg)
Maximum Heart Rate (thalach)
Exercise Induced Angina (exang)
ST Depression (oldpeak)
Slope of Peak Exercise ST Segment (slope)
Number of Major Vessels Colored by Fluoroscopy (ca)
Thalassemia (thal)
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any questions or issues, please contact Adesh Gurjar at [your-email@example.com].

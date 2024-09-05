# Heart Disease Prediction

## Overview

This project provides a web application for predicting the likelihood of heart disease based on patient data. The application uses a machine learning model to analyze various health metrics and predict whether a patient is at high risk for heart disease.

## Features

- **Web Interface**: A simple and user-friendly web interface for entering patient data.
- **Prediction Model**: Utilizes a trained machine learning model to predict the risk of heart disease.
- **Categorical Encoding**: Converts categorical features into one-hot encoded format to be used by the model.
- **Results Display**: Provides predictions with a clear message indicating high or low risk of heart disease.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework in Python.
- **Scikit-Learn**: For machine learning model training and prediction.
- **NumPy**: For numerical operations.
- **HTML/CSS**: For creating the web interface.
- **Python 3.10**: The programming language used for development.

## Usage

   1. **Open the Application**
      Navigate to `http://127.0.0.1:5000/` in your web browser.
   
   2. **Enter Patient Data**
      Fill out the form with the required health metrics. The form fields include:
      - **Age**: Enter the patient's age.
      - **Sex**: Select the patient's sex (Male or Female).
      - **Chest Pain Type (cp)**: Select the type of chest pain (1, 2, or 3).
      - **Resting Blood Pressure (trestbps)**: Enter the resting blood pressure in mm Hg.
      - **Cholesterol Level (chol)**: Enter the cholesterol level in mg/dl.
      - **Fasting Blood Sugar (fbs)**: Enter whether the fasting blood sugar is greater than 120 mg/dl (1 for Yes, 0 for No).
      - **Maximum Heart Rate (thalach)**: Enter the maximum heart rate achieved.
      - **Exercise Induced Angina (exang)**: Enter whether there is exercise-induced angina (1 for Yes, 0 for No).
      - **ST Depression (oldpeak)**: Enter the ST depression induced by exercise relative to rest.
      - **Slope of Peak Exercise ST Segment (slope)**: Select the slope of the peak exercise ST segment (0, 1, or 2).
      - **Number of Major Vessels Colored by Fluoroscopy (ca)**: Enter the number of major vessels colored by fluoroscopy (0, 1, 2, or 3).
      - **Resting Electrocardiographic Results (restecg)**: Select the resting electrocardiographic result (0, 1, or 2).
      - **Thalassemia (thal)**: Select the thalassemia (1, 2, or 3).
   
   3. **Submit the Form**
      Click the "Predict" button to get the prediction result.
   
   4. **View Prediction**
      The result will be displayed on the same page, indicating whether there is a high or low chance of heart disease based on the input data.
   ## Contact

For any questions or issues related to this project, please feel free to reach out:

- **Name**: Adesh Gurjar
- **Email**: [codergurjar02@gmail.com](mailto:codergurjar02@gmail.com)
- **GitHub**: [github.com/AdeshGurjar02](https://github.com/AdeshGurjar02)
- **LinkedIn**: [linkedin.com/in/adesh-gurjar-65a287228](https://www.linkedin.com/in/adesh-gurjar-65a287228/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3Brj1hR%2B2GRkGp0NXzH1RJlw%3D%3D)

You can also report issues or contribute to this project via the [GitHub Issues page](https://github.com/AdeshGurjar02/heart-disease-prediction/issues).



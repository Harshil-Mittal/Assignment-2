# Heart Disease Prediction using AIML

This is just a short overview of the assignment.
Refer the Explaination_Doc_2.2 for detailed explaination of the assignment.

## Overview

This project aims to predict the likelihood of heart disease based on various health parameters using machine learning algorithms. The model was trained using the UCI Heart Disease dataset, and a web application was developed using Flask to allow users to input data and receive predictions in real time.

## Dataset

The dataset used in this project is the **UCI Heart Disease Dataset**, which can be accessed [here](https://archive.ics.uci.edu/ml/datasets/Heart+Disease). It contains several health attributes like age, sex, cholesterol levels, and more, to predict the presence of heart disease in a patient.

## Technologies Used

- **Machine Learning Algorithms**: 
  - Logistic Regression
  - Decision Tree
  - Support Vector Machine (SVM)
  - K-Nearest Neighbors (KNN)
  - Linear Discriminant Analysis (LDA)
  
- **Python Libraries**:
  - scikit-learn (for model implementation)
  - pandas (for data manipulation)
  - numpy (for numerical operations)
  - Flask (for creating the web application)
  - matplotlib, seaborn (for data visualization)

- **Web Development**:
  - HTML
  - CSS

## Features

- **Heart Disease Prediction**: 
  - The user can input health parameters such as age, sex, cholesterol levels, etc.
  - The machine learning model predicts the likelihood of heart disease based on the input.
  
- **Flask Web Application**:
  - The web interface allows users to interact with the model, providing an easy-to-use platform for heart disease prediction.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/harshil-mittal/Assignment-2.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Assignment-2
    ```
3. Install the required dependencies
4. Run the Flask application:
    ```bash
    python app.py
    ```
5. Open your browser and go to `http://127.0.0.1:5000/` to access the web app.

## Usage

- After opening the web app, the user will be prompted to enter various health parameters such as age, cholesterol level, etc.
- Upon submitting the form, the app will display a prediction on the likelihood of heart disease.

## References

1. UCI Heart Disease Dataset: This dataset was used to train the machine learning model for heart disease prediction. It contains attributes such as age, sex, cholesterol levels, and more, to predict the presence of heart disease.
   
2. AIML (Artificial Intelligence and Machine Learning) Techniques: The project utilized machine learning algorithms like Logistic Regression, Decision Tree, and Support Vector Machine (SVM) for classification and prediction tasks. The techniques were implemented using Python libraries such as scikit-learn.

3. Udemy Course: *"Deploy - HTML & CSS for Web Development"*: This course provided essential skills in HTML and CSS, which were applied to create the user interface for the Flask-based web application in the project.

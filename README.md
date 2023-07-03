# ChurnPrediction
This project analyzes customer churn prediction using various machine learning algorithms and evaluates their performance. It also includes feature selection and visualizations to understand the correlation between different features and the churn rate.

Customer Churn Prediction is a machine learning project that aims to predict customer churn based on various factors. It utilizes data analysis, preprocessing, feature selection, and different machine learning algorithms to build a predictive model.

## Features

- Data loading: The project reads customer data from a CSV file using the pandas library.

- Data cleaning: It performs data cleaning tasks such as handling missing values and converting categorical variables into numeric form.

- Exploratory data analysis (EDA): The project analyzes the dataset to gain insights into the data, such as identifying correlations between features and the target variable (churn).

- Feature selection: It selects relevant features by considering their correlation with the target variable and eliminates redundant or irrelevant features.

- Model training and evaluation: The project trains machine learning models, such as logistic regression, K-nearest neighbors (KNN), and support vector machines (SVM), to predict customer churn. It evaluates the models using various metrics such as accuracy, precision, recall, and F1 score.

- Model deployment: The project showcases how to save the trained model using the pickle library and provides an example of how to load the model for making predictions on new data.

## Prerequisites

- Python 3.x
- Required libraries: numpy, pandas, matplotlib, scikit-learn, pickle

## Installation

1. Clone the repository:
git clone https://github.com/HHDVasishtPranav/ChurnPrediction.git


2. Install the required libraries:
pip install numpy pandas matplotlib scikit-learn


## Usage

1. Open the project in your preferred Python development environment.

2. Run the `Churn_prediction.ipynb` script to train and evaluate the machine learning models for customer churn prediction.

3. The script will load the customer data from the CSV file, perform data cleaning, feature selection, and train the machine learning models.

4. The script will display the evaluation metrics for each model, such as accuracy, precision, recall, and F1 score.

5. To make predictions on new data, use the trained model by loading it using the pickle library. An example of how to load the model and make predictions is provided in the script.
6. To deploy the model using Flask, run the following command:
    python REST_API.py
7. The Flask web application will start running locally.
8. Open a web browser and visit http://localhost:5000 to access the customer churn prediction interface.
9. Enter the required information about the customer, such as contract type, tech support, payment method, internet service, paperless billing, senior citizen status, streaming movies and TV, and monthly charges.

Click the "Predict" button to get the prediction for customer churn.

## Deployment with Flask
The project includes a Flask web application to deploy the trained model. Here's an overview of the deployment process:

Import the necessary libraries: pickle for loading the trained model and flask for creating the web application.

Load the trained model using pickle: This allows you to use the model for making predictions.

Define routes for the web application: In this project, the main route '/' renders the index.html template, and the '/churn/v1/predict' route handles the prediction request.

Implement the prediction logic: When the prediction route is accessed with a POST request, the input data is extracted from the request, processed, and passed to the loaded model for prediction. The result is then rendered on the index.html template.

Run the Flask application: Execute app.run(debug=True) to start the Flask server in debug mode.

## Screen Shots
![ss1](https://github.com/HHDVasishtPranav/ChurnPrediction/blob/main/static/Screenshot%202023-07-03%20115712.png?raw=true "Title")
![ss2](https://github.com/HHDVasishtPranav/ChurnPrediction/blob/main/static/Screenshot%202023-07-03%20115757.png?raw=true "Title")
![analysis](https://github.com/HHDVasishtPranav/ChurnPrediction/blob/main/static/output.png?raw=true "Title")
## Project Structure
The project directory contains the following files and directories:

churn_prediction.py: The main script for data loading, preprocessing, model training, and evaluation.

REST_API.py: The Flask application script for model deployment.

churn.pkl: The serialized version of the trained model saved using pickle.

index.html: The HTML template for the web interface.

## Acknowledgments

- The project uses the Telco Customer Churn dataset from [Kaggle](https://www.kaggle.com/blastchar/telco-customer-churn).

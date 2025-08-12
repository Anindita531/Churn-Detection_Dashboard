# Churn-Detection_Dashboard
# Customer Churn Prediction Web App

This repository contains a simple Machine Learning web application built with Flask.  
It predicts customer churn based on input features using a trained Random Forest model.

## Project Structure
├── app.py # Flask API server
├── train.py # Script to train and save the model
├── random_forest_model.pkl # Trained model file (not included in repo, add after training)
├─ index.html # Frontend HTML form for input
├── test_api.py # Python script to test the API
└── README.md # This file
Step 1:run python train_pipeline.py
it will save the model random_forest_model
step 2:run app.py
for server it will be running at 5000 port
step 3:run test_api.py
to predict 

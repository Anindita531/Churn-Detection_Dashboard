📊 Customer Churn Detection Dashboard
📌 Project Overview

Customer churn is a major challenge for subscription-based businesses like telecom companies.
This project builds a Machine Learning–powered Churn Detection Dashboard that predicts whether a customer is likely to leave the service based on their usage and account details.

The system combines data analysis, ML modeling, and a Flask-based web application to deliver real-time churn predictions through a simple user interface.

🎯 Objectives

Analyze customer behavior using historical telecom data

Train a machine learning model to predict churn

Deploy the trained model using a Flask web application

Provide an easy-to-use dashboard for churn prediction

🧠 Machine Learning Model

Algorithm Used: Random Forest Classifier

Reason:

Handles non-linear relationships

Works well with categorical and numerical features

Reduces overfitting compared to single decision trees

📂 Dataset

Dataset Name: Telco Customer Churn Dataset

Source: Public telecom churn dataset

Target Variable: Churn (Yes / No)

Key Features:

Customer tenure

Monthly charges

Total charges

Contract type

Internet service

Payment method

🛠️ Tech Stack
Category	Tools
Programming Language	Python
ML Libraries	scikit-learn, pandas, numpy
Backend	Flask
Frontend	HTML
Model Storage	Pickle (.pkl)
Visualization (EDA)	Matplotlib / Seaborn
📁 Project Structure
```
Churn-Detection_Dashboard/
│
├── Telco-Customer-Churn.csv        # Dataset
├── customer_churn_prediction.ipynb# Data analysis & model training
├── train_pipeline.py              # Training pipeline script
├── random_forest_model.pkl        # Saved ML model
├── app.py                         # Flask backend
├── index.html                     # Frontend UI
├── test_api.py                    # API testing script
├── requirements.txt               # Dependencies
└── README.md                      # Project documentation
```
### ⚙️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/Anindita531/Churn-Detection_Dashboard.git
cd Churn-Detection_Dashboard

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Train the Model (Optional)
python train_pipeline.py

4️⃣ Run the Flask App
python app.py

5️⃣ Open in Browser
http://localhost:5000

🔍 Features

Predicts customer churn in real time

Web-based dashboard using Flask

Pre-trained Random Forest model

Easy to extend with new models or features

📈 Future Enhancements

Add interactive visual dashboards (Plotly / Streamlit)

Deploy on cloud platforms (Render / Heroku)

Add user authentication

Improve UI using React

Compare multiple ML models

💼 Use Case

Telecom companies

Subscription-based services

Customer retention analysis

Business intelligence systems

🧑‍💻 Author

Anindita Ghosh
B.Tech IT | Aspiring Software & Data Engineer
GitHub: Anindita531

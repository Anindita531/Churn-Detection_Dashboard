import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
import joblib

# ডেটা লোড করো
df = pd.read_csv('Telco-Customer-Churn.csv')

# TotalCharges কলাম numeric এ কনভার্ট করো (যদি string থাকে)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# missing values থাকলে ড্রপ বা ফিল করো
df.dropna(inplace=True)

# টার্গেট ও ফিচার সেট করো
X = df.drop(columns=['Churn', 'customerID'])
y = df['Churn'].map({'No': 0, 'Yes': 1})

# Train-test স্প্লিট
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# categorical ও numeric কলাম আলাদা করো
categorical_cols = X_train.select_dtypes(include=['object']).columns.tolist()
numeric_cols = X_train.select_dtypes(include=['int64', 'float64']).columns.tolist()

# প্রিপ্রসেসিং + মডেল pipeline
preprocessor = ColumnTransformer(transformers=[
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols),
    ('num', 'passthrough', numeric_cols)
])

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# মডেল ট্রেন করো
pipeline.fit(X_train, y_train)

# pipeline সেভ করো
joblib.dump(pipeline, 'random_forest_model.pkl')

print("Training complete and model saved as 'random_forest_model.pkl'")

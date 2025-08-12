from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)  # <-- CORS চালু করলাম

pipeline = joblib.load('random_forest_model.pkl')

@app.route('/predict', methods=['POST'])
 
def predict():
    data = request.get_json(force=True)
    print("Received data:", data)  # ইনপুট দেখা
    df = pd.DataFrame([data])
    print("Dataframe columns:", df.columns)
    prediction = pipeline.predict(df)
    return jsonify({'prediction': int(prediction[0])})


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

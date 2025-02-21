# ml_service.py
from flask import Flask, request, jsonify
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

app = Flask(__name__)

# Dummy model training (In production, load a pre-trained model)
def train_dummy_model():
    # Sample data: [age, heart_rate, steps]
    X = np.array([[25, 70, 10000], [50, 80, 5000], [35, 65, 12000], [60, 90, 3000]])
    y = np.array([0, 1, 0, 1])  # 0: low risk, 1: high risk
    model = LogisticRegression()
    model.fit(X, y)
    return model

model = train_dummy_model()
# Optionally, pickle the model for later use

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    # Extract features (this must match your model’s requirements)
    features = [data.get('age', 0), data.get('heart_rate', 0), data.get('steps', 0)]
    risk_prediction = model.predict([features])[0]
    recommendation = "Schedule a checkup" if risk_prediction == 1 else "Keep up the good work"
    return jsonify({"risk": int(risk_prediction), "recommendation": recommendation})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


from flask import Flask, request, jsonify
from clf import ir

app = Flask(__name__)

@app.route("/predict-alphabet", methods=["POST"])

def predict_data():
    image = request.files.get("alphabet")
    prediction = get_prediction(image)
return jsonify({
    "prediction": prediction
}), 200

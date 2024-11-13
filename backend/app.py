# app.py
from flask import Flask, request, jsonify
from fertilizer_recommendation_predict import recommend_fertilizer
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from React frontend

@app.route('/recommend-fertilizer', methods=['POST'])
def recommend():
    data = request.json
    fertilizer = recommend_fertilizer(
        temperature=float(data['temperature']),
        humidity=float(data['humidity']),
        moisture=float(data['moisture']),
        nitrogen=float(data['nitrogen']),
        potassium=float(data['potassium']),
        phosphorus=float(data['phosphorus']),
        soil_type=data['soilType'],
        crop_type=data['cropType']
    )
    return jsonify({'recommended_fertilizer': fertilizer})

if __name__ == '__main__':
    app.run(debug=True)
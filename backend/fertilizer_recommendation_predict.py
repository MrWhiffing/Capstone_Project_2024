# fertilizer_recommendation_predict.py
import numpy as np
import pickle

# Load models and encoders
with open("svm_pipeline.pkl", "rb") as f:
    model = pickle.load(f)
with open("fertname_label_encoder.pkl", "rb") as f:
    fertname_label_encoder = pickle.load(f)
with open("soil_type_label_encoder.pkl", "rb") as f:
    soil_type_label_encoder = pickle.load(f)
with open("crop_type_label_encoder.pkl", "rb") as f:
    crop_type_label_encoder = pickle.load(f)

# Function to predict fertilizer based on user input
def recommend_fertilizer(temperature, humidity, moisture, nitrogen, potassium, phosphorus, soil_type, crop_type):
    # Encode categorical inputs
    soil_type_encoded = soil_type_label_encoder.transform([soil_type])[0]
    crop_type_encoded = crop_type_label_encoder.transform([crop_type])[0]

    # Create input array
    features = np.array([[temperature, humidity, moisture, nitrogen, potassium, phosphorus, soil_type_encoded, crop_type_encoded]])

    # Predict using the model
    prediction = model.predict(features)[0]
    recommended_fertilizer = fertname_label_encoder.inverse_transform([prediction])[0]

    return recommended_fertilizer
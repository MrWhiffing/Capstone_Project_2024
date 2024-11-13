# fertilizer_recommendation_model.py
import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE

# Load the dataset
data = pd.read_csv(r"C:\Users\USER\Downloads\Fertilizer Prediction.csv")

# Preprocess data
continuous_data_cols = ["Temparature", "Humidity", "Moisture", "Nitrogen", "Potassium", "Phosphorous"]
categorical_data_cols = ["Soil Type", "Crop Type"]

# Encode categorical columns
soil_type_label_encoder = LabelEncoder()
data["Soil Type"] = soil_type_label_encoder.fit_transform(data["Soil Type"])

crop_type_label_encoder = LabelEncoder()
data["Crop Type"] = crop_type_label_encoder.fit_transform(data["Crop Type"])

fertname_label_encoder = LabelEncoder()
data["Fertilizer Name"] = fertname_label_encoder.fit_transform(data["Fertilizer Name"])

# Prepare features and target
X = data[continuous_data_cols + categorical_data_cols]
y = data["Fertilizer Name"]

# Address data imbalance
smote = SMOTE()
X, y = smote.fit_resample(X, y)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Model pipelines
svm_pipeline = make_pipeline(StandardScaler(), SVC(probability=True, random_state=18))
rf_pipeline = make_pipeline(StandardScaler(), RandomForestClassifier(random_state=18))
xgb_pipeline = make_pipeline(StandardScaler(), XGBClassifier(random_state=18))

# Train the models
svm_pipeline.fit(X_train, y_train)
rf_pipeline.fit(X_train, y_train)
xgb_pipeline.fit(X_train, y_train)

# Save models and encoders
pickle.dump(svm_pipeline, open("svm_pipeline.pkl", "wb"))
pickle.dump(rf_pipeline, open("rf_pipeline.pkl", "wb"))
pickle.dump(xgb_pipeline, open("xgb_pipeline.pkl", "wb"))
pickle.dump(fertname_label_encoder, open("fertname_label_encoder.pkl", "wb"))
pickle.dump(soil_type_label_encoder, open("soil_type_label_encoder.pkl", "wb"))
pickle.dump(crop_type_label_encoder, open("crop_type_label_encoder.pkl", "wb"))
print("Models and encoders saved successfully.")
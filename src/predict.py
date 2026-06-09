import pickle
import numpy as np
import pandas as pd

# Load trained model
with open("D:/Insurance_Cost_Prediction/models/insurance_model.pkl", "rb") as file:
    model = pickle.load(file)

print("=== Insurance Cost Prediction ===")

age = int(input("Age: "))
sex = input("Sex (male/female): ").lower()
bmi = float(input("BMI: "))
children = int(input("Number of Children: "))
smoker = input("Smoker (yes/no): ").lower()

# Encoding
sex = 1 if sex == "male" else 0
smoker = 1 if smoker == "yes" else 0

# Region values (default)
region_northwest = 0
region_southeast = 0
region_southwest = 0

sample = pd.DataFrame([{
    "age": age,
    "sex": sex,
    "bmi": bmi,
    "children": children,
    "smoker": smoker,
    "region_northwest": region_northwest,
    "region_southeast": region_southeast,
    "region_southwest": region_southwest
}])

prediction = model.predict(sample)

print("\nPredicted Insurance Cost = ₹", round(prediction[0], 2))

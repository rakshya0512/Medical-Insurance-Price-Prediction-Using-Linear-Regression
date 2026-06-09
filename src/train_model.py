import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load dataset
data = pd.read_csv("D:\Insurance_Cost_Prediction\dataset\insurance.csv")

# Encoding
data["sex"] = data["sex"].map({"male":1,"female":0})
data["smoker"] = data["smoker"].map({"yes":1,"no":0})

data = pd.get_dummies(
    data,
    columns=["region"],
    drop_first=True
)

X = data.drop("charges", axis=1)
y = data["charges"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

score = r2_score(y_test, y_pred)

print("Accuracy:", score)

with open("D:/Insurance_Cost_Prediction/models/insurance_model.pkl","wb") as file:
    pickle.dump(model,file)

print("Model Saved")

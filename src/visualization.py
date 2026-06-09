import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv("D:/Insurance_Cost_Prediction/dataset/insurance.csv")

data["sex"] = data["sex"].map({"male":1,"female":0})
data["smoker"] = data["smoker"].map({"yes":1,"no":0})

data = pd.get_dummies(
    data,
    columns=["region"],
    drop_first=True
)

X = data.drop("charges",axis=1)
y = data["charges"]

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

plt.figure(figsize=(8,6))

plt.scatter(y_test,y_pred)

plt.xlabel("Actual Charges")
plt.ylabel("Predicted Charges")

plt.title(
    "Insurance Cost Prediction"
)

plt.plot(
    [y_test.min(),y_test.max()],
    [y_test.min(),y_test.max()]
)

plt.savefig(
    "D:/Insurance_Cost_Prediction/results/actual_vs_predicted.png"
)
print("Graph saved successfully!")
plt.show()

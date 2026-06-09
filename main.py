import os

while True:

    print("\n===== INSURANCE COST PREDICTION =====")
    print("1. Predict Insurance Cost")
    print("2. Generate Visualization")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        os.system("python src/predict.py")

    elif choice == "2":
        os.system("python src/visualization.py")

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")

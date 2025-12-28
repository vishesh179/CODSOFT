# Student Performance Prediction System
# Internship Project - Python and Machine Learning

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

def main():
    # Load the dataset
    data = pd.read_csv("student_data.csv")

    print("Dataset Loaded Successfully\n")
    print(data.head())

    # Select input features and target variable
    X = data[['study_hours', 'attendance', 'previous_score']]
    y = data['final_score']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train Linear Regression model
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)

    # Train Decision Tree model
    dt_model = DecisionTreeRegressor(random_state=42)
    dt_model.fit(X_train, y_train)

    # Make predictions
    lr_predictions = lr_model.predict(X_test)
    dt_predictions = dt_model.predict(X_test)

    # Evaluate the models
    lr_error = mean_absolute_error(y_test, lr_predictions)
    dt_error = mean_absolute_error(y_test, dt_predictions)

    print("\nModel Evaluation Results:")
    print("Linear Regression Mean Absolute Error:", round(lr_error, 2))
    print("Decision Tree Mean Absolute Error:", round(dt_error, 2))

    # Sample prediction
    sample_student = np.array([[7, 88, 68]])  # study_hours, attendance, previous_score

    lr_result = lr_model.predict(sample_student)
    dt_result = dt_model.predict(sample_student)

    print("\nSample Student Prediction:")
    print("Linear Regression Predicted Score:", round(lr_result[0], 2))
    print("Decision Tree Predicted Score:", round(dt_result[0], 2))

if __name__ == "__main__":
    main()

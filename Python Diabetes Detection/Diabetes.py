#!/usr/bin/env python3

# Diabetes Prediction Using Support Vector Machine
import pickle
import os
import sys
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# For training
# ... (previous code)

def load_model():
    with open('svc.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    return model

def train():
    dataset = pd.read_csv('pima.csv')
    X = dataset[['B', 'C', 'E', 'F', 'H']]  # Updated column names here
    Y = dataset['I']  # Use single brackets for Y as it's a Series

    # Train-test split
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=101)

    model = SVC(kernel='linear')
    svc = model.fit(X_train, Y_train)

    # Save Model As Pickle File
    with open('svc.pkl', 'wb') as m:
        pickle.dump(svc, m)
    test(X_test, Y_test)
    print("Training complete!")  # Add this line

# Updated test function
def test(X_test, Y_test):
    model = load_model()
    pre = model.predict(X_test)
    accuracy = accuracy_score(Y_test, pre)
    print(f"Accuracy of the model: {accuracy:.2f}")

# Updated check_input function
def check_input(data) -> int:
    df = pd.DataFrame(data=data, index=[0])
    model = load_model()
    op = model.predict(df)
    return op[0]

if __name__ == '__main__':
    train()


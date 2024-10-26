import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pickle

# Load the dataset
dataset = pd.read_csv('pima.csv')

# Define features (X) and target (Y)
X = dataset[['B', 'C', 'E', 'F', 'H']]
Y = dataset['I']

# Split the dataset into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=101)

# Create and train the SVM model
model = SVC(kernel='linear')
model.fit(X_train, Y_train)

# Save the trained model as svc.pkl
with open('svc.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

print("Model training complete. The model is saved as svc.pkl.")

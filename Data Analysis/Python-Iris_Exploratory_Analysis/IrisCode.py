plt.pause(0.1)
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Load the Iris dataset
iris = load_iris()

# Creating a Pandas DataFrame from the dataset
df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                  columns=iris['feature_names'] + ['target'])

# Check the first few rows of the DataFrame
print(df.head())

# Check the summary statistics of the dataset
print(df.describe())

# Check the distribution of the target variable
sns.countplot(x='target', data=df)
plt.xlabel('Species')
plt.ylabel('Count')
plt.title('Distribution of Iris Species')
plt.show()
plt.pause(0.1)


# Check the correlation between the variables
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
plt.pause(0.1)

# Exploring the distributions of individual variables
sns.histplot(data=df, x='sepal length (cm)', hue='target', kde=True)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Count')
plt.title('Distribution of Sepal Length by Species')
plt.show()
plt.pause(0.1)


sns.histplot(data=df, x='sepal width (cm)', hue='target', kde=True)
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Count')
plt.title('Distribution of Sepal Width by Species')
plt.show()
plt.pause(0.1)


sns.histplot(data=df, x='petal length (cm)', hue='target', kde=True)
plt.xlabel('Petal Length (cm)')
plt.ylabel('Count')
plt.title('Distribution of Petal Length by Species')
plt.show()
plt.pause(0.1)


sns.histplot(data=df, x='petal width (cm)', hue='target', kde=True)
plt.xlabel('Petal Width (cm)')
plt.ylabel('Count')
plt.title('Distribution of Petal Width by Species')
plt.show()
plt.pause(0.1)


# Comparing the distributions between species
sns.boxplot(data=df, x='target', y='sepal length (cm)')
plt.xlabel('Species')
plt.ylabel('Sepal Length (cm)')
plt.title('Comparison of Sepal Length between Species')
plt.show()
plt.pause(0.1)


sns.boxplot(data=df, x='target', y='sepal width (cm)')
plt.xlabel('Species')
plt.ylabel('Sepal Width (cm)')
plt.title('Comparison of Sepal Width between Species')
plt.show()
plt.pause(0.1)


sns.boxplot(data=df, x='target', y='petal length (cm)')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.title('Comparison of Petal Length between Species')
plt.show()
plt.pause(0.1)


sns.boxplot(data=df, x='target', y='petal width (cm)')
plt.xlabel('Species')
plt.ylabel('Petal Width (cm)')
plt.title('Comparison of Petal Width between Species')
plt.show()
plt.pause(0.1)


# Building a predictive model to classify the Iris species
# Split the dataset into features (X) and target (y)
X = df.drop('target', axis=1)
y = df['target']

# Split to training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Logistic Regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Creating a confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

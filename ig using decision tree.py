from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.feature_selection import mutual_info_classif
import matplotlib.pyplot as plt

n = int(input("Enter number of records: "))
X = []
y = []

for i in range(n):
    a, b, c = map(int, input("Enter Feature1 Feature2 Class: ").split())
    X.append([a, b])
    y.append(c)

# Calculate Information Gain using inbuilt function
gain = mutual_info_classif(X, y, discrete_features=True)

print("\nInformation Gain:")
print("Feature1:", round(gain[0], 4))
print("Feature2:", round(gain[1], 4))

# Decision Tree using Entropy
model = DecisionTreeClassifier(criterion="entropy")
model.fit(X, y)

# Display Decision Tree
plt.figure(figsize=(8, 5))
plot_tree(model, feature_names=["Feature1", "Feature2"], filled=True)
plt.show()

# Prediction
a, b = map(int, input("Enter test values: ").split())

print("Predicted Class:", model.predict([[a, b]])[0])

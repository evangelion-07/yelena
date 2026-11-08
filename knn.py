]import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

n = int(input("Enter number of records: "))
X = []
y = []

for i in range(n):
    a, b, c = input("Enter Feature1 Feature2 Class: ").split()
    X.append([float(a), float(b)])
    y.append(c)

k = int(input("Enter K (1 to n): "))
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X, y)

a, b = map(float, input("Enter test values: ").split())
prediction = model.predict([[a, b]])[0]
print("Predicted Class:", prediction)

# Two features form the X and Y axes; each class is a different group.
for cls in sorted(set(y)):
    points = [point for point, label in zip(X, y) if label == cls]
    plt.scatter([p[0] for p in points], [p[1] for p in points], label=f"Class {cls}")
plt.scatter(a, b, marker="*", s=180, label=f"Test: {prediction}")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("KNN Classification")
plt.legend()
plt.tight_layout()
plt.show()

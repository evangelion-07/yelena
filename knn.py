import matplotlib.pyplot as plt
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


plt.scatter(a, b, marker="*", s=180, color="black", label=f"Test: {prediction}")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("KNN Classification")
plt.legend()
plt.tight_layout()
plt.show()

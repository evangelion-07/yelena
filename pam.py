
import numpy as np
import matplotlib.pyplot as plt
from kmedoids import KMedoids

n = int(input("Enter number of points: "))
X = []

for i in range(n):
    x, y = map(float, input("Enter X Y: ").split())
    X.append([x, y])

X = np.array(X)

k = int(input("Enter number of clusters: "))

model = KMedoids(n_clusters=k, metric="euclidean",
                 method="pam", init="build")
labels = model.fit_predict(X)

medoids = X[model.medoid_indices_]

print("Medoids:", medoids)
for point, label in zip(X, labels):
    print("Point:", point, "Cluster:", label)

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis")
plt.scatter(medoids[:, 0], medoids[:, 1],
            color="red", marker="*", s=250, label="Medoids")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("PAM Clustering")
plt.legend()
plt.show()

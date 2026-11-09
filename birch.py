import matplotlib.pyplot as plt
from sklearn.cluster import Birch
from sklearn.metrics import cluster
from sklearn.metrics import cluster

n = int(input("Enter number of points: "))
X = []

for i in range(n):
    x, y = map(float, input("Enter X Y: ").split())
    X.append([x, y])

k = int(input("Enter number of clusters: "))
threshold = float(input("Enter threshold (example 0.5): "))
model = Birch(n_clusters=k, threshold=threshold)
labels = model.fit_predict(X)

for point, label in zip(X, labels):
    print("Point:", point, "Cluster:", label)

plt.scatter([point[0] for point in X], [point[1] for point in X],
            c=labels, cmap="viridis", alpha=0.7)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("BIRCH Clustering")
plt.legend()
plt.tight_layout()
plt.show()

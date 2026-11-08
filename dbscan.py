import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

n = int(input("Enter number of points: "))
X = []

for i in range(n):
    x, y = map(float, input("Enter X Y: ").split())
    X.append([x, y])

eps = float(input("Enter epsilon (example 1.5): "))
min_samples = int(input("Enter minimum samples: "))
model = DBSCAN(eps=eps, min_samples=min_samples)
labels = model.fit_predict(X)

for point, label in zip(X, labels):
    print("Point:", point, "Cluster:", label)
print("Cluster -1 means noise")

# Plot the points in each cluster (label -1 indicates DBSCAN noise).
for cluster in sorted(set(labels)):
    points = [point for point, label in zip(X, labels) if label == cluster]
    plt.scatter([p[0] for p in points], [p[1] for p in points],
                label="Noise" if cluster == -1 else f"Cluster {cluster}")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("DBSCAN Clustering")
plt.legend()
plt.tight_layout()
plt.show()

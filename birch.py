import matplotlib.pyplot as plt
from sklearn.cluster import Birch

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

# Plot the points in each cluster (label -1 indicates DBSCAN noise).
for cluster in sorted(set(labels)):
    points = [point for point, label in zip(X, labels) if label == cluster]
    plt.scatter([p[0] for p in points], [p[1] for p in points],
                label="Noise" if cluster == -1 else f"Cluster {cluster}")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("BIRCH Clustering")
plt.legend()
plt.tight_layout()
plt.show()

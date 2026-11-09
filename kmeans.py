import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

n = int(input("Enter number of points: "))
X = []

for i in range(n):
    x, y = map(float, input("Enter X Y: ").split())
    X.append([x, y])

k = int(input("Enter number of clusters: "))
model = KMeans(n_clusters=k, random_state=0, n_init=10)
labels = model.fit_predict(X)

for point, label in zip(X, labels):
    print("Point:", point, "Cluster:", label)
print("Cluster Centers:\n", model.cluster_centers_)


plt.scatter([point[0] for point in X], [point[1] for point in X],
            c=labels, cmap="viridis", alpha=0.7, label="Points")
plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1],
            marker="X", s=150, label="Centroids")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("K-Means Clustering")
plt.legend()
plt.tight_layout()
plt.show()

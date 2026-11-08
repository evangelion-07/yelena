
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

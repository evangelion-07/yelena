
from sklearn.naive_bayes import GaussianNB

n = int(input("Enter number of records: "))
X = []
y = []

for i in range(n):
    a, b, c = input("Enter Feature1 Feature2 Class: ").split()
    X.append([float(a), float(b)])
    y.append(c)

model = GaussianNB()
model.fit(X, y)

a, b = map(float, input("Enter test values: ").split())
print("Predicted Class:", model.predict([[a, b]])[0])

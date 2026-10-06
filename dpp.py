import pandas as pd

n = int(input("Enter records: "))
data = []

for i in range(n):
    row = input("Enter name and salary: ").split()
    data.append(row)

df = pd.DataFrame(data, columns=["Name", "Salary"])
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
df = df.fillna({"Name": "Unknown", "Salary": df["Salary"].mean()})

print("Cleaned Data:", data)

salary = [float(row[1]) for row in data]
mn, mx = min(salary), max(salary)

print("Normalized Data:")
for row in data:
    value = (float(row[1]) - mn) / (mx - mn) if mx != mn else 0
    print(row[0], round(value, 2))

m = int(input("Enter second dataset records: "))
for i in range(m):
    data.append(input("Enter name and salary: ").split())

print("Integrated Data:", data)
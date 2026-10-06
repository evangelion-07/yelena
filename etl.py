n = int(input("Enter records: "))
data = []

for i in range(n):
    name, age, salary = input("Enter Name Age Salary: ").split()
    data.append([name, int(age), int(salary)])

print("\nExtracted Data:")
print(data)

data = [x for x in data if x[1] > 0 and x[2] > 0]

for x in data:
    x[0] = x[0].upper()
    x[2] = x[2] * 1.1

print("\nTransformed Data:")
print(data)

loaded = data
print("\nLoaded Data:")
print(loaded)
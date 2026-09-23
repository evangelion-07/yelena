
data = [
    ["101", "Alice", "CSE"],
    ["102", "Bob", "ECE"],
    ["103", "Charlie", "IT"],
    ["104", "David", "CSE"],
    ["105", "Eva", "ECE"],
    ["106", "Frank", "IT"]
]

part1 = data[:3]
part2 = data[3:]

print("Partition 1:")
print(part1)

print("\nPartition 2:")
print(part2)

part3 = [[row[0], row[1]] for row in data]
part4 = [[row[0], row[2]] for row in data]

print("\nPartition 3 (ID, Name):")
print(part3)

print("\nPartition 4 (ID, Department):")
print(part4)

part5 = []
part6 = []

for i, item in enumerate(data):
    if i % 2 == 0:
        part5.append(item)
    else:
        part6.append(item)

print("\nPartition 5:")
print(part5)

print("\nPartition 6:")
print(part6)

part7 = []
part8 = []

for row in data:
    if int(row[0]) % 2 == 0:
        part7.append(row)
    else:
        part8.append(row)

print("\nPartition 7 (Odd IDs):")
print(part7)

print("\nPartition 8 (Even IDs):")
print(part8)

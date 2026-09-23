data = input("Enter data separated by spaces: ").split()
n = int(input("Enter number of partitions: "))
print("\n1. Horizontal Partitioning:")
size = len(data) // n

for i in range(n):
    start = i * size
    end = (i + 1) * size if i < n - 1 else len(data)
    print("Partition", i + 1, ":", data[start:end])

print("\n2. Vertical Partitioning:")

for i in range(n):
    print("Partition", i + 1, ":", data[i::n])

print("\n3. Round Robin Partitioning:")

round_robin = [[] for _ in range(n)]

for i, value in enumerate(data):
    round_robin[i % n].append(value)

for i in range(n):
    print("Partition", i + 1, ":", round_robin[i])

print("\n4. Hash Based Partitioning:")

hash_partitions = [[] for _ in range(n)]

for value in data:
    partition = hash(value) % n
    hash_partitions[partition].append(value)

for i in range(n):
    print("Partition", i + 1, ":", hash_partitions[i])

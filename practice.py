#data = []
# n = int(input("Enter number of partitions:"))
# for i in range(n):
#     id = int(input("Enter your ID:"))
#     name = input("Enter your name:")
#     age = int(input("Enter your age:"))
#     city = input("Enter your city:")
#     data.append([id, name, age, city])

# p = int(input("Enter number of partitions:"))

# print("\nHorizontal Partitioning:")
# size = (n + p - 1) // p
# for i in range(p):
#     print("Partition", i + 1, data[size * i:size * (i + 1)])
    
# print("\nVertical Partitioning:")
# p1 = [[r[0], r[1]] for r in data]
# p2 = [[r[0] ,r [2], r[3]] for r in data]
# print("Partition 1:", p1)
# print("Partition 2:", p2)
# print("\nRound Robin Partitioning:")
# rr = [[] for _ in range(p)]
# for i, row in enumerate(data):
#     rr[i % p].append(row)
# for i in range(p):
#     print("Partition", i + 1, rr[i])
# print("\nHash Based partitioning:")
# h = [[] for _ in range(p)]
# for row in data:
#     h[row[0] % p].append(row)
# for i in range(p):
#     print("Partition", i + 1, h[i])




# data = []
# n = int(input("Enter number of records:"))
# for i in range(n):
#     id = int(input("Enter your ID:"))
#     name = input("enter your name:")
#     age = int(input("Enter your age:"))
#     city = input("Enter your city:")
#     data.append([id, name, age, city])
# print("Extracted Data:")
# print(data)
# data = [x for x in data if x[2] > 0 and x[3] != ' ']
# for x in data:
#     x[1] = x[1].upper()
#     x[2] = x[2] + 4
#     print("Transformed Data:", data)
# loaded = data
# print("Loaded data:")
# print(loaded)


# data = []
# n = int(input("Enter your number of records:"))
# for i in range(n):
#     id = int(input("Enter your ID:"))
#     name = input("Enter your name:")
#     age = int(input("Enter your age:"))
#     city = input("Enter your city:")
#     data.append([id, name, age, city])

# print("\nData Cube:")
# for x in data:
#     print(x)

# print("\nRoll-Up:")
# total = sum(x[2] for x in data)
# print("Total Age:", total)

# print("\nSlice:")
# slice = [x for x in data if x[3] == input("Enter city for Slice:")]
# print("Slice:",slice)

# print("\nDice")
# dice = [x for x in data if x[1] == input("Enter name for Dice:") and x[2] == int(input("Enter your age for Dice:"))]
# print("Dice:",dice)

# print("\nDrill-Down:")
# for x in data:
#     print(x)

# n = int(input("Enter number of records:"))
# data =[]
# sales = []

# for i in range(n):
#     p, c, d, q = input("Enter Product Catergory Date Quantity:").split()
#     sales.append([p, c, d, int(q)])

# print("\nStar Schema:")
# print("Fact_Sales:", sales)
# print("Dimensions: Product Category Date")

# print("\nSnowflake Schema:")
# product = list(set(x[0] for x in sales))
# category = list(set(x[1] for x in sales))
# date = list(set(x[2] for x in sales))
# quantity = list(set(x[3] for x in sales))
# print("Product:", product)
# print("Category:", category)
# print("Date:", date)
# print("Quantity:", quantity)
# print("Fact_Sales:", sales)

# print("\nFact Constellation:")
# returns =[]
# m = int(input("Enter number of returns:"))
# for i in range(m):
#     p, d, q = input("Enter Product date quantity:").split()
#     returns.append([p, d, int(q)])

# print("Fact_Sales:", sales)
# print("Fact_Returns:", returns)
# print("Shared Dimensions: Product Date")

# data = []
# n = int(input("Enter number of records:"))

# for i in range(n):
#     row = input("Enter your ID, name, age, city:").split()
#     if len(row) == 2 and row not in data:
#         data.append(row)
# print("Cleaned Data:", data)

# salary = [int(row[1]) for row in data]
# mn, mx = min(salary), max(salary)
# print("Normalized Data:")
# for row in data:
#     value = (int(row[1]) - mn) / (mx-mn) if mx != mn else 0
#     print(row[0], round(value, 2))

# m = int(input("Enter Second dataset records:"))
# for i in range(m):
#     data.append(input("Enter your ID, name, age, city:").split())

# print("Integrated Data:", data)



n = int(input("Enter number of records: "))
data = []

for i in range(n):
    name, age, city = input("Enter Name Age City: ").split()
    age = int(age)

    age_group = "Young" if age < 30 else "Adult"
    region = "South" if city in ["Hyderabad", "Chennai", "Bangalore"] else "North"

    data.append([age_group, region])

print("\nGeneralized Data:")
for x in sorted(set(map(tuple, data))):
    print(list(x), "Count:", data.count(x))
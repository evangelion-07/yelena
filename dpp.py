data = input("Enter numbers (use space): ").split()
cleaned = []
for x in data:
    try:
        cleaned.append(float(x))
    except:
        pass
print("\nCleaned Data:", cleaned)

minimum = min(cleaned)
maximum = max(cleaned)

normalized = []

for x in cleaned:
    if maximum != minimum:
        n = (x - minimum) / (maximum - minimum)
    else:
        n = 0
    normalized.append(round(n, 2))

print("Normalized Data:", normalized)
data2 = input("\nEnter second dataset (use space): ").split()
integrated = cleaned + data2
print("Integrated Data:", integrated)

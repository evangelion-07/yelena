
n = int(input("Number of transactions: "))
transactions = [set(input(f"Transaction {i+1}: ").split()) for i in range(n)]

min_support = float(input("Minimum support (0 to 1): "))
min_confidence = float(input("Minimum confidence (0 to 1): "))

candidates = {frozenset([item]) for t in transactions for item in t}
frequent = {}
k = 1

while candidates:
    counts = {c: sum(c.issubset(t) for t in transactions) for c in candidates}

    current = {c: count for c, count in counts.items()
               if count / n >= min_support}

    if not current:
        break

    frequent.update(current)
    k += 1
    candidates = set()

    for a in current:
        for b in current:
            merged = a | b
            if len(merged) == k and all(merged - {x} in current for x in merged):
                candidates.add(merged)

print("\nFrequent Itemsets:")
for items, count in sorted(frequent.items(), key=lambda x: (len(x[0]), sorted(x[0]))):
    name = ", ".join(sorted(items))
    print(f"{{{name}}}: {count}/{n} " + "#" * round(20 * count / n))

print("\nAssociation Rules:")
for items, count in frequent.items():
    if len(items) < 2:
        continue
    for left in frequent:
        if left < items:
            confidence = count / frequent[left]
            if confidence >= min_confidence:
                right = items - left
                print(f"{set(left)} -> {set(right)}: Confidence = {confidence:.2f}")

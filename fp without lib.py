
class Node:
    def __init__(self, item, parent):
        self.item = item
        self.count = 0
        self.parent = parent
        self.children = {}

n = int(input("Number of transactions: "))
transactions = [set(input(f"Transaction {i+1}: ").split()) for i in range(n)]

min_support = float(input("Minimum support (0 to 1): "))
min_confidence = float(input("Minimum confidence (0 to 1): "))

def build_tree(data):
    counts = {}
    for items, weight in data:
        for item in items:
            counts[item] = counts.get(item, 0) + weight

    counts = {item: c for item, c in counts.items()
              if c / n >= min_support}

    root = Node(None, None)
    header = {item: [] for item in counts}

    for items, weight in data:
        ordered = sorted((x for x in items if x in counts),
                         key=lambda x: (-counts[x], x))
        node = root

        for item in ordered:
            if item not in node.children:
                node.children[item] = Node(item, node)
                header[item].append(node.children[item])
            node = node.children[item]
            node.count += weight

    return counts, header

frequent = {}

def fp_growth(data, prefix=frozenset()):
    counts, header = build_tree(data)

    for item in sorted(counts, key=lambda x: (counts[x], x)):
        pattern = prefix | {item}
        frequent[pattern] = counts[item]

        conditional = []

        for node in header[item]:
            path = []
            parent = node.parent

            while parent.item is not None:
                path.append(parent.item)
                parent = parent.parent

            if path:
                conditional.append((path, node.count))

        if conditional:
            fp_growth(conditional, pattern)

fp_growth([(t, 1) for t in transactions])

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

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

n = int(input("Enter number of transactions: "))
data = []

for i in range(n):
    data.append(input("Enter items: ").split())

s = float(input("Enter minimum support: "))

te = TransactionEncoder()
x = te.fit(data).transform(data)

df = __import__("pandas").DataFrame(x, columns=te.columns_)

freq = apriori(df, min_support=s, use_colnames=True)
print("\nFrequent Itemsets:")
print(freq)

rules = association_rules(freq, metric="confidence", min_threshold=0.5)
print("\nAssociation Rules:")
print(rules[["antecedents", "consequents", "support", "confidence"]])
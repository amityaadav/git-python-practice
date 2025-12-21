##Lists
weights = [45, 95, 125, 135, 145]
print(f"List of weights: {weights}")
weights.append(165)
print("Total: ", sum(weights))
print("Max: ", max(weights))
print("Min: ", min(weights))
print("Count: ", len(weights))
print("First weight: ",weights[0])
print("Last weight: ",weights[-1]) ##Instead of counting items manually and listing index, you can use first from last by using negative numbers
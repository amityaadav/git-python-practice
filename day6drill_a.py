## Working with loops
weights = [135, 155, 175]
print("--For loop without index--")
for w in weights:
    print(w)

print("--For loop with index--")
for i, w in enumerate(weights):

    print(f"Set {i + 1}: {w} lbs")

count = 0
print("--While loop--")
while count < 3:
    print(count)
    count += 1

print("--Use loop to create a list--")
weights = []
for i in range(3):
    w = int(input(f"Set {i + 1} Weight: "))
    weights.append(w)
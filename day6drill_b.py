# User input for while loop (count)
set_count = int(input("How many reps did you do? "))
print("Great, now enter weights for each set")
weights=[]

# User input to assign weights to a list
i = 1
while i <= set_count:
    input_weight = int(input(f"Set {i}: "))
    weights.append(input_weight)
    i += 1

# After the loop, print: all weights, total volume, average weight
print("---------")
count = 1
volume = []
for x in weights:
    print(f"Set {count}: Weight lifted {x}")
    count += 1
    volume.append(x)
total_volume = sum(volume)
print("Total Volume: ", total_volume)
print("Average Weight: ", total_volume/set_count)
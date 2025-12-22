# User Input: exercise
workout_name = input("What do you want to name your workout today: ")
if not workout_name:
    print("Workout name is required")
    exit()
exercise_name = input("What is your first exercise: ")
if not exercise_name:
    print("Exercise name is required")
    exit()

# User Input: Weight and Reps
set_count =  int(input("How many sets are you doing today "))
count = 1
weights = []
reps = []
while count <= set_count:
    try:
        input_weight = int(input(f"Set {count} weight in lbs: "))
        input_rep = int(input(f"Set {count} reps:"))
        if input_weight <= 0 or input_rep <=0:
            print("Weights must be positive value")
            continue
        weights.append(input_weight)
        reps.append(input_rep)
        count += 1
    except ValueError:
        print("Please enter a valid number")

# Print lists  
for i, (w,r) in enumerate(zip(weights, reps)):
    print(f"Set {i+1}: with {w} lbs for {r} reps")
    print(f"Volume for set {i+1} is {w * r}")

# Total Volume
total_volume = (sum(w * r for w, r in zip(weights, reps)))
print(f"Total Volume of your workout is: {total_volume}")
# User Input: Exercise name
workout_name = input("What do you want to name your workout today: ")
if not workout_name:
    print("Workout name is required")
    exit()
exercise_name = input("What is your first exercise: ")
if not exercise_name:
    print("Exercise name is required")
    exit()

# User input for the no. of sets
set_count =  int(input("How many sets are you doing today "))

# function to get weight and reps
def get_set_data(set_number):
    weight = int(input(f"Set {set_number} weight in lbs: "))
    reps = int(input(f"Set {set_number} reps: "))
    volume = weight * reps
    return {"weight": weight, "reps": reps, "volume": volume}

# function to calc volume
def calc_total_volume(sets):
    return sum(s["weight"] * s["reps"] for s in sets)

# run the functions
sets = []
for i in range(set_count):
    set_data = get_set_data(i + 1)
    sets.append(set_data)

# print summary
print("- - - Summary - - - ")
for i, x in enumerate(sets):
    print(f"For set {i+1}, you lifted a total of {x['weight']} lbs for {x['reps']} reps, and the total volume for the set was {x['volume']} lbs")

# print total volume
total_vol = calc_total_volume(sets)
print(f"The total volume for {exercise_name} was {total_vol} lbs")

# calculate and print best set
best_set = max(sets, key=lambda s: s["volume"])
print(f"Your best set was {best_set['weight']} lbs x {best_set['reps']} = {best_set['volume']} lbs")
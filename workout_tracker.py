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
    return {"weight": weight, "reps": reps}

# function to calc volume
def calc_total_volume(sets):
    return sum(s["weight"] * s["reps"] for s in sets)

sets = []
for i in range(set_count):
    set_data = get_set_data(i + 1)
    sets.append(set_data)

total = calc_total_volume(sets)
print(f"Total volume: {total}")
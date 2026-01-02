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

# input function
def get_set_data(set_number):
    weight_input = int(input(f"Set {set_number} weight in lbs: "))
    rep_input = int(input(f"Set {set_number} reps: "))
    return weight_input, rep_input

# total volume function
def calc_total_volume(weights, reps):
        return (sum(w * r for w,r in zip(weights, reps)))

# call input function
weights = []
reps = []
for i in range(set_count):
    w, r = get_set_data(i + 1)  # returns two values
    weights.append(w)
    reps.append(r)

# call total vol function
total = calc_total_volume(weights, reps)
print(f"Total volume: {total}")
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

sets = []  # list to hold all dictionaries

# insert two values into the dictionary
for i in range(set_count):
    weight = int(input(f"Set {i + 1} weight in lbs: "))
    reps = int(input(f"Set {i + 1} reps: "))
    set_data = {"weight": weight, "reps": reps}
    sets.append(set_data)

print(sets)
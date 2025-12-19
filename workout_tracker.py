# User Input: exercise
workout_name = input("What workout are we doing today: ")
if not workout_name:
    print("Workout name is required")
    exit()
exercise = input("What exercise: ")
    
# User Input: Weight and Reps
set1_weight = int(input("How much weight for the first set (lbs) are we lifting? "))
if set1_weight <=0:
    print("Weight cannot be empty")
    exit()
set1_reps = int(input(f"How many reps are we doing with {set1_weight} lbs? "))
set2_weight = int(input("How much weight for the second set (lbs) are we lifting? "))
if set2_weight <=0:
    print("Weight cannot be empty")
    exit()
set2_reps = int(input(f"How many reps are we doing with {set2_weight} lbs? "))

## Calculate
set1_volume = (set1_weight * set1_reps)
set2_volume = (set2_weight * set2_reps)
total_volume = set1_volume + set2_volume

## Display
print("---Workout Entry---")
print(f"Workout: {workout_name.title()}")
print(f"Exercise: {exercise.title()}")
print(f"-----")
print(f"Set 1 total volume {set1_volume}")
print(f"Set 2 total volume {set2_volume}")
print(f"Total volume of weight lifted was: {total_volume} lbs")
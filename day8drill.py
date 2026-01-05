# Create a dictionary for one workout set with keys: exercise, weight, reps
# Print each value using key access
# Add a new key volume with the calculated value
# Loop through and print all key-value pairs

workout_set = {"exercise": "Squats", "weight": 135, "reps": 10}

print(f"{workout_set['exercise']}")
print(f"{workout_set['weight']}")
print(f"{workout_set['reps']}")

workout_set["volume"] = (workout_set["weight"] * workout_set["reps"])
print(f"{workout_set["volume"]}")

for key, value in workout_set.items():
    print(f"{key}: {value}")
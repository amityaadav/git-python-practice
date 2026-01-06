# create an initial dictionary
workout_set = {
    "exercise": "Squats", 
    "weight": 135, 
    "reps": 10
}

# print a key from dictionary
print(f"{workout_set['exercise']}")
print(f"{workout_set['weight']}")
print(f"{workout_set['reps']}")

# perform an action on the dictionary and print the added KVP
workout_set["volume"] = (workout_set["weight"] * workout_set["reps"])
print(f"{workout_set["volume"]}")

# print all KVP
for key, value in workout_set.items():
    print(f"{key}: {value}")
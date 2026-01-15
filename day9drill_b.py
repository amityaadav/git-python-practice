# nested dictionary(workout) of list (exercise) which has a dictionary of sets
workout = {
    "name": "Chest and Triceps",
    "date": "2026-01-11",
    "exercises": [
        {
            "name": "Bench Press",
            "sets" : [
                {"weight": 135, "reps": 10},
                {"weight": 155, "reps": 5}
            ]
        }
    ]
}

# add volume for each set separately
for s in workout["exercises"]:
    for x in s["sets"]:
        x["volume"] = x["weight"] * x["reps"]

# print only the set
for s in workout["exercises"]:
    for x in s["sets"]:  
        print(f"Weight: {x['weight']}, Reps {x['reps']}, Volume {x['volume']}")
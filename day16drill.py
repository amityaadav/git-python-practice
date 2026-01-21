import pandas as pd

df = pd.read_csv('data/strong_workouts.csv')

# print(df[["Exercise Name", "Weight","Reps"]])

report = df[
    (df["Weight"] > 100) &
    (df["Reps"] >= 5) &
    (df["Exercise Name"].str.contains("Deadlift"))
    ]
    
print(report[["Exercise Name","Weight","Reps"]])

# Select just the Exercise Name, Weight, and Reps columns
# Filter to show only sets where weight > 100 lbs
# Filter to show only your heaviest exercise (pick one you know)
# Combine: show sets where weight > 100 AND reps >= 5
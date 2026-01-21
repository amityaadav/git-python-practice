import pandas as pd

# import workout spreadsheet
df = pd.read_csv('data/strong_workouts.csv')

# user input
exercise_name = input("What's the name of the exercise? ")

# Serach by user input
name_filter = df[
    df['Exercise Name'].str.contains(exercise_name)
]

# max weight in the entire data set
max_weight = name_filter[name_filter["Weight"] == name_filter["Weight"].max()]

print(max_weight[["Date","Exercise Name","Reps","Set Order","Weight"]])

# print total sets after filtering the name
print(f"Total sets: {len(name_filter)}")
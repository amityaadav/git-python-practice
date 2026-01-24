import pandas as pd

# import workout spreadsheet
df = pd.read_csv('data/strong_workouts.csv')

# user input
exercise_name = input("What's the name of the exercise? ")

# Serach by user input
name_filter = df[
    df['Exercise Name'].str.contains(exercise_name, case=False)
]

# Top 5 heaviest sets for the searched exercise
sort_val1 = (
    name_filter
    .sort_values("Weight", ascending=False).head(5)
)
print("\n"+"-" * 80)
print("\n"+"=" * 80)
print(sort_val1[["Date","Exercise Name","Reps","Set Order","Weight"]])

# Most recent set for that exercise
sort_val2 = (
    name_filter
    .sort_values("Date", ascending=False).head(5)
)
print("\n"+"=" * 80)
print(sort_val2[["Date","Exercise Name","Reps","Set Order","Weight"]])
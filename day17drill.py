import pandas as pd

df = pd.read_csv('data/strong_workouts.csv')

# Print your 10 heaviest sets ever (any exercise)
sorted_val1 = df.sort_values(["Weight"], ascending=[False]).head(10)
print("=" * 60)
print(sorted_val1[["Exercise Name","Set Order","Weight","Reps"]])

# Print your 5 most recent workouts (by date)
sorted_val2 = df.sort_values(["Date"], ascending=False).head(5)
print("=" * 60)
print(sorted_val2[["Date"]])

# Pick one exercise — print the top 5 heaviest sets for just that exercise
sorted_val3 = (
    df[df["Exercise Name"].str.contains("Bench")]
    .sort_values("Weight",ascending=False).head(5)
)
print("=" * 60)
print(sorted_val3[["Exercise Name","Weight"]])
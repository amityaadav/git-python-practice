# create a list(sets) of dictionary(2 defualt items)
sets = [
    {"weight": 135, "reps": 8},
    {"weight": 155, "reps": 6}
]
# add thrid attribute for volume in the dictionary
for s in sets:
    s["volume"] = s["weight"] * s["reps"]

for x in sets:
    print(x)
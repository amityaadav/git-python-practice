## User Input
set1_weight=int(input("How much weight did you lift on your first set? "))
set1_rep=int(input("How many reps did you perform? "))
set2_weight=int(input("How much weight did you lift on your second set? "))
set2_rep=int(input("How many reps did you perform? "))
set3_weight=int(input("How much weight did you lift on your third set? "))
set3_rep=int(input("How many reps did you perform? "))
total_volume = (set1_weight * set1_rep)+(set2_weight * set2_rep)+(set3_weight * set3_rep)

## Conditional Statement
if total_volume >= 2000:
    print("Monster Set")
elif total_volume >=1000:
    print("Solid work")
elif total_volume >= 500:
    print("Warm-up set")    
else:
    print("Just getting started")
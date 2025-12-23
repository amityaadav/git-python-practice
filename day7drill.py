# Global Variables
user_weight = [135,155]
user_reps = [10,8]

# Basic function
def calc_volume(weights,reps):
    return weights * reps

# function for total volume
def calc_total_volume(weights,reps):
    total_volume = 0
    for x,y in zip(weights, reps):
        total_volume += (calc_volume(x,y))
    return total_volume

# function for heaviest set
def get_heaviest_set(weights):
    return max(weights)

print(f"Total Volume: {calc_total_volume(user_weight,user_reps)}")
print(f"Heaviest Set: {get_heaviest_set(user_weight)}")
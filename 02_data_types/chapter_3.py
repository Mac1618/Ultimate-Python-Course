# Numbers and Operators

# variables
black_tea_grams = 14
sugar_grams = 3

# operators (add, minus, multiply = *)
total_grams = black_tea_grams + sugar_grams
remaining_tea_grams = black_tea_grams - sugar_grams
print(f"Total amount of grams: {total_grams}")
print(f"Remaining grams: {remaining_tea_grams}")


# division (float = /)
milk_liters = 7
servings = 4
milk_per_serving = milk_liters / servings
print(f"Milk per serving is: {milk_per_serving}")


# division (whole number = //)
total_tea_bags = 7
pots = 4
bags_per_tea = total_tea_bags // pots
print(f"Tea bags per pot is: {bags_per_tea}")


# modulus (remaining)
total_cinnamon_pods = 10
pods_per_cup = 3
leftover_pods = total_cinnamon_pods % pods_per_cup
print(f"Leftover cinnamon is: {leftover_pods}")


# power of (2 to the power of 3 = (3 * 3 * 3))
base_flavor_strength = 2
scale_factor = 3
flavor_scale = base_flavor_strength ** scale_factor
print(f"Scaled flavor strength: {flavor_scale}")


# improve readability in numbers
total_tea_leaves_harvested = 1_000_000_000
print(f"Total tea leaves harvested: {total_tea_leaves_harvested}")

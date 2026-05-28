# real number
import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 95.50
current_temp = 95.49999999

# expected output
print(f"Ideal temp: {ideal_temp}")
print(f"Current temp: {current_temp}")

# unexpected output
print(f"Diffent temp: {ideal_temp - current_temp}")


# show details or help for float infos
# note this can varry from every systems / computer compute power
print(f"float info: {sys.float_info}")

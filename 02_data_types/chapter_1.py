# Immutable Sample

sugar_amount = 2
# don't check with "value"
print(f"Initial sugar: {sugar_amount}")

sugar_amount = 12
# don't check with "value"
print(f"Second initial sugar: {sugar_amount}")

# check via "identity"
print(f"Identity/ID of 2: {id(2)}")
print(f"Identity/ID of 12: {id(12)}")

# How memory works?
  # sugar_amount name of variable
  # 2 and 12 is the value, both of these are saved in memory
  # it makes this "Immutable". This only changes the reference of sugar amount e.g.
      # sugar_amount      -> reference to             -> 2          -> memory saved [2]
      # sugar_amount      -> changed reference to     -> 12         -> memory saved [2, 12]
#Mutable

spice_mix = set()
print(f"Initial spice mix id: {id(spice_mix)}")
print(f"Initial spice mix: {spice_mix}")

# added values
spice_mix.add("Cinamon")
spice_mix.add("Ginger")
spice_mix.add("Lemon")
spice_mix.add(12)
print(f"After spice mix: {id(spice_mix)}")
print(f"After spice mix: {spice_mix}")


# set() = use to to store collection of data types
# How memory works?
  # spice_mix name of variable
  # objects store in set is saved in memory as single ID
  # it's "Mutable" because the object value can change but not the ID e.g.
      # spice_mix      -> reference to             -> {}                                    -> memory saved {} with single ID
      # spice_mix      -> changed reference to     -> {'Cinamon', 'Giner', 'Lemon'}         -> memory saved {'Cinamon', 'Giner', 'Lemon'} with still a single ID



# How memory works?
  # sugar_amount name of variable
  # 2 and 12 is the value, both of these are saved in memory
  # it makes this "Immutable". This only changes the reference of sugar amount e.g.
      # sugar_amount      -> reference to             -> 2          -> memory saved [2]
      # sugar_amount      -> changed reference to     -> 12         -> memory saved [2, 12]
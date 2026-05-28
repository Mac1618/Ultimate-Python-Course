# boolean and logical operations

is_boiling = True
stri_count = 5
water_hot = True
tea_added = False

# upcasting = adding number to boolean (converts to "1")
total_actions = stri_count + is_boiling
print(f"Total actions: {total_actions}")


# convert number to boolean
milk_present = 30
print(f"Is there milk? {bool(milk_present)}")


# "and" operator
can_serve = water_hot and tea_added
print(f"Can serve chai? {can_serve}")


# Boolean can also be read as 1 or 0
  # true = 1
  # false = 0

  # Values that can be perceived as false
    # None, 0, 
    # the rest are mostly true  

# Logical Operators
  # and, or, not
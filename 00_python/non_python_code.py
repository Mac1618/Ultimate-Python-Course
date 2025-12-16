def make_chai():
  if not keetle_has_water():
    fill_kettle()
  plug_in_kettle()
  boil_water()
  if not is_cup_clean():
    wash_cup()
  add_to_cup("tea leaves")
  add_to_cup("sugar")
  pour("water")
  stir("cup")
  serve("chai")

make_chai()
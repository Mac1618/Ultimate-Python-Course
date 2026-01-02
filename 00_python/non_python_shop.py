# class
class Chai:
  # initialize
  def __init__(self, sweetness, milk_level):
    self.sweetness = sweetness
    self.milk_level = milk_level

  # method 1
  def sip(self):
    print("Sipping a chai")

  # method 2
  def add_sugar(self, amount):
    print("Adding the sugar")

# calling class and methods
my_chai = Chai(sweetness="50%", milk_level="100%")
my_chai.add_sugar(amount="75%")
class Coordinate(object):
  # __init__ : special method to create an instance
  # self : parameter to refer to an instance of the class
  # x, y -> what data initializes a Coordinate object
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def distance(self, other):
    x_diff_sq = (self.x - other.x) ** 2
    y_diff_sq = (self.y - other.y) ** 2
    return (x_diff_sq + y_diff_sq) ** 0.5

  def __str__(self):
    return "<" + str(self.x) + "," + str(self.y) + ">"


c = Coordinate(3, 4)
b = Coordinate(10, 12)

print(c.distance(b))
print(b)
print(isinstance(c, Coordinate))
print(type(c))

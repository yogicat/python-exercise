class Animal(object):
	def __init__(self, age):
		self.age = age
		self.name = None
	def get_age(self):
		return self.age
	def get_name(self):
		return self.name
	def set_age(self, newage):
		self.age = newage
	def set_name(self, newname=""):
		self.name = newname
	def __str__(self):
		return "animal:" + str(self.name) + ":" + str(self.age)


class Cat(Animal):
  def speak(self):
    print("meow")
  # overrides Animal's __str__
  def __str__(self):
    return "cat:" + str(self.name) + ":" + str(self.age)

class Rabbit(Animal):
  # class variable tag
  tag = 1
  def __init__(self, age, name, )

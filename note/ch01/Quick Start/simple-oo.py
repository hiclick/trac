class AnimalAction():
	"""docstring for AnimalAction"""

	def quack(self):
		return self.strings["quack"]

	def feathers(self):
		return self.strings["feathers"]

	def bark(self):
		return self.strings["bark"]

	def fur(self):
		return self.strings["fur"]
		
class Duck(AnimalAction):
	"""docstring for Duck"""
	strings = dict(
		quack = "Quaaaak",
		feathers = "The duck has gray and white feathers",
		bark = "The duck cannot bark",
		fur = "The duck has no fur"
	)

class Person(AnimalAction):
	"""docstring for Person"""
	strings = dict(
		quack = "The person imitates a duck",
		feathers = "The person takes a feather from the ground and shows it",
		bark = "The person says woolf!",
		fur = "The person puts on a fur coat."
	)

def in_the_forest(duck):
	print duck.quack()
	print duck.feathers()

def at_home(person):
	print person.bark()
	print person.fur()

def main():
	donald = Duck()
	christen = Person()

	print "-- in the forest"

	for o in (donald, christen):
		in_the_forest(o)

	print "-- at home"

	for o in (donald, christen):
		at_home(o)

if __name__ == '__main__':
	main()
		
		

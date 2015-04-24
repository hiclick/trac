def main():
	fried = Egg()
	print fried.whatkind()

	scrambled = Egg("scrambled")
	print scrambled.whatkind()

class Egg(object):
	"""docstring for Egg"""
	def __init__(self, kind = "fried"):
		self.kind = kind
		
	def whatkind(self):
		return self.kind

def test():
	name = "christen"
	print name
		

if __name__ == '__main__':
	main()
	test()


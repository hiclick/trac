def main():
	func(1)
	func(3)
	func()

def func(a = 5):
	for i in range(a, 10):
		print i,
	print

if __name__ == '__main__':
	main()
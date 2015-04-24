def main():
	a, b = 2, 1
	print a, b, b, a
	s = "less than" if a < b else "greater than or equal to"
	print s

	if a < b:
		print "a is less than b"
	elif a > b:
		print "a is greater than b"
	else:
		print "a is equal to b"

if __name__ == '__main__':
	main()
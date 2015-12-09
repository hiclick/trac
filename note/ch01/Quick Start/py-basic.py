# -*- coding: utf-8 -*-

# Conditional 

a, b = 1, 5
if a < b:
    print "a is less than b"
else:
    print "a is not less than b"

print "foo" if a < b else "bar"

# Loop while

while b < 50:
    print b
    a, b = b, a + b
print "Done."

# Loop for

fh = open("lines.txt")
for line in fh.readlines():
    print line,
print

# Function 

def isPrime(n):
    if n == 1:
        print "1 is special"
        return False
    for x in range(2, n):
        if n % x == 0:
            print n, "is not a prime number"
            return False
    else:
        print n, "is a prime number"
        return True


# for n in range(1,10):
# isPrime(n)

# Simple OOP

class Fibonacci():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def series(self):
        while True:
            yield (self.b)
            self.a, self.b = self.b, self.a + self.b


f = Fibonacci(0, 1)

for r in f.series():
    if r > 100:
        break
    print r,

print




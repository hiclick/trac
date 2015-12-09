try:
    fh = open("lines.txt")
    for line in fh.readlines():
        print line,

except IOError as e:
    print "Some thind bad has happened"
    print e

print "after badness"
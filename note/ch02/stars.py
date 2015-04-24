__author__ = 'Christen'

def astarts(num):
    for x in range(num):
        while x >= 0:
            print '*',
            x -= 1
        print
    return

def dstarts(num):
    tmp = num - 1
    for x in range(tmp):
        while x < tmp:
            print '*',
            x += 1
        print
    return

y = 10
astarts(y)
dstarts(y)

print
print '* ' * 26
print '*', 'This scripts if written for print stars.'
print '* ' * 26


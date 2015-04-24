# -*- coding:utf-8 -*-
__author__ = 'Christen'

# f = open("/music/_singles/kairo.mp3", "rb")


# http://www.afterhoursprogramming.com/tutorial/Python/Reading-Files/

with open('test.txt', 'r') as f:
    data = f.readlines()
    for line in data:
        #words = line.split()
        #for word in words:
        print line.lower().replace(" ", "-")

# http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python










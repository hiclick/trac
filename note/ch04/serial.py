# -*- coding:utf-8 -*-
__author__ = 'Christen'

import random


def GenerateSerial():
    Letter = ["A", "B", "C", "D", "E", "F", "H", "K", "P", "Q", "S", "T", "W", "X", "Y", "Z"]
    Arabic = "23456897"
    salt = random.sample(Letter, 2)
    num = random.sample(Arabic, 8)
    serial = "".join(salt) + "".join(num)
    print serial


if __name__ == "__main__":
    print "请输入需要的数量："
    number = raw_input()
    for i in range(int(number)):
        GenerateSerial()
    #raw_input("Waiting...")
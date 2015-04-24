# -*- coding:utf-8 -*-
__author__ = 'Christen'


def getPrime(maxNum):
    aList = [x for x in range(0, maxNum)]
    prime = []
    for i in range(2, len(aList)):
        if aList[i] != 0:
            prime.append(aList[i])
            clear(aList[i], aList, maxNum)
    return prime


def clear(aPrime, aList, maxNum):
    for i in range(2, int((maxNum / aPrime) + 1)):
        if not aPrime * i > maxNum - 1:
            aList[i * aPrime] = 0


print getPrime(500)

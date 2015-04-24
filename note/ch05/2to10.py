# -*- coding:utf-8 -*-

def bin2dec(s):
    total = 0
    for i in s:
        total = 2 * total + (0 if i == '0' else 1)
    return total


def bin2dec2(bin):
    count = 0
    for i in range(0, len(bin)):
        if bin[i] == str(1):
            sum = 2 ** (len(bin) - i - 1)
            count += sum
    return count

a = '10000000000'

print(bin2dec(a))
print(bin2dec2(a))



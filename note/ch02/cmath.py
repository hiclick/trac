# coding: utf-8


# 大公约数递归算法
def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)


# 最小公倍数算法
def lcm(num1, num2):
    tmp = gcd(num1, num2)
    return num1 * num2 / tmp


# 欧几里德算法
def gcd_Euclid(m, n):
    while n:
        m, n = n, m % n
    return m


# 欧几里德的Python语言描述
def gcd_Python(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        temp = a % b
        a = b
        b = temp

    return a


#  Stein 算法
def gcd_Stein(a, b):
    if a < b:
        a, b = b, a
    if 0 == b:
        return a
    if a % 2 == 0 and b % 2 == 0:
        return 2 * gcd_Stein(a / 2, b / 2)
    if a % 2 == 0:
        return gcd_Stein(a / 2, b)
    if b % 2 == 0:
        return gcd_Stein(a, b / 2)

    return gcd_Stein((a + b) / 2, (a - b) / 2)


print gcd_Stein(180, 356)
print lcm(180, 356)

# http://www.cnitblog.com/donne/archive/2008/07/23/47050.html
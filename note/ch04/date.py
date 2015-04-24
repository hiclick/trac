# -*- coding:utf-8 -*-
__author__ = 'Christen'

# coding=gbk

import datetime
import random


def tm(m, count, y=2014):
    _res = []
    next_month = datetime.date(y, m + 1, 1)
    difference = datetime.timedelta(1)
    _month = next_month - difference

    for i in range(count):
        r1 = random.randint(0, _month.day - 1)
        r2 = random.randint(r1, _month.day - 1)
        _res.append(
            (_month - datetime.timedelta(r2)).strftime("%m.%d") + "-" + (_month - datetime.timedelta(r1)).strftime(
                "%m.%d"))
    _res.sort()

    # print _res

    return _res


if __name__ == '__main__':

    while True:

        try:
            month = int(raw_input('请输入需要随机的月份> ').replace(" ", ""))
            count = int(raw_input('请输入需要随机的数量> ').replace(" ", ""))
            res = tm(month, count)
            for ss in res:
                print ss
            yesno = raw_input('是否继续Y/N？').strip()[0]
            if yesno in 'Nn':
                break
        except:
            print '抛出异常'
            continue
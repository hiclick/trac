
# -*- coding:utf-8 -*-

import timeit
#执行命令
print timeit.Timer('x=range(1000)').timeit(1000000), " s"
print timeit.Timer('x=range(1000)').repeat(2, 1000000), " s"


#执行命令
print timeit.Timer('sum(x)', 'x = (i for i in range(1000))').timeit(), " s"




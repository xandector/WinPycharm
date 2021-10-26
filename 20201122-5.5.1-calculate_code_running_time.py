# 计算一段代码的执行时间

import time  # time模块可以获取当前的时间

# # 代码运行之前，获取一下时间
# start = time.time() # time模块里的time方法，可以获取当前时间的时间戳
# # 时间戳是从 1970-01-01 00:00:00 UTC 到现在的秒数
# # 北京时间转UTC需要减8个小时
# print('start =', start)
#
# x = 0
# for i in range(1, 100000000):
#     x += i
#
# print(x)
# # 代码运行完成以后，再获取一下时间
# end = time.time()
# print('代码运行耗时{}秒'.format(end - start))


def cal_time(fn):
    start = time.time()
    fn()
    end = time.time()
    print('代码运行耗时{}秒'.format(end - start))


def demo():
    y = 1
    for j in range(1, 100000):
        y *= j
    print(y)


cal_time(demo)




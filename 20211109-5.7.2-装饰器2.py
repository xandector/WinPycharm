import time


def cal_time(fn):

    def inner(x, *args, **kwargs):  # 接受多个形参
        # print('inner被调用')
        start = time.time()
        s = fn(x)
        end = time.time()
        return s, end - start

    return inner


@cal_time
def demo(n):
    x = 0
    for i in range(1, n):
        x += i
    return x


m = demo(100000, 'good', y='hello')
print('m的值是', m)


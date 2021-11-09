import time


def cal_time(fn):
    print('cal_time被调用')
    print('装饰前的demo = {}'.format(fn))

    def inner():
        print('inner被调用')
        start = time.time()
        fn()
        end = time.time()
        print('代码耗时', end - start)

    print('cal_time返回')
    return inner


@cal_time   # 第一件事调用cal_time；第二件事把被装饰的函数传递给fn
def demo():
    print('demo被调用')
    x = 0
    for i in range(1, 10000000):
        x += i
    print(x)
# 装饰器作用在函数定义时就已经完成


@cal_time
def foo():
    print('foo被调用')
    print('Hello')
    time.sleep(2)
    print('World')


# 第三件事：当再次调用demo函数时，此时的demo已经不再是上面的demo
print('装饰后的demo = {}'.format(demo))
demo()
print('装饰后的foo = {}'.format(foo))
foo()

# def say_hello(name, age, city="襄阳"):  # 形参city设置了一个默认值
#     print("大家好，我是{}，我今年{}岁了，我来自{}".format(name, age, city))
#
#
# say_hello('Jack', 19)  # 如果没有传递参数，会使用默认值
# say_hello('Tony', 20, '北京')  # 如果传递参数，就使用传递的实参
#
# say_hello(name='David', age=23, city='广州')
# # 如果有位置参数和关键字参数，关键字参数一定要放在位置参数的后面
# say_hello('Jerry', age=25, city='南京')  # 可以直接传递单个参数，也可以使用变量赋值的形式传递参数


# def add(a, b):
#     return a + b


# def add_many(itera):
#     x = 0
#     for n in itera:
#         x += n
#     return x
#
#
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(add_many(nums))
# print(add_many((5, 4, 2, 3, 6, 7, 9, 6, 3, 2)))
# print(add_many({5, 7, 8, 9}))
# print(add_many(range(2, 19)))


# def add(a, b, *args):  # *args表示可变参数
#     print('a = {}, b = {}'.format(a, b))
#     print('args = {}'.format(args))  # 多出来的可变参数会以元组的形式保存到args里
#     c = a + b
#     for arg in args:
#         c += arg
#     return c
#
#
# print(add(1, 3))
# # ==> a = 1, b = 3
# # ==> args = ()
# # ==> 4
# print(add(1, 3, 4, 5, 7, 8, 34, 5))
# # ==> a = 1, b = 3
# # ==> args = (4, 5, 7, 8, 34, 5)
# # ==> 67


# def add(a, b, *args, mul=1, **kwargs):  # **kwargs 表示可变的关键字参数
#     print('kwargs = {}'.format(kwargs))     # 多出来的关键字参数会以字典的形式保存
#     c = a + b
#     for arg in args:
#         c += arg
#     return c * mul
#
#
# print((add(1, 3, 5, 7, mul=2, x=0, y=4)))
# # ==> kwargs = {'x': 0, 'y': 4}
# # ==> 32
# add(9, 5, 4, 7, 8, p=9, q=10)

# def test(a):
#     print('修改前a的内存地址0x%X' % id(a))
#     a = 100
#     print('修改后a的内存地址0x%X' % id(a))


# def demo(nums):
#     print('修改前nums的内存地址0x%X' % id(nums))
#     nums[0] = 10
#     print('修改后nums的内存地址0x%X' % id(nums))
#
#
# x = 1
# print('调用前x的内存地址0x%X'% id(x))
# test(x)
# print('调用前x的内存地址0x%X'% id(x))
# print(x)
# # ==> 调用前x的内存地址0x7FFF247316A0
# # ==> 修改前a的内存地址0x7FFF247316A0
# # ==> 修改后a的内存地址0x7FFF24732300
# # ==> 调用前x的内存地址0x7FFF247316A0
# # ==> 1
#
# y = [3, 4, 5, 6, 7, 8]
# print('修改前nums的内存地址0x%X' % id(y))
# demo(y)
# print('修改后nums的内存地址0x%X' % id(y))
# print(y)
# # ==> 修改前nums的内存地址0x250172C0300
# # ==> 修改前nums的内存地址0x250172C0300
# # ==> 修改后nums的内存地址0x250172C0300
# # ==> 修改后nums的内存地址0x250172C0300
# # ==> [10, 4, 5, 6, 7, 8]


# def test(a, b):
#     print('hello,a = {},b = {}'.format(a, b))
#
#
# def test(x):
#     print('good, x= {}'.format(x))
#
#
# test(3, 4)

# # test = 对应的是一个函数
# def test(x):
#     print('good, x= {}'.format(x))
# 
#
# test = 5
#
# test(3)

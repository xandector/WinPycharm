# def add(a, b):
#     return a + b
#
#
# x = add(4, 5)  # 函数名（实参）作用是调用函数，获取到函数的执行结果，并复制给变量x
# print(x)
#
# fn = add  # 相当与给函数add起了一个别名
# print(fn(3, 7))

# # 除了使用def关键字定义一个函数以外，我们还能使用lambda表达式定义一个函数
# # 匿名函数用来表达一个简单的函数，函数调用的次数很少，基本上就是调用一次
# # 调用匿名函数两种方式：
# # 1. 给它定义一个名字（很少这样使用）
# # 2. 把这个函数当作参数传给另一个函数使用(使用场景比较多）
# mul = lambda a, b: a * b
# mul(4, 5)


# def calc(a, b, fn):
#     c = fn(a, b)
#     return c
#
#
# # def add(x, y):
# #     return x + y
# #
# #
# # def minus(x, y):
# #     return x - y
# #
# #
# # x1 = calc(1, 2, add)
# # print(x1)
# # x2 = calc(10, 5, minus)
# # print(x2)
#
# x3 = calc(1, 2, lambda x, y: x + y)
# x4 = calc(10, 5, lambda x, y: x - y)
# x5 = calc(5, 6, lambda x, y: x * y)
# x6 = calc(12, 4, lambda x, y: x - y)
# print(x3, x4, x5, x6)


# # 有几个内置函数和内置类，用到了匿名函数
# nums = [4, 8, 2, 1, 7, 6]
#
# # 列表的sort方法，会直接对列表进行排序
# # nums.sort()
# # print(nums)
#
# ints = (5, 9, 5, 32, 5, 4, 7, 5, 1, 2)
# # sorted内置函数，不会改变原有的数据，而是生成一个新的结果
# x = sorted(nums)
# print(x)
# # ==> [1, 2, 4, 6, 7, 8]
# # 可以将元组排列成新的列表
# y = sorted(ints)
# print(y)
# # ==> [1, 2, 4, 5, 5, 5, 5, 7, 9, 32]

# students = [
#     {'name': 'zhangsan', 'age': 18, 'score': 98, 'height': 180},
#     {'name': 'lisi', 'age': 19, 'score': 66, 'height': 171},
#     {'name': 'Jack', 'age': 20, 'score': 59, 'height': 160},
#     {'name': 'Tony', 'age': 22, 'score': 88, 'height': 186},
#     {'name': 'Jerry', 'age': 28, 'score': 75, 'height': 168},
#     {'name': 'David', 'age': 16, 'score': 16, 'height': 159}
# ]
#
# # def foo(ele):
# #     return ele['age']   # 通过返回值告诉sort方法，按照元素哪个属性进行排序
#
#
# # 需要传递参数key指定比较规则
# # key参数类型是函数=
# # 在sort内部实现的时候，调用了foo方法，并且传入了一个参数（列表元素）
# # students.sort(key=foo)
# students.sort(key=lambda ele: ele['score'])
# print(students)

# ages = [12, 23, 32, 50, 88, 6, 48]
# # filter可以给定两个参数，第一个参数是函数，第二个参数是可迭代对象
# x = filter(lambda ele: ele > 18, ages)
# # filter结果是一个filter类型的对象,是可迭代对象
# print(x)
# # ==> <filter object at 0x00000192D3046670>
# for a in x:
#     print(a)
# # ==> 23
# # ==> 32
# # ==> 50
# # ==> 88
# # ==> 48

# ages = [12, 23, 32, 50, 88, 6, 48]
# m = map(lambda ele: ele + 2, ages)
# print(list(m))
# # ==> [14, 25, 34, 52, 90, 8, 50]


# from functools import reduce  # 导入模块的语法
#
# scores = [100, 89, 67, 76, 53]
# print(reduce(lambda ele1, ele2: ele1 + ele2, scores))
# # ==> 385

from functools import reduce

students = [
    {'name': 'zhangsan', 'age': 18, 'score': 98, 'height': 180},
    {'name': 'lisi', 'age': 19, 'score': 66, 'height': 171},
    {'name': 'Jack', 'age': 20, 'score': 59, 'height': 160},
    {'name': 'Tony', 'age': 22, 'score': 88, 'height': 186},
    {'name': 'Jerry', 'age': 28, 'score': 75, 'height': 168},
    {'name': 'David', 'age': 16, 'score': 16, 'height': 159}
]


print(reduce(lambda x,y:x+y['age'], students, 0))

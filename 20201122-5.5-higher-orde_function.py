# def foo():
#     print('我是foo，我被调用了')
#     return 'foo'
#
#
# def bar():
#     print('我是bar，我被调用了')
#     return foo()
#
#
# bar()
# # ==> 我是bar，我被调用了
# # ==> 我是foo，我被调用了
#
# x = bar()
# print('x的值是{}'.format(x))
# # ==> 我是bar，我被调用了
# # ==> 我是foo，我被调用了
# # ==> x的值是foo

# def foo():
#     print('我是foo，我被调用了')
#     return 'foo'
#
#
# def bar():
#     print('我是bar，我被调用了')
#     return foo
#
#
# x = bar()
# print('x的值是{}'.format(x))
# print('-----------------------------')
# x()
# # ==> 我是bar，我被调用了
# # ==> x的值是<function foo at 0x00000273FDA67C10>
# # ==> -----------------------------
# # ==> 我是foo，我被调用了
#
# y = bar()()
# print(y)
# # ==> 我是bar，我被调用了
# # ==> 我是foo，我被调用了
# # ==> foo
#
#
# # 装饰器
# def outer():
#     m = 100
#
#     def inner():
#         n = 90
#         print('我是inner函数')
#
#     print('我是outer函数')
#     return inner
#
#
# outer()
# # ==> 我是outer函数
# outer()()
# # ==> 我是outer函数
# # ==> 我是inner函数


# def test():
#     print('我是一个函数')
#     return 'hello'
#
#
# def demo():
#     print('我是demo函数')
#     return test
#
#
# def bar():
#     print('我是bar函数')
#     return test()
#
#
# x = test()
# print(x)
# # ==> 我是一个函数
# # ==> hello
#
# y = demo()
# print(y)
# z = y()
# print(z)
# # ==> 我是demo函数
# # ==> <function test at 0x000001ED8E677C10>
# # ==> 我是一个函数
# # ==> hello
#
# a = bar()
# print(a)
# # ==> 我是bar函数
# # ==> 我是一个函数
# # ==> hello

# 函数嵌套
# def outer(x):
#     m = 100  # 局部变量
#     print('我是outer函数')
#
#     def inner():  # inner函数是定义在outer函数内部的一个函数
#         print('我是inner函数')
#
#     if x > 18:
#         inner()
#
#     return 'hello'
#
#
# print(outer(21))
# # ==> 我是outer函数
# # ==> 我是inner函数
# # ==> hello

# # 函数闭包
# def outer(n):
#     num = n
#
#     def inner():
#         return num+1
#     return inner
#
#
# print(outer(3)())
# # ==> 4
# print(outer(5)())
# # ==> 6

def outer():
    x = 10  # 在外部函数里定义了一个变量x，是一个局部变量

    def inner():
        # 在内部函数如何修改外部函数的局部变量
        nonlocal x  # 此时，这里的x不再是新增的变量，而是外部的局部变量x
        y = x + 1
        print('inner里的y =', y)
        x = 20  # 不是修改外部的x变量，而是在inner函数内部又创建了一个新的变量x

    return inner


outer()()
# ==> inner里的y = 11

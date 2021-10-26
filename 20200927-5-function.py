# def tell_story():
#     print('从前有座山')
#     print('山上有座庙')
#     print('庙里有个老和尚')
#     print('还有一个小和尚')
#     print('老和尚再给小和尚讲故事')
#     print('故事的内容是:')
#
#
# age = int(input('Please type in age:'))
# if 0 <= age < 3:
#     for i in range(5):
#         tell_story()
# elif age >= 3:
#     tell_story()

# # 函数的参数
# def tell_story(place, person1, person2):
#     print('从前有座山')
#     print('山上有座' + place)
#     print('庙里有个' + person1)
#     print('还有一个' + person2)
#     print(person1 + '再给' + person2 + '讲故事')
#     print('故事的内容是:')
#
#
# tell_story('道观', '老道', '道童')  # 会把实参一一对应的传递，交给形参处理
# # ==> 从前有座山
# # ==> 山上有座道观
# # ==> 庙里有个老道
# # ==> 还有一个道童
# # ==> 老道再给道童讲故事
# # ==> 故事的内容是:
#
# tell_story('尼姑庵', '师太', '小尼姑')
# # ==> 从前有座山
# # ==> 山上有座尼姑庵
# # ==> 庙里有个师太
# # ==> 还有一个小尼姑
# # ==> 师太再给小尼姑讲故事
# # ==> 故事的内容是:
#
# tell_story(place='禅院', person1='禅师', person2='青年')
# # ==> 从前有座山
# # ==> 山上有座禅院
# # ==> 庙里有个禅师
# # ==> 还有一个青年
# # ==> 禅师再给青年讲故事
# # ==> 故事的内容是:

# def add(a, b):
#     c = a + b   # c在函数外部时不可见的，只能在函数内部使用
#     return c    # return表示一个函数的执行结果
#
#
# # 获取add结果的四次方
# result = add(1, 2)
# print(result ** 4)
# # ==> 81

# # print就是一个无返回的内置函数
# x = print('hello')
# print(x)
# # ==> None
# # input是一个有返回的内置函数
# age = int(input('Please type in your age:'))
# print(age)


# # 函数的说明（注释）
# def add(a, b):
#     """
#     这个函数用来将两个数字相加
#     :param a:第一个数字
#     :param b:第二个数字
#     :return:两个数之和
#     """
#     return a + b

# 通过定义类型规范入参
def add(a: int, b: int):
    """
    这个函数用来将两个数字相加
    :param a:第一个数字
    :param b:第二个数字
    :return:两个数之和
    """
    return a+b


# # 使用help函数可以查看函数描述文档
# help(add)
# # ==> add(a, b)
# # ==>     这个函数用来将两个数字相加
# # ==>     :param a:第一个数字
# # ==>     :param b:第二个数字
# # ==>     :return:两个数之和

x = add(1, 2)
print(x)
y = add('hello', 'world')  # 会提示需要入参为int，获得了str
print(y)
# z = add('hello', 5)  # 字符串不能和整形相加
# print(z)
# 会报错：TypeError: can only concatenate str (not "int") to str

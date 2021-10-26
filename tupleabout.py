# # 使用一对（）小括号来表示元组
# nums = (9, 4, 3, 1, 7, 6)
#
# print(nums[3])
# print(nums.index(7))
# print(nums.count(9))

# ages = (18)
# print(type(ages))
# # ==> <class 'int'>
# # 单个元组需要在后面加一个逗号，不然为int类型
# ages = (18,)
# print(type(ages))
# # ==> <class 'tuple'>
#
# # 可迭代对象转换位元组
# print(tuple('hello'))
# # ==> ('h', 'e', 'l', 'l', 'o')
#
# # 怎样把列表转换成为元组？元组转换成为列表
# words = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# print(tuple(words))
# # ==> ('A', 'B', 'C', 'D', 'E', 'F', 'G')
# nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(list(nums))
# # ==> [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # 使用join联合元组中各字符串输出
# height = ("189", "174", "170")
# print('*'.join(height))
# # ==> 189*174*170
# print("".join(('h', 'e', 'l', 'l', 'o')))
# # ==> hello

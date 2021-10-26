# # +：可以用来拼接，用于字符串、元组、列表
# print('hello' + 'world')
# # ==> helloworld
# print(('good', 'yes') + ('hi', 'ok'))
# # ==> ('good', 'yes', 'hi', 'ok')
# print([1, 2, 3] + [4, 5, 6])
# # ==> [1, 2, 3, 4, 5, 6]
#
# # -：只能用于集合，求差集
# print({1, 2, 3} - {3})
# # ==> {1, 2}
#
# # *：可以用于字符串元组列表，表示重复多次
# # 不能用于字典和集合（不允许重复）
# print('hello' * 3)
# # ==> hellohellohello
# print([1, 2, 3] * 3)
# # ==> [1, 2, 3, 1, 2, 3, 1, 2, 3]
# print((1, 2, 3,) * 3)
# # ==> (1, 2, 3, 1, 2, 3, 1, 2, 3)
#
# # in：成员运算符
# print('a' in 'abc')
# # ==> True
# print(1 in [1, 2, 3])
# # ==> True
# print(4 in (4, 5, 6))
# # ==> True
# # in用于字典是用来判断key是否存在
# print('name' in {'name': 'zhangsan', 'age': 18, 'height': '180cm'})
# # ==> True
# print(3 in {1, 2, 3})

# # 字符串遍历
# a_str = "hello world"
# for char in a_str:
#     print(char, end=' ')
# # ==> h e l l o   w o r l d

# # 列表遍历
# a_list = [1, 2, 3, 4, 5]
# for num in a_list:
#     print(num, end=' ')
# # ==> 1 2 3 4 5

# # 元组遍历
# a_tuple = (1, 2, 3, 4, 5)
# for num in a_tuple:
#     print(num, end=' ')
# # ==> 1 2 3 4 5

# 带下标遍历
nums = [12, 9, 8, 5, 4, 7, 3, 6]
# 将列表nums包装成enumerate对象
for i, num in enumerate(nums):  # i表示元素下标，num表示列表里的元素
    print('第%d个元素是%d' % (i, num))
# ==> 第0个元素是12
# ==> 第1个元素是9
# ==> 第2个元素是8
# ==> 第3个元素是5
# ==> 第4个元素是4
# ==> 第5个元素是7
# ==> 第6个元素是3
# ==> 第7个元素是6

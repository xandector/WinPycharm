# names = {'zhangsan', 'lisi', 'jack', 'tony', 'jack', 'lisi'}
# print(names)
#
# names.add('Xa')
# print(names)

# names.clear()
# print(names)

# names.pop()
# print(names)
#
# names.remove('jack')
# print(names)
#
# print(names.union({'Henry', 'Ivy'}))
#
# print(names.update({'Ron', 'Harry'}))
# print(names)

# first = {'A', 'B', 'C', 'D', 'E', 'F'}
# second = {'A', 'B', 'C', 'J', 'K', 'L'}
# third = {'D', 'B', 'J', 'P', 'Q', 'R'}
#
# # set支持很多算数运算符
# # print(first + second) # 不支持加法
# print(first - second)  # 支持减法，去掉后者重复的元素
# # ==> {'D', 'F', 'E'}
# print(second - first)
# # ==> {'J', 'K', 'L'}
# print(first & second)
# # ==> {'B', 'A', 'C'}
# print(first | second)
# # ==> {'C', 'A', 'E', 'B', 'K', 'L', 'J', 'F', 'D'}
# print(first ^ second)
# # ==> {'E', 'D', 'J', 'L', 'F', 'K'}


# # 去重排序
# nums = [5, 8, 7, 6, 4, 1, 3, 5, 1, 8, 4]
# setnums = set(nums)
# print(setnums)  # 如果转换集合元素为数字，则会自动排序
# # ==> {1, 3, 4, 5, 6, 7, 8}
# anums = list(setnums)
# print(anums)
# # ==> [1, 3, 4, 5, 6, 7, 8]
# anums.sort(reverse=True)
# print(anums)
# # ==> [8, 7, 6, 5, 4, 3, 1]

# # 内置类 list typle set
# nums = [9, 8, 4, 3, 2, 1, ]
# x = tuple(nums)  # 转换tup内置类转换成为元组
# print(x)
# # ==> (9, 8, 4, 3, 2, 1)
#
# y = set(x)  # 使用set内置类转换成为集合
# print(y)
# # ==> {1, 2, 3, 4, 8, 9}
#
# z = list({'name': 'zhangsan', 'age': 18, 'score': 98})  # 字典转换列表保存为key的列表
# print(z)
# # ==> ['name', 'age', 'score']


# # Python里有一个比较强大的内置函数eval，可以执行字符串里的代码
# a = 'print("请输入您的用户名")'    # a是一个字符串
# eval(a)
# # ==> 请输入您的用户名
# b = '1+1'
# print(eval(b))
# # ==> 2

# import json
#
# # JSON的使用: 把列表、元组、字典等转换成为JSON字符串
# person = {'name': 'zhangsan', 'age': 18, 'gender': 'female'}
# # 字典如果想要把他传给前端页面，或者把字典写入到一个文件里
# m = json.dumps(person)  # dumps方法将字典、列表、集合、元组等转换成为JSON字符串
# print(m)
# # ==> {"name": "zhangsan", "age": 18, "gender": "female"}
# print(type(m))  # 转换后类型为字符串
# # ==> <class 'str'>
#
# n = '{"name": "lisi", "age": 20, "gender": "male"}'
# p = eval(n)
# print(type(p))
# # ==> <class 'dict'>
# s = json.loads(n)   # loads方法可以将JSON字符串转换成为Python里的数据
# print(s)
# # ==> {'name': 'lisi', 'age': 20, 'gender': 'male'}

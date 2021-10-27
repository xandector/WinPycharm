# # 列表可以存储任意数据类型，但是一般情况下我们都存储单一数据类型
# names = ['zhangsan', 'lisi', 'wangwu']
# scores = [100, 99, 98, 97]
# # 列表只能存储值，但是无法对值进行描述
# person = ['zhangsan', 18, 98, 97, 95, 93, 180, 150]

# 使用大括号来表示一个字典，不仅有值value，还有只的描述key
# 字典里的数据都是以键值对key-value的形式保留的
# key和value之间使用冒号:来连接
# 多个键值对之间使用逗号,来分隔
# person = {'name': 'zhangsan',
#           'age': 18,
#           'math': 98, 'Chinese': 95,
#           'English': 97, 'PE': 94,
#           'height': 180,
#           'weight': 150
#           }
# print(person)
# print(person['name'])
# x = 'age'
# print(person[x])
#
# print(person.get('sex'))
#
# print(person.get('sex', 'female'))
# print(person.get('name', 'lisi'))
#
# print(person)

# person['name'] = 'lisi'
# print(person)
#
# person['gender'] = 'female'
# print(person)

# person.pop('name')
# print(person)
#
# result = person.popitem()
# print(person)
# print(result)

# del person['name']
# print(person)
#
# person.clear()
# print(person)

# # 列表可以使用extend方法将两个列表合并成为一个列表
# nums1 = [1, 2, 3, 4, 5, 6, 7]
# nums2 = [8, 9, 10]
# nums1.extend(nums2)
# print(nums1)
# personA = {'addr': 'ZQ', 'job': 'worker'}
# person.update(personA)
# print(person)
#
# tuple1 = ('hello', 'good')
# tuple2 = ('hello', 'ok')
# print(tuple1 + tuple2)

# person = {'name': 'zhangsan', 'age': 18, 'height': '180cm'}
# for x in person:
#     print(x)
# for x in person:
#     print(x, '=', person[x])

# print(person.keys())
# for k in person.keys():
#     print(k, '=', person[k])

# for v in person.values():
#     print(v)

# print(person.items())
#
# for item in person.items():
#     print(item[0], '=', item[1])
#
# for k, v in person.items():
#     print(k, '=', v)

# chars = ['a', 'c', 'x', 'd', 'p', 'a', 'p', 'a', 'c', 'c']
# char_count = {}
#
# for c in chars:
#     # if c in char_count:
#     #     char_count[c] += 1
#     # else:
#     #     char_count[c] = 1
#     if c not in char_count:
#         char_count[c] = chars.count(c)
# print(char_count)
#
# n_count = char_count.values()
# max_count = max(n_count)
# # ==> 3
# for k, v in char_count.items():
#     if v == max_count:
#         print(k)

# # 让用户输入姓名，如果姓名已经存在，提示用户；
# # 如果姓名不存在，继续输入年龄，并存入列表里
# persons = [
#     {'name': 'zhangsan', 'age': 18},
#     {'name': 'lisi', 'age': 19},
#     {'name': 'Jack', 'age': 21}
# ]
# in_name = input('请输入姓名：')
# for person in persons:
#     if person['name'] == in_name:
#         print('该名字已存在！')
#         break
# else:
#     in_age = int(input('请输入年龄：'))
#     persons.append({'name': in_name, 'age': in_age})
#     print('信息已录入：', persons)


# # 调换字典key和value的位置
# dict1 = {'a': 100, 'b': 200, 'c': 300}
# dict1 = {v: k for k, v in dict1.items()}
# print(dict1)

# # 声明一个字典保存一个学生的信息，学生信息中包括：姓名、年龄、成绩（单科)、电话、性别、（男、女、不明）
# student = {
#     'name': 'X',
#     'age': 18,
#     'Chinese': 100,
#     'math': 100,
#     'English': 100,
#     'phone': 18888888888,
#     'sexuality': 'M'
# }
# 生命一个列表，在列表中保存6个学生的信息
students = [
    {'name': 'X', 'age': 18, 'mark': 90, 'phone': '18888888888', 'sexuality': 'M'},
    {'name': 'Y', 'age': 18, 'mark': 59, 'phone': '17777777777', 'sexuality': 'F'},
    {'name': 'Z', 'age': 17, 'mark': 80, 'phone': '16666666666', 'sexuality': 'Unknown'},
    {'name': 'AA', 'age': 20, 'mark': 20, 'phone': '15555555555', 'sexuality': 'M'},
    {'name': 'BB', 'age': 18, 'mark': 100, 'phone': '14444444444', 'sexuality': 'F'},
    {'name': 'CC', 'age': 16, 'mark': 97, 'phone': '13333333333', 'sexuality': 'M'},
]
# print(students)

# 1.统计不及格学生个数
count = 0
for student in students:
    if student['mark'] < 60:
        count += 1
print('一共有%d人不及格' % count)

# 2.打印不及格学生的名字和对应的成绩
for student in students:
    if student['mark'] < 60:
        print(student['name'], ':', student['mark'], '分')

# 3.统计未成年学生的个数
underage_count = 0
for student in students:
    if student['age'] < 18:
        underage_count += 1
print('未成年学生有%d个' % underage_count)

# 4.打印手机尾号是8的学生的名字
lucky8 = []
for student in students:
    p = student['phone']
    if p.endswith('8'):
        lucky8.append(student['name'])
print('手机尾号是8的同学：', lucky8)

# 5.打印最高分和对应的学生的名字
max_mark = 0
for student in students:
    if student['mark'] > max_mark:
        max_mark = student['mark']
        max_student = student['name']
print('最高分的是%s，拿到了%d分' % (max_student, max_mark))

# # 6.删除性别不明的所有学生（坑）
# unknown_list = []
# for student in students:
#     if student['sexuality'] != 'M' and student['sexuality'] != 'F':
#         unknown_list.append(student)
# print(unknown_list)
# for u in unknown_list:
#     students.remove(u)
# print(students)

# 7.将列表按学生成绩从大到小排序（选）
ii = 0
while ii < len(students):
    i = 0
    while i < len(students) - 1 - ii:
        stu1 = students[i]
        stu2 = students[i+1]
        mark1 = stu1['mark']
        mark2 = stu2['mark']
        if mark1 < mark2:
            students[i], students[i + 1] = students[i + 1], students[i]
        i += 1
    ii += 1
print(students)

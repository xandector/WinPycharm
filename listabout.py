# names = ['Jack', 'John', 'Bruce', 'Hugh', 'Tim']
# print(names[2])
# names[2] = 'Bruce Wayne'
# print(names[1:3])

# # append：在列表的最后面追加一个数据
# names = ['Jack', 'John', 'Bruce', 'Hugh', 'Tim']
# print(names)
# names.append('Ivan')
# print(names)
# # insert：在指定下标元素前方插入元素
# names.insert(2, 'Frank')
# print(names)
# # extend：在
# insertnames = ['Bill', 'Steve', 'Linus']
# names.extend(insertnames)
# print(names)

# # pop: 默认删除列表最后一个数据(输入下标时则为对应位置数据），并且返回此数据
# names = ['Jack', 'John', 'Bruce', 'Hugh', 'Tim']
# popname1 = names.pop()
# popname2 = names.pop(2)
# print(names)
# print(popname1, popname2)
# # ==> ['Jack', 'John', 'Bruce', 'Hugh']
# # ==> Tim

# names = ['Jack', 'John', 'Bruce', 'Hugh', 'Tim']
# names.remove('Hugh')
# print(names)
#
# del names[2]
# print(names)

# # clear: 用来清空列表
# names = ['Jack', 'John', 'Bruce', 'Hugh', 'Tim']
# names.clear()
# print(names)
# # ==>

# names = ['Jack', 'John', 'Bruce', 'Hugh', 'Tim']
# print(names.index('John'))

# # count: 计算列表内指定元素个数
# names = ['Jack', 'John', 'Bruce', 'Hugh', 'Tim','Jack']
# print(names.count('Jack'))
# # ==> 2
#
# # in : 返回元素是否在表中
# names = ['Jack', 'John', 'Bruce', 'Hugh', 'Tim']
# print('John' in names)
# # ==> True

# names = ['Jack', 'John', 'Bruce', 'Hugh', 'Tim']
# names[4] = 'Tom'
# print(names)
# # ==>

# # for in 遍历
# names = ['Jack', 'John', 'Bruce', 'Hugh', 'Tim']
# for name in names:
#     print(name)

# names = ['Jack', 'John', 'Bruce', 'Hugh', 'Tim']
# i = 0
# while i < len(names):
#     print(names[i])
#     i += 1
#
# a = 13
# b = 20
# a, b = b, a
# print(a,b)

# # sorter: 只返回一个排序后的列表，原对象不变动
# nums = [1,3,2,5,34,6,8,23,346,120]
# snums = sorted(nums)
# print(nums)
# print(snums)

# # reverse：将列表顺序反转
# names = ['Jack', 'John', 'Bruce', 'Hugh', 'Tim']
# print(names)
# names.reverse()
# print(names)
#
# # 切片方法也可反转顺序
# print(names[::-1])

# a = 12
# b = a
# print('修改前， a={}, b={}'.format(id(a), id(b)))
# a = 10
# print('修改后， a={}, b={}'.format(id(a), id(b)))

# nums1 = [100, 200, 300]
# nums2 = nums1
# print('nums1 = %x, nums2 = %x' %(id(nums1),id(nums2)))
# nums1[0] = 1
# print('nums1 = %x, nums2 = %x' %(id(nums1),id(nums2)))

# # 调用copy方法，可以复制一个列表
# # 新列表内容一样，指向地址不同
# x = [100, 200, 300]
# y = x
# z = x.copy()
#
# print('0x%X, 0x%X, 0x%X' % (id(x), id(y), id(z)))

# # 求列表里的最大数及下标
# nums = [3, 1, 9, 8, 3, 4, 1, 6, 9, 5]
# i = 0
# n = 0
# while i < len(nums):
#     if nums[i] > nums[n]:
#         n = i
#     i += 1
# print('The biggest is No.', n+1, ':', nums[n])

# nums = [3, 1, 9, 8, 3, 4, 1, 6, 9, 5]
# x = nums[0]
# index = 0
# for num in nums:
#     if num > x:
#         x = num
#         index = nums.index(x)
# print('The bigest is No.%d : %d' % (index, x))

# # 在使用for...in遍历列表时，最好不要对元素进行增删操作
# x = ['hello', 'good', '', '', 'yes', 'ok', '']
# # for xxs in x:
# #     if len(xxs) == 0:
# #         x.remove(xxs)
# # print(x)
#
# # i = 0
# # while i < len(x):
# #     if x[i] == '':
# #         x.remove(x[i])
# #         i -= 1
# #     i += 1
# # print(x)
#
# x2 = []
# for xs in x:
#     if xs != '':
#         x2.append(xs)
# print(x)
# print(x2)

# from defx_findListLargest import findListLargest
#
# x = ['h', 'e', 'l', 'l', 'o', 'g', 'o', 'o', 'd', 'y', 'e', 's', 'o', 'k']
# xcount = []
# i = 0
# while i < len(x):
#     n = i
#     xcount.insert(i, 0)
#     while n < len(x):
#         if x[n] == x[i]:
#             xcount[i] += 1
#         n += 1
#     i += 1
# count = findListLargest(xcount)
# print('Most used is', x[count], 'and the frequncy is %d' % xcount[count])

# # 一个学校，有3个办公室，像现在有8位老师等待工位的分配，请编写程序，完成随机的分配
# import random
#
# teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# rooms = [[], [], []]
# for teacher in teachers:
#     room = random.choice(rooms)
#     room.append(teacher)
# print(rooms)
#
# # for循环遍历带下标
# for i, room in enumerate(rooms):
#     print('Room %d has %d teachers:' % (i, len(room)), room)

# nums = [i for i in range(10)]
# print(nums)
# # 等价于↓
# # nums = []
# # for i in range(10):
# #   nums.append(i)
# x = [i for i in range(10) if i % 2 == 0]
# print(x)
# y = [i for i in range(10) if i % 2]
# print(y)
#
# points = [(x, y) for x in range(5, 9) for y in range(10, 20)]
# print(points)


# # # 请写出代码实现分组一个list里面的元素，比如[1, 2, 3,...100]变成[[1,2,3],[4,5,6]....]
# x = [i for i in range(1, 101)]
# # xbig = []
# # print(x)
# # n = 0
# # while n + 3 <= len(x):
# #     xsmall = [x[n], x[n + 1], x[n + 2]]
# #     xbig.append(xsmall)
# #     n += 3
# # xsmall = []
# # while n < len(x):
# #     xsmall.append(x[n])
# #     n += 1
# # xbig.append(xsmall)
# # print(xbig)
# y = [x[i:i + 3] for i in range(0, 100, 3)]
# print(x)
# print(y)


# import copy
# # 浅复制（拷贝）
# nums = [1, 2, 3, 4, 5]
# nums1 = nums # 非深/浅复制，纯粹赋值
#
# nums2 = nums.copy() # 浅拷贝，两个内容一模一样，不是同一个对象
# nums3 = copy.copy(nums) # 和上行功能一致，都是浅拷贝
#
# # 深复制（拷贝）
# # 只能使用copy模块实现
# words = ['hello', 'good', [100, 200, 300], 'yes', 'hi', 'ok']
# # word1是words的浅拷贝
# words1 = words.copy()
# words[0] = '你好'
# print(words1)
# # ==> ['hello', 'good', [100, 200, 300], 'yes', 'hi', 'ok']
# words[2][0] = 1
# print(words1)
# # ==> ['hello', 'good', [1, 200, 300], 'yes', 'hi', 'ok']
# 浅拷贝只拷贝第一层，包含的列表只指向，不复制

# import copy
# words = ['hello', 'good', [100, 200, 300], 'yes', 'hi', 'ok']
# words2 = copy.deepcopy(words)
# words[0] = '你好'
# words[2][0] = 1
# print(words)
# print(words2)

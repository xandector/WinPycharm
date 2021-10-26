# # 使用内置函数len可以获取字符串长度
# x = 'abcdefghijklmn'
# print(len(x))
#
# # 查找内容相关方法，可以获取指定字符的下标
# # find：寻找自定字符或组合,找到第一个后马上返回对应位置
#  print(x.find('lm'))

# # print(x.index('l'))
#
# word = 'hello'
# word1 = word.replace('l', 'x')
# print(word1)
#
# a = 'hello'
# b = input('Type in a character:')
#
# for c in a:
#     if c == b:
#         print('Yes')
#         break
# else:
#     print('No')
#

# a = 'hello'
# b = input('Type in a character:')
#
# if b in a:
#     print('Yes')
# else:
#     print('No')

# name = 'Jack'
# age = 18
# print('Hi! My name is %s, %d now, has %f dollar' % (name, age, 68.34))
# print('Hi! I\'m No.%3d.' % 5)
# print('Hi! I\'m No.%-3d.' % 5)
# print('Hi! I\'m No.%03d.' % 5)
#
# print('PI = %.2f' % 3.141592653)
# print('%x' % 255)
# print('%X' % 255)
# print('This is %%s and that is %d' % 10)

x = 'Hi, I\'m {}, {} now'.format('Jack', 18)
print(x)
y = 'Hi, I\'m {1}, {0} now'.format('Jack', 18)
print(y)
# {}里可以直接使用变量指定读取
z = 'Hi, I\'m {name}, {age} now'.format(name='Jack', age=18)
print(z)

zz = 'Hi, I\'m {name}, {1} now, from {0}'.format('India', 29, name='Buddha')
print(zz)

d = ['Jack', 18, 'India', '180cm']
# dd = 'Hi, I\'m{}, {} now, from {}, and {} height'.format(d[0], d[1], d[2], d[3])
dd = 'Hi, I\'m {}, {} now, from {}, and {} height'.format(*d)
print(dd)

info = {'name': 'Jack', 'age': 23, 'addr': 'India', 'height': 190}
myinfo = 'Hi, I\'m {name}, {age} now, from {addr}, and {height}cm height'.format(**info)
print(myinfo)


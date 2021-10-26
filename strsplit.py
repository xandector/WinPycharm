# x = 'Jack,John,David,Ross,Mary,Joseph'
# x1 = x.split(',')
# print(x1)
# x11 = x.split(',', 2)   # 最大分割次数
# print(x11)
# x2 = x.rsplit(',')
# print(x2)
# x22 = x.rsplit(',',2)
# print(x22)
#
# print('abcdefXmpqrst'.partition('X'))
#
# print('abcdefXmpXqrst'.rpartition('X'))

# print('hello world.good morning\nyes'.capitalize())
#
# print('hello world'.upper())
#
# print('hello world'.title())

# # ljust(width, fillchar)
# print('Monday'.ljust(10,'+'))
# # ==> Monday++++
# # rjust(width, fillchar)
# print('Monday'.rjust(10,'-'))
# # ==> ----Monday
# # center(width, fillchar)
# print('Monday'.center(10,'*'))
# # ==> **Monday**

# 去掉字符串左边空格
print('    apple    '.lstrip())
# 去掉字符串右边空格
print('    apple    '.rstrip())
# 去掉字符串两边空格
print('    ap ple    '.strip())

print('++++apple++++'.lstrip('+'))

fruits = ['apple', 'banana', 'orange', 'peace']
print('-'.join(fruits))

print('*'.join('hello'))


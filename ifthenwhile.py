# if 5 > 6:
#     print('Big!')
# else:
#     print('Small')

# age = int(input('请输入年龄'))
# if age < 18:
#     print('未成年')
# else:
#     print('成年')

# 写出判断一个数能否同时被3和7整除
# element = int(input('请输入：'))
# if (element % 3 == 0) and (element % 7 == 0):
#     print('Yes')
# else:
#     print('No')

# #写出判断一个数能否被4或6整除，但不能同时被4和6整除
# element = int(input('Please type in:'))
# ele4 = element % 4
# ele6 = element % 6
# if ele4 == 0 or ele6 == 0:
#     if ele4 == 0 and ele6 == 0:
#         print('No')
#     else:
#         print('Yes')
# else:
#     print('No')

# #是否闰年
# year = int(input('Is it a leap year :'))
# y4 = year % 4
# y100 = year % 100
# y400 = year % 400
# if y4 == 0:
#     if y100 == 0:
#         if y400 == 0:
#             print('Yes')
#         else:
#             print('No')
#     else:
#      print('Yes')
# else:
#  print('No')

# #输入秒数，以xx时xx分xx秒表示
# sec = int(input('Type in seconds: '))
# hh = sec // 3600
# mm = (sec // 60) % 60
# ss = (sec % 3600) % 60
# if hh < 10:
#     hour = '0'+ str(hh)
# else:
#     hour = str(hh)
# if mm < 10:
#     minute = '0'+ str(mm)
# else:
#     minute = str(mm)
# if ss < 10:
#     second = '0' + str(ss)
# else:
#     second = str(ss)
# print(hour,':',minute,':',second)

# # 多个if语句，语句和语句之间不存在关联
# score = int(input('Please type in score:'))
# if 60 > score >= 0:
# 	print('D')
# if 80 > score >= 60:
#     print('C')
# if 90 > score >= 80:
#     print('B')
# if 100 >= score >= 90:
#     print('A')

# #此时可以elif
# score = int(input('Please type in score:'))
# if 60 > score >= 0:
#     print('D')
# elif 80 > score >= 60:
#     print('C')
# elif 90 > score >= 80:
#     print('B')
# elif 100 >= score >= 90:
#     print('A')
# else:
#     print('WTF?')

# #if语句嵌套（使用强制缩进表示语句之间结构）
# ticket = input('Have ticket？Y/N')
# if ticket == 'Y':
#     print('Ticket checked!')
#     safe = input('Security check? Y/N')
#     if safe == 'Y':
#         print('Securtiy passed!')
#     else:
#         print('Security not pass!')
# else:
#     print('No ticket!')

# #pass关键字，在python里没有意义，只是用来占位，保证语句完整性
# age = int(input('Type in age:'))
# if age > 18:
#     pass    #使用pass占位，保证if语句完整性
# print('Hello')

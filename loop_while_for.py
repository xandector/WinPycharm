# # while循环
#
# # while 判断条件：
# # 条件成立时执行的代码
# x = 100
# while x > 0:
#     print(x)
#     x -= 1

# # 1-100之和
# a = 0
# x = 0
# while a <= 100:
#     x += a
#     a += 1
# print('Sum 1 to 100 is', x)


# 1-100之和
x = 0
for a in range(1, 101):
    x += a
print('Sum 1 to 100 is', x)

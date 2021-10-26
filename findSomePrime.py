from defx_findMyPrimeNumber import findMyPrimeNumber

# # 连续判断输入数字是否为质数
# while True:
#     number = int(input('Please type in your number:'))
#     isprime = findMyPrimeNumber(number)
#     if isprime:
#         print('It\'s a PRIME！')
#     else:
#         print('It\'s not a prime.')

# 找出连续数字段落中的质数
cp1 = 0
cp2 = 100
for i in range(cp1, cp2):
    if findMyPrimeNumber(i):
        print(i, end=' ')

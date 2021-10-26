# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(str(j)+'x'+str(i)+'='+str(i*j), end='    ')
        j += 1
    print()
    i += 1

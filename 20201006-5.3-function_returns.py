def test(a, b):
    x = a // b
    y = a % b

    # 一般情况下一个函数最多只会执行一个return语句
    # 特殊情况下（finally语句）下，一个函数可能会执行多个return语句
    # return x    # return表示一个函数的结束
    # return y    # y将不会被返回

    # return [x, y]   # 列表形式返回
    # return {'x': x, 'y': y}   # 字典形式返回、
    return x, y  # 元组形式返回（可去掉括号）


result = test(13, 5)
print('商是{},余数是{}'.format(result[0], result[1]))  # 列表形式时用
# print('商是{},余数是{}'.format(result['x'], result['y']))  # 字典形式时用
# ==> 商是2,余数是3

shang, yushu = test(16, 3)
print('商是{},余数是{}'.format(shang, yushu))  # 分开赋值
# ==> 商是5,余数是1

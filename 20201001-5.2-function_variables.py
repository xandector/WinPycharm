a = 100  # 全局变量，在整个py文件里可访问
word = 'hello'


def test():
    x = 'hello'
    print('x = {}'.format(x))
    # 如果局部变量和全局变量同名，会在函数内部有定义一个新的局部变量
    a = 10  # 局部变量a
    print('函数内部 a = {}'.format(a))
    # 使用global声明变量，可以在函数内部修改全局变量
    global word
    word = 'ok'
    # 内置函数globals(),locals()可以查看全局变量和局部变量
    print('locals = {}, globals = {}'.format(locals(), globals()))


test()
# ==>x = hello
# ==> 函数内部 a = 100
# ==> locals = {'x': 'hello', 'a': 10}, globals = (...)

print('函数外部 a = {}'.format(a))
# ==> 函数外部 a = 100
print('函数外部 word = {}'.format(word))
# ==> 函数外部 word = ok

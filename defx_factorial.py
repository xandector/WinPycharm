def factorial(n):
    """
    求n的阶乘
    :param n: 阶乘的叔
    :return: n的阶乘结果
    """
    s = 1
    for i in range(1, n+1):
        s = s * i
    print('%d的阶乘为%d' % (n, s))
    return s


# factorial(9)

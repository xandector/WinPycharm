def sumNtoM(n: int, m: int):
    """
    求n~m之间所有整数之和
    :param n: 起始数，整数
    :param m: 终点数，整数
    :return: n到m（包括）间所有数之和
    """
    if n > m:
        n, m = m, n
    i = n
    s = 0
    while i <= m:
        s += i
        i += 1
    print('Sum between %d to %d is %d' % (n, m, s))
    return s


# sumNtoM(10, 5)

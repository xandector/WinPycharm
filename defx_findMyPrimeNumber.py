def findMyPrimeNumber(num):
    """
    获取整数，如果为质数返回True，否则返回False
    :param num: 输入数字（整数）
    :return: 是否为质数（True/False）
    """
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

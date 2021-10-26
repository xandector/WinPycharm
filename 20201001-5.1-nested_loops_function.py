# def test1():
#     print('test1 begins')
#     print('test1 ends')
#
#
# def test2():
#     print('test2 begins')
#     test1()
#     print('test2 ends')
#
#
# test2()
# # ==> test2 begins
# # ==> test1 begins
# # ==> test1 ends
# # ==> test2 ends

from defx_factorial import factorial


def sum_factorial_1_to_m(m):
    """
    计算m阶乘的和
    :param m: 输入数
    :return: 返回1到m的阶乘的和
    """
    s = 0
    for i in range(1, m + 1):
        s = s + factorial(i)
    print('1到%d之间阶乘之和为%d' % (m, s))
    return s


sum_factorial_1_to_m(10)

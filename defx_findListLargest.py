def findListLargest(mylist):
    """
    返回列表最大值的下标
    :param mylist: 数字列表
    :return: 最大值的下标
    """
    x = mylist[0]
    # listindex = 0
    for ml in mylist:
        if ml > x:
            x = ml
            listindex = mylist.index(x)
    return listindex


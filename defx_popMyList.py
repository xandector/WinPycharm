def popMyList(thelist, switch=0):
    """
    获取数字列表，进行冒泡排序（降序1,其他升序）
    :param thelist: 获取数字列表
    :param switch: 1为降序，其他输入为升序（默认0）
    """
    ii = 0
    count = 0
    if switch == 1:
        while ii < len(thelist):
            flag = True
            i = 0
            while i < len(thelist) - 1 - ii:
                count += 1
                if thelist[i] < thelist[i + 1]:
                    flag = False
                    thelist[i], thelist[i + 1] = thelist[i + 1], thelist[i]
                i += 1
            ii += 1
            if flag:
                break
    else:
        while ii < len(thelist):
            i = 0
            flag = True
            while i < len(thelist) - 1 - ii:
                count += 1
                if thelist[i] > thelist[i + 1]:
                    flag = False
                    thelist[i], thelist[i + 1] = thelist[i + 1], thelist[i]
                i += 1
            ii += 1
            if flag:
                break
    print(count)

# numbers = [4, 12, 21, 5, 2, 1, 6, 124, 24]
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(numbers)
# popMyList(numbers)
# print(numbers)
# # popUpList(numbers, 0)
# # print(numbers)

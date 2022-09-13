def find_mid(a: list, b: list):
    """
    题目：两个已经排序的数组，找到他们组成一个新数组的中位数，要求不能将两个数组拼接
    思路：双指针
          1. 获取两个数组的长度和；找到中位数的索引位置idx；
          2. 使用变量i记录数组1的索引值，使用变量j记录数组b的索引值，使用变量count记录所有的索引计数；
          3. 当count与idx相等的时候程序终止，当前值即为中位数，但此时又有三种情况：
               a. 数组1遍历完，2没完，但没有找到中位数，需要在数组2中继续寻找；
               b. 数组2遍历完，1没完，但没有找到中位数，需要在数字1中继续寻找；
               c. 数组1和数组2都没有遍历完的情况下找到了中位数。
    :param a: 数组1
    :param b: 数组2
    :return: mid
    """
    la = len(a)
    lb = len(b)
    total_len = la + lb
    idx = total_len // 2

    count = 0
    i = 0
    j = 0
    while True:
        if a[i] < b[j]:
            count += 1
            i += 1
        else:
            count += 1
            j += 1
        if count - 1 == idx:
            print(a[i])
            break

        if i == la - 1:
            count += 1
            j += 1
            if count == idx:
                if total_len % 2 == 0:
                    print((b[j] + b[j + 1]) / 2)
                else:
                    print(b[j])
                break
        elif j == lb - 1:
            count += 1
            i += 1
            if count == idx:
                print(a[i])
                break


if __name__ == '__main__':
    # find_mid([1, 2, 3], [4])  # 1 2 3 4
    # find_mid([1, 2, 2], [4])  # 1 2 2 3
    # find_mid([3, 4, 5], [1, 4, 6, 9, 11])  # 1 3 4 4 5 6 9 11
    # find_mid([3, 4, 5], [1, 6])  # 1 3 4 5 6
    find_mid([3, 4], [1, 2, 6, 7])  # 1 2 3 4 6 7
    find_mid([1, 2], [2, 3, 6, 7])  # 1 2 2 3  6 7

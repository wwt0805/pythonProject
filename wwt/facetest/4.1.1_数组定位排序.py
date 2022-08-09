'''
给定一个数组A以及下标i,将数组元素进行调整，使得所有比A[i]小的元素排在前面，接着是所有等于A[i]的元素，最后排列的是比A[i]大的元素
'''


def range_idx(content: list(), idx: int):
    '''
    思路：双指针。
    1.起始位置指针start， 末尾指针end；
    2.如果start元素小于等于对比值，start后移一位；否则当前两个元素位置调换，end前移一位；
    3.当start与end相遇，返回当前列表结果
    4.对于当前列表结果找到分割点，大于等于分割数据的部分再进行排序，最终与前半部分合并即为最终结果
    :param content: 输入的int型列表
    :param idx: 输入的int型索引
    :return: 排序后的列表
    '''
    start = 0
    end = len(content) - 1
    num = content[idx]
    print(num)
    while start <= end:
        if content[start] < num:
            start += 1
        else:
            content[start], content[end] = content[end], content[start]
            end -= 1
    right = content[content.index(num)::]
    left = content[0:content.index(num)]
    print(content)
    print("left:", left)
    print("right", right)
    begin = 0
    dead = len(right) - 1

    num2 = right[0]
    while begin <= dead:
        if right[begin] <= num2:
            begin += 1
        else:
            right[begin], right[dead] = right[dead], right[begin]
            dead -= 1
    print(left + right)


if __name__ == '__main__':
    range_idx([6, 5, 5, 7, 9, 4, 3, 3, 4, 6, 8, 4, 7, 9, 2, 1], 5)

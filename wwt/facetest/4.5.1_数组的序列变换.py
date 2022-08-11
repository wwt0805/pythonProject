'''
给定数组A={1，2，3，4，5，6}，并将一个变化序列P={3,1,5,4,0,2},将变化序列应用到数组A上，得到新的数组B={A[3],A[1],A[5],A[4],A[0],
A[2]} = {4, 2, 6, 5, 1, 3}
'''


def transform(origin: list, alter: list):
    '''

    :param origin: 输入集合
    :param alter: 索引集合
    :return: 输入对应索引的集合
    '''
    print([origin[x] for x in alter])


if __name__ == '__main__':
    # transform({1, 2, 3, 4, 5, 6}, {3, 1, 5, 4, 0, 2})
    transform([1, 2, 3, 4, 5, 6], [3, 1, 5, 4, 0, 2])

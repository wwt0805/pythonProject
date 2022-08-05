'''
            近些年来，我国防沙治沙取得显著成果。某沙漠新种植N棵胡杨（编号1-N），排成一排。一个月后，有M棵胡杨未能成活。现可补种胡杨K棵，请问如何补种（只能补种，不能新种），可以得到最多的连续胡杨树？
            输入描述:
            N 总种植数量 1<=N<=100000 M 未成活胡杨数量 1<=M<=N M 个空格分隔的数，按编号从小到大排列 K 最多可以补种的数量 0<=K<=M
            输出描述:
            最多的连续胡杨棵树
            示例1
            输入
            5
            2
            2 4
            1
            输出
            3
            说明 补种到2或4结果一样，最多的连续胡杨棵树都是3
            示例2
            输入
            10
            3
            2 4 7
            1
            输出
            6
            说明 补种第7棵树，最多的连续胡杨棵树为6(5,6,7,8,9,10)
'''


def func():
    '''
    思路：
    1. 构建长度等于种树长度全部为1的列表，将死的树标记为0， [1，0，1，0，1，1，0，1，1，1]
    2. 以0对1进行分割[1] [1] [1,1], [1,1,1]
    3. 以补树的值进行合并同时记录合并后的长度，比如补1棵树，就一次选两组(以2为例：[1][1], [1][1,1,1], [1,1][1,1,1]),明显最后一组两个元素合并之后长度是5，
       外加补树的数量1，就是最终数量
    :return:
    '''
    plant_num = int(input())
    dead_num = int(input())
    dead_index = list(map(int, input().split(" ")))
    add_num = int(input())

    plant_index = [1] * plant_num
    for i in dead_index:
        plant_index[i - 1] = 0
    trans = "".join(str(x) for x in plant_index).split('0')
    res = {}
    for i in range(len(trans)):
        res[i] = len("".join([x for x in trans[i: i + add_num + 1]]))
    print(max(res.values()) + add_num)


if __name__ == '__main__':
    func()

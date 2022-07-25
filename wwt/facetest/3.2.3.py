def fixBinaryString(val, setlen):
    '''
    必须保持val的二进制长度和集合长度一致，例如，如果集合有3个元素，val=2, 那么它的二进制形式是0b11
    函数再高位补0，于是0b11转换为0b011,这样打印出来的元素才能根据二进制位对应上每一个元素
    '''
    binary = bin(val).replace("0b", "")
    while len(binary) < setlen:
        binary = "0" + binary
    return binary


def printSetByBinary(val, collection):
    '''
    根据整数二进制形势中比特位上的值是0还是1选择是否把对应元素打印到子集中
    '''
    # 先把整形对应的二进制位数根据集合元素个数补全
    binary = fixBinaryString(val, len(collection))
    idx = 0
    isNull = True
    while idx < len(binary):
        if binary[idx] == '1':
            if isNull is False:
                print(",", end='')
            print(collection[idx], end='')
            isNull = False
        idx += 1
    if isNull is True:
        print("NULL")
    print(";")


def handleAllSubset(set):
    count = len(set)
    val = 0
    # 根据集合中元素的个数构造相应长度的二进制数，并把所有的比特位都设置位1
    for i in range(count):
        val |= (1 << i)
    while val >= 0:
        printSetByBinary(val, set)
        val -= 1


if __name__ == '__main__':
    collection = ["A", "B", "C", "D"]
    handleAllSubset(collection)

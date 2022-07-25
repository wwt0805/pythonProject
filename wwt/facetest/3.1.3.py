"""
对于64位或32位无符号整形数x,我们再他的二进制表示中，把1的个数成为x的权重，例如x=7，他的二进制位0b111，由于有3个1，因此x的权重就是3。
用S(k)表示64或32位无符号整形数中，权重是k的所有整数的集合，其中k不等于0，64，32。给定一个整形数x，如果他属于集合S(k)，要求找到拎一个
属于S(k)的整数y，是的|x-y|的值最小。
"""


def closeWithTheSameWeight(x):
    for i in range(0, 64):
        if ((x >> i) & 1) ^ ((x >> (i + 1)) & 1):
            x ^= (1 << i) | (1 << (i + 1))
            return x


x = 0b11011
y = closeWithTheSameWeight(x)
print('integer closest to x with the same weight is {}'.format(bin(y)))

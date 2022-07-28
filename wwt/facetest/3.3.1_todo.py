'''
两个整数x、y，它们的最大公约数d必须满足d|x, 而且d|y。其中，符号“|”表示整除，d|x表示x是d的倍数。要求设计一个算法来计算最大公约数，
算法不能使用乘除和求余
'''


# 如果可以使用乘除和求余
# 解法1：分别求a、b的公约数，再求最大公约数
def gcd1(a, b):
    cd_a = []
    cd_b = []
    max_cd = 0
    for i in range(1, a + 1):
        if a % i == 0:
            cd_a.append(i)
    for j in range(1, b + 1):
        if b % j == 0:
            cd_b.append(j)
    for k in cd_a:
        if k in cd_b and k > max_cd:
            max_cd = k
    print(max_cd)


# 解法2：对解法1进行改进，a、b的最大公约数不会大于最小的那个数，所以加入大小判断
def gcd2(a, b):
    max_num = max(a, b)
    min_num = min(a, b)
    max_cd = 0
    for i in range(1, min_num + 1):
        if max_num % i == 0 and min_num % i == 0 and i > max_cd:
            max_cd = i
    print(max_cd)


# 解法3：递归。如果a能整除b最大公约数就是b，如果不能递归计算b对(a%b)取余
def gcd3(a, b):
    if a % b == 0:
        print(b)
    else:
        gcd3(b, a % b)


if __name__ == '__main__':
    # gcd1(100, 10)
    # gcd2(100, 10)
    gcd3(100, 11)

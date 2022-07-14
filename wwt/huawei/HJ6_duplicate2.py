import math
def hj_6():
    num = int(input())
    prime_list = []
    factor_list = []
    res_list = []
    res1_list = []

    prime_factor_list = []
    #  因数列表
    for i in range(2, num):
        if num % i == 0:
            # factor_list.append(i)
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    break
            else:
                prime_factor_list.append(i)
    if len(prime_factor_list) != 0:
        i = 0
        while True:
            an = prime_factor_list[i]
            if num % an == 0 and an != 1:
                remain = num / an
                res1_list.append(an)
                if remain == 1:
                    break
                else:
                    num = remain
            else:
                i += 1
        res1_list.sort()
    else:
        res1_list = [num]
    for i in res1_list:
        print(i, end=" ")


if __name__ == '__main__':
    hj_6()

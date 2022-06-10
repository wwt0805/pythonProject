def hj_6():
    num = int(input())
    factor_list = []
    result_list = []
    for i in range(1, num + 1):  # 求因数
        if num % i == 0:
            factor_list.append(i)
    print(factor_list)

    for i in factor_list:
        # if i == 1:
        #     result_list.append(i)
        #     result_list.append(factor_list[-1])
        # else:
        for j in range(1, i):
            if i % j == 0:
                result_list.append(i)
                break

    print(result_list)


if __name__ == '__main__':
    hj_6()

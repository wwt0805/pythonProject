def hj_76():
    num = int(input())
    pow_num = pow(num, 3)
    mid_num = pow(num, 2)
    store_list = []
    start_num = mid_num - (num - 1) / 2 * 2
    store_list.append(str(int(start_num)))
    for i in range(1, num):
        sum_num = start_num + 2 * i
        store_list.append(str(int(sum_num)))
    print("+".join(store_list))



if __name__ == '__main__':
    hj_76()

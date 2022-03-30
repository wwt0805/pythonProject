store_list = []


def hj_62(data):
    while True:
        num = data // 2
        if num != 0:
            store_list.append(data % 2)
            hj_62(num)
        else:
            store_list.append(data % 2)
        break
    return store_list


if __name__ == '__main__':
    data = input()
    a = hj_62(int(data))
    count = 0
    for _ in store_list:
        if _ == 1:
            count += 1
    print(count)

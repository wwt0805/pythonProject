def hj_199():
    store_list = []
    num = input()
    for i in range(int(num) + 1):
        if str(int(i) ** 2)[-len(str(i)):] == str(i):
            store_list.append(i)
    # print(store_list)
    print(len(store_list))


if __name__ == '__main__':
    hj_199()

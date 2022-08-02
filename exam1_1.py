def exam1(mp, hp):
    my_list = list(str(x) for x in mp.split("-"))
    history_list = list(str(x) for x in hp.split("-"))
    current_list = my_list + history_list
    full_list = [str(x) for x in range(3, 15)] * 4
    for i in current_list:
        if i == "J":
            i = "11"
        elif i == "Q":
            i = "12"
        elif i == "K":
            i = "13"
        elif i == "A":
            i = "14"
        if i in full_list:
            full_list.remove(i)
    res_list = [int(x) for x in set(full_list)]
    res_list.sort()
    print(res_list)

    tmp_list = list()
    longest_list = []
    i = 0
    while i <= len(res_list) - 2:
        j = i + 1
        if res_list[i] + 1 == res_list[j]:
            tmp_list.append(res_list[i])
        if res_list[i] + 1 != res_list[j] or j == len(res_list) - 1:
            longest_list.append(tmp_list)
            tmp_list = res_list[j]
        i += 1
    print(longest_list)


if __name__ == '__main__':
    exam1("3-3-3-3-4-4-5-5-6-6-7-8-9-10-J-Q-K-A", "4-5-6-7-8-8-8")
    # print(exam1("3-3-3-3-4-4-5-5-6-7-8-9-10-J-Q-K-A", "4-5-6-7-8-8"))
    # print(exam1("7-7-7-7", "Q-Q-Q-Q"))

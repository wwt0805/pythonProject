def hj_16():
    N, m = map(int, input().strip().split())
    v_lst = []
    p_lst = []
    q_lst = []
    for i in range(m):
        v, p, q = map(int, input().strip().split())
        v_lst.append(v)
        p_lst.append(p)
        q_lst.append(q)
    # print("v: ", v_lst)
    # print("p: ", p_lst)
    # print("q: ", q_lst)
    new_list = []
    for _ in range(len(q_lst)):
        if q_lst[_] != 0:
            # print(q_lst[_])
            if len(new_list) == 0:
                new_list.append(
                    [v_lst[q_lst[_] - 1], p_lst[q_lst[_] - 1], q_lst[_], p_lst[q_lst[_] - 1] / v_lst[q_lst[_] - 1]])
            new_list.append([v_lst[_], p_lst[_], q_lst[_], p_lst[_] / v_lst[_]])
        else:
            new_list.append([v_lst[_], p_lst[_], q_lst[_], p_lst[_] / v_lst[_]])
    print(new_list)
    new_list.sort(key=lambda x: x[-1], reverse=True)
    print(new_list)


if __name__ == '__main__':
    hj_16()

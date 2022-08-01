"""
coding=utf-8
@Author  : Wu Wentong
@Time    : 2022/7/31 9:25 上午
@Site    : 
@File    : normal.py
@Software: PyCharm
"""


def exam1():
    mp = input()
    hp = input()
    p = {}
    p_neg = {}
    n1 = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', "Q", "K", "A"]
    n2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    for i in range(len(n1)):
        p[n1[i]] = n2[i]
        p_neg[n2[i]] = n1[i]

    mp = [p.get(x) for x in str(mp).split("-")]  # 我的手牌
    hp = [p.get(x) for x in str(hp).split("-")]  # 对手的手牌
    full = [x for x in range(3, 15)] * 4         # 全部牌
    # print("mp:", mp)
    # print("hp:", hp)
    # print(full)
    print(mp + hp)
    fouth_element = []
    count_3 = (mp + hp).count(3)
    count_4 = (mp + hp).count(4)
    count_5 = (mp + hp).count(5)
    count_6 = (mp + hp).count(6)
    count_7 = (mp + hp).count(7)
    count_8 = (mp + hp).count(8)
    count_9 = (mp + hp).count(9)
    count_10 = (mp + hp).count(10)
    count_11 = (mp + hp).count(11)
    count_12 = (mp + hp).count(12)
    count_13 = (mp + hp).count(13)
    count_14 = (mp + hp).count(14)
    count_list = [count_3, count_4, count_5, count_6, count_7, count_8, count_9, count_10,
                  count_11, count_12, count_13, count_14]
    for i in count_list:
        if i == 4:
            print(count_list.index(i))




    for i in mp + hp:        
        if full.index(i):
            full.remove(i)
    re_p = list(set(full))
    re_p.sort()

    res = []
    res1 = []
    for i in range(len(re_p) - 1):
        res.append(re_p[i])
        for j in range(i + 1, len(re_p)):
            if re_p[j] - re_p[j - 1] == 1:
                res.append(re_p[j])
            else:
                break
        if len(res) > len(res1):
            res1 = res[:]
        res.clear()
    if len(res1) != 0:
        return "-".join([p_neg[x] for x in res1])
    else:
        return "NO-CHAIN"


if __name__ == '__main__':
    print(exam1())

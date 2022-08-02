"""
coding=utf-8
@Author  : Wu Wentong
@Time    : 2022/7/31 9:25 上午
@Site    :
            提交:4次 得分:66.67/100.0
            标题:最长的顺子|时间限制:1秒|内存限制:262144K|语言限制:不限【最长的顺子】
            斗地主起源于湖北十堰房县，据传是一位叫吴修全的年轻人根据当地流行的扑克玩法“跑得快”改编的，如今已风靡整个中国，并流行于互联网上。牌型:
            单顺又称顺子，最少5张牌，最多12张牌(3…A)，不能有2，也不能有大小王，不计花色例如:3-4-5-6-7-87-8-9-10-J-Q3-4-5-6-7-8-9-10-J-Q-K-A
            可用的牌3<4<5<6<7<8<9<10<J<Q<K<A<2<B(小王)<C(大王)，每种牌除大小王外有4种花色(共有13X4+2张牌)输入1手上已有的牌2已经出过的牌(包括对手出的和自己出的牌)
            输出:对手可能构成的最长的顺子(如果有相同长度的顺子，输出牌面最大的那一个)，如果无法构成顺子，则输出NO-CHAIN输入描述:
            输入的第一行为当前手中的牌输入的第二行为已经出过的牌
            输出描述:
            最长的顺子
            示例1:输入
            3-3-3-3-4-4-5-5-6-7-8-9-10-Q-K-A
            4-5-6-7-8-8-8
            输出
            9-10-1-Q-K-A
@File    : exam1.py
@Software: PyCharm
"""


def exam1(mp, hp):
    '''
    思路很简单，构建整副牌的列表full，在构建我和历史手牌的列表mp+hp，剩下的牌则位full-(mp+hp),再利用集合的元素排他性将相减后的列表转
    化为集合
    :param mp: 表示自己手中的牌
    :param hp: 表示历史打出的牌
    :return: 返回最大顺子
    '''
    # mp = input()
    # hp = input()
    p = {}  # 牌到数字{'3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    p_neg = {}  # 数字到牌 {3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
    n1 = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', "Q", "K", "A"]
    n2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    for i in range(len(n1)):
        p[n1[i]] = n2[i]
        p_neg[n2[i]] = n1[i]

    # print(p)
    # print(p_neg)
    mp = [p.get(x) for x in str(mp).split("-")]  # 我的手牌 通过牌到数字取出
    hp = [p.get(x) for x in str(hp).split("-")]  # 对手的手牌
    full = [x for x in range(3, 15)] * 4  # 全部牌
    # print("mp:", mp)
    # print("hp:", hp)
    # print("full:",full)  # [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    # print("=" * 50)
    # print("mp + hp:", mp + hp)
    # print("=" * 50)
    for i in mp + hp:  # [3, 3, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 4, 5, 6, 7, 8, 8, 8]
        # print(i)
        # if full.index(i):
        if i in full:
            full.remove(i)
            # print(full)
    re_p = list(set(full))  # 利用set的元素唯一性去重复
    re_p.sort()
    # print("re_p:", re_p)
    # print("=" * 50)

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
    if len(res1) >= 5:
        return "-".join([p_neg[x] for x in res1])
    else:
        return "NO-CHAIN"


if __name__ == '__main__':
    print(exam1("3-3-3-3-4-4-5-5-6-7-8-9-10-J-Q-K-A", "4-5-6-7-8-8-8"))
    print(exam1("3-3-3-3-4-4-5-5-6-7-8-9-10-J-Q-K-A", "4-5-6-7-8-8"))
    print(exam1("7-7-7-7", "Q-Q-Q-Q"))

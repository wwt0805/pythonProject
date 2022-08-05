'''
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
'''


def func(mp, hp):
    '''
    思路：
    1. 构建我的手牌和历史牌的列表current_list，构建整个牌的列表full_list
    2. 将current_list中的每个元素在full_list中寻找，如果存在就在full_list中移除。以此类推最终得到的就是对手的手牌, 利用集合的元素
       唯一性将对手手牌集合去重再按顺序排列
    3. 在对手的手牌中寻找出最大的连续牌即可
    :param mp: 我手上的牌
    :param hp: 已经打出的牌
    :return: 可能存在的最大顺自
    '''
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
    # print(res_list)

    tmp_list = []
    result_list = []
    for i in range(len(res_list)):
        if len(tmp_list) == 0:
            tmp_list.append(res_list[i])
        else:
            if res_list[i] == tmp_list[-1] + 1:
                tmp_list.append(res_list[i])
                if i == len(res_list) - 1:
                    result_list.append(tmp_list)
            else:
                result_list.append(tmp_list.copy())
                tmp_list.clear()
    result_list.sort(key=lambda x: len(x))
    if len(result_list[-1]) >= 5:
        a = ("-".join(str(x) for x in result_list[-1])).replace("11", "J").replace("12", "Q").replace("13",
                                                                                                      "K").replace("14",
                                                                                                                   "A")
        print(a)
    else:
        print("NO-CHAIN")


if __name__ == '__main__':
    # func("3-3-3-3-4-4-5-5-6-7-8-9-10-J-Q-K-A", "4-5-6-7-8-8-8")
    # func("3-3-3-3-4-4-5-5-6-7-8-9-10-J-Q-K-A", "4-5-6-7-8-8")
    # func("7-7-7-7", "Q-Q-Q-Q")
    func("8-8-8-8", "Q-Q-Q-Q")

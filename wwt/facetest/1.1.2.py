def findmaxprofit(S):
    # 返回值格式
    if len(S) < 2:
        return [0, 0, 0]
    if len(S) == 2:
        # 如果交易只有两天，就只能第一天买入第二天卖出
        if S[1] > S[0]:
            return [0, 1, S[1] - S[0]]
        else:
            return [0, 0, 0]
    # 把交易数据分成两部分，分别找出前半部分和后半部分最大交易利润，然后选取两种结果的最大值
    first_half = findmaxprofit(S[0: int(len(S) / 2)])
    second_half = findmaxprofit(S[int(len(S) / 2): len(S)])
    finalresult = first_half

    if (second_half[2] > first_half[2]):
        second_half[0] += int(len(S) / 2)
        second_half[1] += int(len(S) / 2)
        finalresult = second_half

    lowestprice = S[0]
    highestprice = S[int(len(S) / 2)]
    buyDay = 0
    selDay = int(len(S) / 2)
    for i in range(0, int(len(S) / 2)):
        if (S[i] < lowestprice):
            buyDay = i
            lowestprice = S[i]
    for i in range(int(len(S) / 2), len(S)):
        if (S[i] > highestprice):
            selDay = i
            highestprice = S[i]

    if (highestprice - lowestprice > finalresult[2]):
        finalresult[0] = buyDay
        finalresult[1] = selDay
        finalresult[2] = highestprice - lowestprice

    return finalresult


S = [1, 2, 9, 4, 5, 6, 7, 10]
maxprofit = findmaxprofit(S)
print("{}day buy in ; {}day sell out; maxprofile is {}".format(maxprofit[0] + 1, maxprofit[1] + 1, maxprofit[2]))

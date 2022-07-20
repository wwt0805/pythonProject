'''
暴力法
'''
# S定义股票开盘价格数组
S = [10, 4, 8, 7, 9, 6, 2, 5, 3]
maxProfile = 0
buyDay = 0
sellDay = 0
for i in range(len(S) - 1):
    for j in range(i + 1, len(S)):
        if S[j] - S[i] > maxProfile:
            maxProfile = S[j] - S[i]
            buyDay = i
            sellDay = j
print("{}day buy in ; {}day sell out; maxprofile is {}".format(buyDay + 1, sellDay + 1, maxProfile))



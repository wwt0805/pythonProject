S = [1, 2, 9, 4, 5, 6, 7, 10]
minprice = S[0]
N = 0
profit = 0
selday = 0
buyday = 0

for N in range(len(S)):
    if S[N] < minprice:
        minprice = S[N]
        buyday = N

    if S[N] - minprice > profit:
        profit = S[N] - minprice
        selday = N

print("{}day buy in ; {}day sell out; maxprofile is {}".format(buyday + 1, selday + 1, profit))

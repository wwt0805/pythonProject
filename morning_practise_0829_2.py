class FindMedian:
    def __init__(self, a: list, b: list):
        self.a = a
        self.b = b
        self.la = len(self.a)
        self.lb = len(self.b)
        self.length = self.la + self.lb
        self.mid_idx = self.cal_mid()

    def charge_odds(self):
        if self.length % 2 == 0:
            return True
        else:
            return False

    def cal_mid(self):
        if self.charge_odds():
            return self.length // 2 - 1
        else:
            return self.length // 2

    def search_mid(self):
        count = 0
        idx_a = 0
        idx_b = 0
        flag = ""
        while True:
            if self.a[idx_a] <= self.b[idx_b]:
                idx_a += 1
                count += 1
                flag = "a"
            else:
                idx_b += 1
                count += 1
                flag = "b"

            if count == self.mid_idx:
                if flag == "a":
                    print(self.a[idx_a])
                    break
                elif flag == "b":
                    print(self.b[idx_b])
                    break

            if idx_a == self.la - 1:
                idx_b += 1
                count += 1
                if count == self.mid_idx:
                    pass

            elif idx_b == self.lb - 1:
                idx_a += 1
                count += 1
                if count == self.mid_idx:
                    pass


if __name__ == '__main__':
    f = FindMedian([1, 3, 5], [4])
    f = FindMedian([1, 3, 5], [6, 7])
    f = FindMedian([1, 3, 5], [6])
    f = FindMedian([1, 3, 5], [2, 2, 6])
    f = FindMedian([1, 3, 5], [2, 4, 6, 7])  # 1 2 3 4 5 6 7 ~~~ 4
    f = FindMedian([1, 2, 3], [3, 4, 5])  # 1 2 3 3 4 5  ~~~ 3

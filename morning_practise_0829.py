import numpy as np


class RotationMatrix:
    def __init__(self, num):
        self.num = num
        self.matrix = np.arange(1, self.num ** 2 + 1).reshape(self.num, self.num)
        self.top = 0
        self.right = self.num - 1
        self.bottom = self.num - 1
        self.left = 0

    def rotation(self):
        print(self.matrix)
        while self.top <= self.bottom and self.left <= self.right:
            for i in range(self.left, self.right + 1):
                print(self.matrix[self.top][i], end="")
            for i in range(self.top + 1, self.bottom + 1):
                print(self.matrix[i][self.right], end="")
            for i in range(self.right - 1, self.left - 1, -1):
                print(self.matrix[self.bottom][i], end="")
            for i in range(self.bottom - 1, self.top, -1):
                print(self.matrix[i][self.left], end="")

            self.top += 1
            self.right -= 1
            self.bottom -= 1
            self.left += 1


if __name__ == '__main__':
    r = RotationMatrix(3)
    r.rotation()

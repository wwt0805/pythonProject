import numpy as np


class Rotation:
    def __init__(self, size: int):
        self.size = size
        self.matrix = np.arange(1, self.size ** 2 + 1).reshape(self.size, self.size)
        self.top = 0
        self.right = self.size - 1
        self.bottom = self.size - 1
        self.left = 0

    def output(self):
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
    r = Rotation(3)
    r.output()

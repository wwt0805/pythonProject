'''
给定两个坐标轴对齐的矩形，判断他们是否相交，如果是，给出他们所形成的矩形面积
'''


class Retangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def charge_interact(self, other):
        if self.x + self.width > other.x > self.x:
            if self.y + self.height >= other.y > self.y:
                print("True")
            elif self.y + self.height >= other.y + other.height > self.y:
                print('True')

        elif self.x + self.width > other.x + other.width > self.x:
            if self.y + self.height >= other.y > self.y:
                print("True")
            elif self.y + self.height >= other.y + other.height > self.y:
                print("True")


if __name__ == '__main__':
    A = Retangle(1, 1, 4, 2)
    B = Retangle(2, 2, 3, 3)
    A.charge_interact(B)

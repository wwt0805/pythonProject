'''
给定一个数组A以及下标i,将数组元素进行调整，使得所有比A[i]小的元素排在前面，接着是所有等于A[i]的元素，最后排列的是比A[i]大的元素
'''


def rangeidx(content, idx):
    num = content[idx]
    for i in range(len(content)):
        if content[i] < num:
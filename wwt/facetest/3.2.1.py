'''
有一个集合S，要求打印出他的所有子集，子集元素用逗号隔开，假设集合S的内容位S={"A", "B", "C"},那么该集合的所有子集分别位"A,B,C","A,B",
"A,C","B,C","A""B""C"和“NULL”。其中S本身和空集都可以认为是S的子集
'''


def findpartstring(setstring):
    # 将集合内容转化为字符串
    convert_string = "".join((str(x) for x in setstring))
    print(convert_string)
    # 计算当前长度可以表示的最大的二级制数
    bin_num = "0b" + "1" * (len(setstring))
    num = int(bin_num, 2)

    for i in range(1, num + 1):
        # 获取转化位二进制表示0b之后的数值
        tmp_str = str(bin(i))[2:]
        # 如果tmp_str的长度小于输入集合长度，说明需要补0才能使得所有数据长度一样
        if len(tmp_str) <= (len(setstring) - 1):
            full_tmp_str = "0" * (len(setstring) - len(tmp_str)) + tmp_str
        else:
            full_tmp_str = tmp_str
        # print(full_tmp_str)

    # 遍历full_tmp_str，其中为1的就表示集合中对应位置的元素
        res = ""
        res_list = []
        for i in range(len(full_tmp_str)):
            if full_tmp_str[i] == '1':
                res += convert_string[i]
                res_list.append(res)
        print(res_list)
        print([""])


if __name__ == '__main__':
    findpartstring({"A", "B", "C", "D"})

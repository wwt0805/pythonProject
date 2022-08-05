def func(content):
    '''
        要点：1.括号匹配用进栈和出栈完成；2.注意观察'['前一定都是数字
        思路：1.从后到前将非数字进栈；
         2.如果当前为数字，出栈；并即将当前数字使用变量记录
         3.因为最前入栈一定是']'，所以判断出栈的终止条件即为当前栈顶是否为“]”,如果“是”则停止；如果“否”则说明其内容为报文部分
         4.当3结束后，去除当前栈顶，再将重复次数与报文内容相乘，并用变量做累加，并将结果重新压入栈中
         5.因为是从后向前入栈所以将表示栈的列表取反，调整元素顺序，再join为字符串即为最终结果
    :param content: 输入字符串内容
    :return: 解压后的文件字符串
    '''
    content = input()  # 输入报文
    tmp_list = []
    l = len(content)
    endline = l - 1
    while endline >= 0:  # 从后向前读取字符串
        if not content[endline].isdigit():  # 如果索引取得不是数字
            tmp_list.append(content[endline])  # 压入栈
            endline -= 1
        else:  # 如果是数字
            num = ''  # 用于记录栈前数字
            res = ''  # 用于记录栈内报文内容
            while endline >= 0 and content[endline].isdigit():
                num = content[endline] + num
                endline -= 1
            while tmp_list[-1] != ']':
                ls = tmp_list.pop()
                if ls != "[":
                    res += ls
            tmp_list.pop()  # 括号匹配对完成，删除当前栈顶即"]"
            res = int(num) * res
            tmp_list.append(res)
    tmp_list.reverse()
    print("".join([x for x in tmp_list if x not in "[]"]))


if __name__ == '__main__':
    func("2[w]5[ls]")  # ]ls[5 ]w[2
    func("7[s]66[as3[i2[cd]]]")  # ]]]dc[2i [3sa[66 ]s[7
    #    kkkkkkkkkkmnjopopjopopjopopmnjopopjopopjopop

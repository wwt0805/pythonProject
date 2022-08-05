'''
            标题:解压报文|时间限制:1秒|内存限制:262144K|语言限制:不限【解压报文】
            为了提升数据传输的效率，会对传输的报文进行压缩处理。输入一个压缩后的报文，请返回它解压后的原始报文。
            压缩规则:nfstr1表示方括号内部的str正好重复n次。注意n为正整数(0<n<=100)，str只包含小写英文字母，不考虑异常情况
            输入描述:
            输入压缩后的报文:
            1)不考虑无效的输入，报文没有额外的空格，方括号总是符合格式要求的:
            2)原始报文不包含数字，所有的数字只表示重复的次数n，例如不会出现像5b或3[8]的输入;
            输出描述:
            解压后的原始报文注:
            1)原始报文长度不会超过1000，不考虑异常的情况
            示例1:输入
            3[k]2[mn]
            输出
            kkkmmn
'''


def exam(content):
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
    tmp_list = []
    l = len(content)
    endline = l - 1  # 最后一位索引位置
    while endline >= 0:  # 从后向前读取字符串
        if not content[endline].isdigit():  # 如果索引取得不是数字
            tmp_list.append(content[endline])  # 压入栈
            endline -= 1
        else:  # 如果是数字
            num = ''
            res = ''
            while endline >= 0 and content[endline].isdigit():
            # while endline >= 0 :
                num = content[endline] + num
                endline -= 1
            while tmp_list[-1] != ']':
                ls = tmp_list.pop()
                if ls != "[":
                    res += ls
            tmp_list.pop()  # 移除匹配的']'，即当前栈顶
            res = int(num) * res
            tmp_list.append(res)
    tmp_list.reverse()
    print("".join([x for x in tmp_list if x not in "[]"]))


if __name__ == '__main__':
    exam("2[w]5[ls]")  # ]ls[5 ]w[2
    # exam("7[s]66[as3[i2[cd]]]")  # ]]]dc[2i [3sa[66 ]s[7

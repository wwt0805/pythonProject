"""
coding=utf-8
@Author  : Wu Wentong
@Time    : 2022/7/31 10:44 上午
@Site    :
            提交:2次 得分:200.0/200.0
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
@File    : test3_1.py
@Software: PyCharm
"""


def exam3():
    content = input()   #  输入报文
    tmp_list = []
    l = len(content)
    endline = l - 1
    while endline >= 0:  # 从后向前读取字符串
        if not content[endline].isdigit():  # 如果索引取得不是数字
            tmp_list.append(content[endline]) # 压入栈
            endline -= 1
        else:  # 如果是数字
            num = ''
            res = ''
            while endline >= 0 and content[endline].isdigit():
                num = content[endline] + num
                endline -= 1
            while tmp_list[-1] != ']':
                ls = tmp_list.pop()
                if ls != "[":
                    res += ls
            tmp_list.pop()
            res = int(num) * res
            tmp_list.append(res)
    tmp_list.reverse()
    print("".join([x for x in tmp_list if x not in "[]"]))


if __name__ == '__main__':
    exam3()

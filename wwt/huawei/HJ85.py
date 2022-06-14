def hj_85():
    tem = []
    content = input()
    for i in content:
        if len(tem) == 0:
            tem.append(i)
        else:
            while True:
                if i == tem[-1]:
                    tem.pop()
                    continue

                else:
                    tem.append(i)

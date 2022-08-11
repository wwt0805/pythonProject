'''
A是含有n个元素的数组，如果可以申请到足够大内存，那么把A从位置i开始旋转是比较简单的。比如A：a,b,c,d,e,i=3，旋转后字符串A为：d,e,a,b,c。
要求设计宇哥时间复杂度为O(n)、空间复杂度为O(l)的算法，实现字符串A从给定位置开始旋转。
'''


def string_spin1(s: str, n: int):
    s = s.split(",")
    l1, l2 = s[0:n], s[n:]
    print(",".join(x for x in l2 + l1))


if __name__ == '__main__':
    string_spin1("a,b,c,d,e", 3)
    string_spin1("a,b,c,d,e,f,g,h,i", 5)

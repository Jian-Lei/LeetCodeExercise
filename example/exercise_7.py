#!/usr/bin/env python
# coding=utf-8
"""
Auther: jian.lei
Email: leijian0907@163.com

给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2*31,  2*31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
https://leetcode-cn.com/problems/reverse-integer/
"""


def reverse(x):
    """
    :param x: int
    :return:
    """
    if "-" in str(x):
        y = str(x)[1:]
    else:
        y = str(x)
    ll1 = [i for i in y]
    ll1.reverse()
    num = int("".join(ll1))
    if "-" in str(x):
        num = 0 - num
    return num if -2147483648 < num < 2147483647 else 0


if __name__ == "__main__":
    s1 = -4567890
    s2 = 1534236469
    print(reverse(s1))
    print(reverse(s2))

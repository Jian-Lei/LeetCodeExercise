#!/usr/bin/env python
# coding=utf-8
"""
Auther: jian.lei
Email: leijian0907@163.com

将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
https://leetcode-cn.com/problems/zigzag-conversion/
"""


def convert(s, numRows):
    if numRows == 1:
        return s
    result = [''] * numRows
    cycle = numRows * 2 - 2
    for i in range(len(s)):
        print(i % cycle, cycle - i % cycle)
        row = (i % cycle if i % cycle <= cycle - i % cycle else cycle - i % cycle)
        result[row] += s[i]
    return ''.join(result)


if __name__ == "__main__":
    s1 = "PAYPALISHIRING"
    num = 4
    print(convert(s1, num))
